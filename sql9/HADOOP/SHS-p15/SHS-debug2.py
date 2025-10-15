import pyspark
from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.types import StructType, StructField, StringType, IntegerType, DateType, TimestampType

spark = SparkSession.builder.master("local")\
        .appName("News_Platform_Analytics")\
        .getOrCreate()

user_profile_schema = StructType([
    StructField("user_id", StringType(), True),
    StructField("age", IntegerType(), True),
    StructField("region", StringType(), True),
    StructField("gender", StringType(), True)
])

article_metadata_schema = StructType([
    StructField("article_id", StringType(), True),
    StructField("title", StringType(), True),
    StructField("category", StringType(), True),
    StructField("publish_date", DateType(), True),
    StructField("author", StringType(), True)
])


user_activity_schema = StructType([
    StructField("user_id", StringType(), True),
    StructField("article_id", StringType(), True),
    StructField("action", StringType(), True),
    StructField("timestamp", TimestampType(), True),
    StructField("time_spent", IntegerType(), True)
])

user_profile_df = spark.read.format("csv")\
                    .option("header","true")\
                    .schema(user_profile_schema)\
                    .load("/Users/dhiraj/Downloads/E2EDemo/user_profile_new.csv")

article_metadata_df = spark.read.format("csv")\
                        .option("header","true")\
                        .schema(article_metadata_schema)\
                        .load("/Users/dhiraj/Downloads/E2EDemo/article_metadata.csv")

user_activity_df = spark.read.format("csv")\
                    .option("header","true")\
                    .schema(user_activity_schema)\
                    .load("/Users/dhiraj/Downloads/E2EDemo/new_user_activity.csv")

# article_metadata_df = article_metadata_df.withColumn("published_date_typed", to_date(col("publish_date")))
# user_activity_df = user_activity_df.withColumn("timestamp_typed", to_timestamp(col("timestamp")))
# article_metadata_df = article_metadata_df.drop(col("publish_date")).withColumnRenamed("published_date_typed", "publish_date")
# user_activity_df = user_activity_df.drop(col("timestamp")).withColumnRenamed("timestamp_typed", "timestamp")

mean_age = int(user_profile_df.agg(avg(col("age"))).collect()[0][0])
user_profile_df = user_profile_df.fillna(mean_age, ["age"])

user_profile_df = user_profile_df.withColumn(
    "gender_typed",
    when(col("gender") == "female", "Female")\
    .when(col("gender") == "male", "Male")\
    .when(col("gender") == "MALE", "Male")\
    .otherwise(col("gender"))
)

user_profile_df = user_profile_df.drop(col("gender")).withColumnRenamed("gender_typed", "gender")

user_activity_df = user_activity_df.filter(col("time_spent") > 0)

activity_with_date = user_activity_df.withColumn("report_date", to_date(col("timestamp")))
# Join activity with article metadata to get 'category'
joined_df = activity_with_date.join(
 article_metadata_df,
 on="article_id",
 how="left"
)

# Join the result with user profiles to get 'region' and 'gender'
full_joined_df = joined_df.join(
 user_profile_df,
 on="user_id",
 how="left"
)
full_joined_df = full_joined_df.cache()
full_joined_df.count()

dau_df = full_joined_df.groupBy("report_date").agg(
    count_distinct("user_id").alias("daily_active_users"),\
    sum("time_spent").alias("total_time_spent")
)

engagement_by_action_df = full_joined_df.groupBy("report_date").agg(
    sum(when(col("action") == "like", 1)).alias("liked_count"),
    sum(when(col("action") == "share", 1)).alias("shared_count"),
    sum(when(col("action") == "read", 1)).alias("read_count")
).withColumn(
    "engagement_by_action",
    to_json(
        struct(
            col("liked_count").alias("like"),
            col("shared_count").alias("share"),
            col("read_count").alias("read"),
        )
    )
).select(
    "report_date", 
    "engagement_by_action"
)

region_engagement = full_joined_df.groupBy("report_date", "region").agg(
    count_distinct("user_id").alias("dau")
).groupBy(
    "report_date"
).agg(
    map_from_entries(
        collect_list(
            struct("region", "dau")
        )
    ).alias("engagement_by_region")
)

# views per category 
view_per_category_df = full_joined_df.groupBy("report_date", "category").agg(
    sum(when(col("action") == "read", 1)).alias("view_per_category")
).groupBy(
    "report_date"
).agg(
    map_from_entries(
        collect_list(
            struct(
                "category",
                "view_per_category"
            )
        )
    ).alias("view_per_category")
)

full_df = dau_df.join(
    engagement_by_action_df, 
    on="report_date",
    how="inner"
).join(
    region_engagement,
    on="report_date",
    how="inner"
).join(
    view_per_category_df,
    on="report_date",
    how="inner"
)

full_df.coalesce(1).write.mode("overwrite").parquet("/Users/dhiraj/Downloads/E2EDemo/dailyHuntOutput")

spark.stop()
