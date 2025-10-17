import time
from pyspark.sql.functions import col, broadcast, when, rand, udf, concat, lit, floor, split, spark_partition_id
from pyspark.sql.types import IntegerType

# Disable AQE
spark.conf.set("spark.sql.adaptive.enabled", "false")

# Disable Auto Broadcasting 
spark.conf.set("spark.sql.autoBroadcastJoinThreshold", -1)


### Caching
def expensive_row_operation(value):
    time.sleep(0.1) 
    return value * 2

spark.udf.register("expensive_udf", expensive_row_operation, IntegerType())

base_small_df = spark.range(1000).toDF("id")

disk_cached_df = base_small_df.selectExpr("id", "expensive_udf(id) as result")

start_time = time.time()
expensive_df.show()
end_time = time.time()

end_time - start_time

expensive_df.count()


base_large_df = spark.range(2000).toDF("val")

cached_expensive_df = base_large_df.selectExpr("val", "expensive_udf(val) as doubleVal").cache()

cached_expensive_df.count()

start_time = time.time()
cached_expensive_df.show()
end_time = time.time()

end_time - start_time


###############################################################################################


#### JOIN (Broadcasting)
large_df = spark.range(20_000_000) \
    .withColumn("id", (col("id") % 10)) \
    .withColumn("data", rand())

dimension_data = [(i, f"Group_{i}") for i in range(10)]
dimension_df = spark.createDataFrame(dimension_data, ["id", "group_name"])

result_df = large_df.join(dimension_df, on="id", how="inner")

start_time = time.time()
result_df.show()
end_time = time.time()


## After broadcasting 
broadcast_result_df = large_df.join(broadcast(dimension_df), on="id", how="inner")
broadcast_result_df.write.format("noop").mode("overwrite").save()


#### Group BY (Salting)

skewed_data = [("USA",)] * 9_000_000 + \
              [("Canada",)] * 250_000 + \
              [("Mexico",)] * 250_000 + \
              [("UK",)] * 250_000 + \
              [("Germany",)] * 250_000

skewed_df = spark.createDataFrame(skewed_data, ["country"])
agg_df = skewed_df.groupBy("country").count()
agg_df.write.format("noop").mode("overwrite").save()



SALT_FACTOR = 5
salted_df = skewed_df.withColumn(
    "salted_country",
    concat(col("country"), lit("_"), (floor(rand() * SALT_FACTOR)).cast("string"))
)

partial_agg = salted_df.groupBy("salted_country").count()

final_agg = partial_agg.withColumn(
    "country",
    split(col("salted_country"), "_").getItem(0)
).groupBy("country").sum("count")
final_agg.show()
