Redistributing data is important to avoid skewness coz all of them will have same count

<img width="452" height="244" alt="image" src="https://github.com/user-attachments/assets/baa50d51-d7b4-40f8-b899-7606bf972615" />

In colasesce - Smaller partition will have data skewness and if all partition will get same no of cores then biger partition will suffer coz it has lot to complete so solution is merging. Of smaller partition so that all can have same data
We have 8 partition by default and on join,groupby (wide transformation)spark create 200 partition

IN CASE OF SALTING
<img width="468" height="176" alt="image" src="https://github.com/user-attachments/assets/f36ac723-de2e-4228-9592-399019a0b941" />

<img width="452" height="186" alt="image" src="https://github.com/user-attachments/assets/482c578e-c598-4839-a579-52986e97807b" />

IF WE WANT TO COUNT REVENUE/COUNTRY then we group by country 
If we group by usa or india we get 1-1 group but if we group by right column then we will get 4 group of USA which is incorrect

Spark partition has sizd-128 to 256MB
<img width="468" height="142" alt="image" src="https://github.com/user-attachments/assets/86d6ba21-33ac-4f93-adbb-b33f6fc45326" />

Introduction to Data Skewness
Data skewness is a common problem in distributed computing where a large amount of data resides in a small number of partitions. This can lead to some partitions being assigned disproportionately more work, causing inefficiencies. When working with systems like Spark, addressing data skewness is crucial to ensure efficient data processing and resource utilization【4:1†transcript.txt】.

Concept of Salting
Salting is a technique used to address data skewness by modifying key values to distribute data more evenly across partitions. This involves appending a random suffix to the keys, turning singular frequent entries into multiple unique entries, thus allowing for a more balanced data distribution across partitions【4:0†transcript.txt】【4:6†transcript.txt】.

How Salting Works
Initial Skewed Data: Consider a data set where 90% of the records have the key 'USA'.
Applying Salt: Convert each instance of 'USA' to 'USA_0', 'USA_1', 'USA_2', etc., across a range determined by a salt factor. For instance, using a salt factor of 5 might distribute the data into 'USA_0' to 'USA_4'【4:0†transcript.txt】【4:1†transcript.txt】.
Resulting Distribution: This ensures the data is split more evenly across partitions, enabling better parallel processing. It prevents performance bottlenecks by ensuring no single executor is overburdened【4:0†transcript.txt】.
Challenges with Salting
Original Key Loss: The main challenge with salting is that it transforms the original keys, which can complicate downstream processing. For instance, grouping by 'USA' after salting will require additional steps to combine 'USA_0' to 'USA_4' back into a single group【4:11†transcript.txt】.
Determining Salt Factor: Selecting the right salt factor often involves trial and error. It is not formulaic and depends on achieving efficient partition sizes, often recommended between 128 MB to 256 MB for systems like HDFS【4:5†transcript.txt】.
Repartitioning and Coalescing
Repartitioning and coalescing are two techniques used to manage partition sizes more effectively in Spark.

Repartitioning
Purpose: Increases the number of partitions to distribute the data more finely across available resources, thus minimizing load on individual executors【4:4†transcript.txt】【4:17†transcript.txt】.
Mechanism: When you repartition, the system creates new partitions and redistributes the data, often using a hashing or round-robin method to ensure even distribution【4:12†transcript.txt】.
Coalescing
Purpose: Reduces the number of partitions and should be used when you need fewer partitions. It's useful in scenarios where reducing partition overhead is desired【4:10†transcript.txt】.
Mechanism: Coalescing reduces the number of partitions without a full data shuffle, merging smaller partitions into larger ones to optimize the process for narrow transformations【4:10†transcript.txt】.
Practical Applications in Spark
Managing Task Load: By using salting and (re)partitioning techniques, the computational workload is distributed more evenly across available executors. This maximizes resource utilization and minimizes execution time【4:7†transcript.txt】.
Code Example: A typical Spark operation might involve transforming skewed data by adding a salt factor, followed by repartitioning to distribute the data evenly:
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, lit, rand

spark = SparkSession.builder.master("local").appName("SaltingExample").getOrCreate()

# Example DataFrame with skewed data
data = [("USA",), ("USA",), ("USA",), ("IND",), ("CAN",)]
df = spark.createDataFrame(data, ["country"])

# Add a 'salt' column
salted_df = df.withColumn("salt", (rand()*5).cast("int")).withColumn("country_salted", col("country") + "_" + col("salt"))

# Repartitioning to balance load
balanced_df = salted_df.repartition(5, col("country_salted"))
balanced_df.show()


Repartitioning - Splitting up or shuffling data based on input parameters to increase or redistribute partitions in Spark【4:5†transcript.txt】.

spark3.0 - Introduction of new features including Adaptive Query Execution for optimizing query execution plans【4:15†transcript.txt】.

Adaptive Query Execution (AQE) - A feature in Spark 3.0 that optimizes query plans based on runtime statistics【4:1†handwritten.pdf】.

Wide Transformation - A type of Spark transformation that involves shuffling large amounts of data across partition

Narrow Transformation - A Spark transformation where each input partition maps to exactly one output partition, minimizing data shuffling

Executor Configuration - Settings that determine how Spark allocates resources such as memory and CPU during job execution

Driver Configuration - Settings related to the Spark driver which coordinates the cluster resources and job execution

Hash Collision - Occurs when different keys map to the same hash value, potentially causing data skewness 
 
Partition ID - An identifier for partitions in Spark, crucial for understanding data distribution among partitions
