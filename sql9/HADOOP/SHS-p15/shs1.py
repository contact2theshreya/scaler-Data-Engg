from pyspark.sql import SparkSession
from pyspark.sql.functions import col, rand

spark = SparkSession.builder \
    .appName("Analyze_Jobs") \
    .master("local[*]") \
    .config("spark.sql.shuffle.partitions", "200") \
    .config("spark.sql.autoBroadcastJoinThreshold", -1) \
    .config("spark.sql.adaptive.enabled", "false") \
    .getOrCreate()


large_df = spark.range(20_000_000) \
    .withColumn("id", (col("id") % 10)) \
    .withColumn("data", rand())

dimension_data = [(i, f"Group_{i}") for i in range(10)]
dimension_df = spark.createDataFrame(dimension_data, ["id", "group_name"])

result_df = large_df.join(dimension_df, on="id", how="inner")
result_df.write.format("noop").mode("overwrite").save()


skewed_data = [("USA",)] * 9_000_000 + \
              [("Canada",)] * 250_000 + \
              [("Mexico",)] * 250_000 + \
              [("UK",)] * 250_000 + \
              [("Germany",)] * 250_000

skewed_df = spark.createDataFrame(skewed_data, ["country"])

agg_df = skewed_df.groupBy("country").count()

agg_df.write.format("noop").mode("overwrite").save()



# def print_partitions(df, name):
#     num_partitions = df.rdd.getNumPartitions()
#     print(f"'{name}' has {num_partitions} partitions.")

base_df = spark.range(10_000_000, numPartitions=4)
# print_partitions(base_df, "Base DataFrame")

repart_by_num_df = base_df.repartition(10)
# print_partitions(repart_by_num_df, "Repartition by Number")
repart_by_num_df.write.format("noop").mode("overwrite").save()


df_with_key = base_df.withColumn("key", col("id") % 3)

repart_by_col_df = df_with_key.repartition(5, "key")
repart_by_col_df.write.format("noop").mode("overwrite").save()
spark.stop()

