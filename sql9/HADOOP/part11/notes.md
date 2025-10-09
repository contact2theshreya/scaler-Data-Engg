Redaing data from distributed machine from 1 single rdd as rdd is an abstraction it provides api to manage complex task u don’t have to write code for them

<img width="468" height="87" alt="image" src="https://github.com/user-attachments/assets/c09e9e5f-7232-4d2b-9967-cedd370dd864" />

<img width="279" height="134" alt="image" src="https://github.com/user-attachments/assets/09c84f9c-58d1-4d39-bd62-18ba855dfc13" />


2nd way to create rdd--  by list parallelized collection
Data is in list/set
<img width="468" height="100" alt="image" src="https://github.com/user-attachments/assets/2a0ae4d9-14fc-467f-8857-0fb5615f96f7" />

<img width="452" height="130" alt="image" src="https://github.com/user-attachments/assets/80ddc212-26ae-4e5c-970c-6816da6d09bc" />

Now create with 10 partition
<img width="468" height="77" alt="image" src="https://github.com/user-attachments/assets/8a9c6d75-ead2-4165-bfaf-725bb9d4a124" />

<img width="316" height="139" alt="image" src="https://github.com/user-attachments/assets/5d8a1c02-d828-4cd0-86df-5f6eaecf5893" />

Another RDD -  creatye using existing RDD
If u have spark and u perform task ,spark willl 
Redaing data from distributed machine from 1 single rdd as rdd is an abstraction it provides api to manage complex task u don’t have to write code for them
<img width="468" height="139" alt="image" src="https://github.com/user-attachments/assets/205a11bd-7285-45c2-9f27-711350b077fa" />


<img width="279" height="134" alt="image" src="https://github.com/user-attachments/assets/fde7b0f2-d13e-41f2-a4e3-167e7ebbd517" />



2nd way to create rdd--  by list parallelized collection
Data is in list/set
<img width="468" height="100" alt="image" src="https://github.com/user-attachments/assets/575d0fc9-a222-429f-838c-4c3a89d5f102" />

<img width="452" height="130" alt="image" src="https://github.com/user-attachments/assets/16892990-6417-46b0-a6eb-dfc1e820d6e3" />


Now create with 10 partition
<img width="468" height="77" alt="image" src="https://github.com/user-attachments/assets/054fe150-794f-49bc-aa2d-4b03b440d00a" />

<img width="316" height="139" alt="image" src="https://github.com/user-attachments/assets/a278f575-5446-42c4-9aab-e45a5b9a2d7c" />



Another RDD -  creatye using existing RDD
If u have spark and u perform task ,spark will create DAG and on action(like collect) all task will be performed
Wide transformation - -when u shuffle data loke in groupby ,join,sort
<img width="468" height="140" alt="image" src="https://github.com/user-attachments/assets/915245d9-a741-4e17-8513-eaa5c8c082b0" />

<img width="322" height="205" alt="image" src="https://github.com/user-attachments/assets/d7ce53d6-94c2-42d1-86ba-3fbcba779b50" />

<img width="363" height="130" alt="image" src="https://github.com/user-attachments/assets/593fbfaf-d65e-4aa1-b1e6-4fdfcbec3f9c" />

<img width="452" height="175" alt="image" src="https://github.com/user-attachments/assets/3e93e41c-af59-4a47-a016-e5d164dea54c" />

<img width="452" height="176" alt="image" src="https://github.com/user-attachments/assets/488aa835-f7e2-4b4e-a86c-12a39ab3d21d" />

U need to shufflw data in this format to perform groupby<img width="468" height="50" alt="image" src="https://github.com/user-attachments/assets/c0764442-6f25-4e46-8e33-cd4524c74f03" />

<img width="272" height="175" alt="image" src="https://github.com/user-attachments/assets/eba8354b-2b51-4930-afe3-486ca88a96af" />


Narrow transformation – apply map on indiv valkue so it is self sufficient
<img width="468" height="75" alt="image" src="https://github.com/user-attachments/assets/f9f70e3c-3280-4172-8699-245b7a705178" />

<img width="331" height="176" alt="image" src="https://github.com/user-attachments/assets/abb87a3e-429c-48f9-b754-bbd841b61ef1" />

<img width="452" height="117" alt="image" src="https://github.com/user-attachments/assets/ef84c085-eefa-4f20-a863-ea339b0254a4" />

Do this using map function<img width="468" height="50" alt="image" src="https://github.com/user-attachments/assets/bc209fb5-887c-4c6e-8510-904232341dc0" />

<img width="261" height="75" alt="image" src="https://github.com/user-attachments/assets/b8e1463f-d89d-4ad3-9790-6ce0eab67fe1" />

<img width="409" height="270" alt="image" src="https://github.com/user-attachments/assets/aa7487e4-241d-4af3-9dc5-15bc61e67c13" />

<img width="423" height="255" alt="image" src="https://github.com/user-attachments/assets/346d0c26-c2d6-4f58-b527-af5acf93ca29" />

<img width="251" height="289" alt="image" src="https://github.com/user-attachments/assets/00cf409f-7350-445d-bea8-23cf6aeca057" />

<img width="450" height="174" alt="image" src="https://github.com/user-attachments/assets/57475601-f6af-40b5-8a47-b76a988f08df" />

<img width="452" height="125" alt="image" src="https://github.com/user-attachments/assets/64c9da22-c1c6-47b5-a99d-a6b01e6d718f" />

<img width="441" height="105" alt="image" src="https://github.com/user-attachments/assets/7d83e877-2e7e-4909-8ad3-bb4112f6f285" />

<img width="452" height="275" alt="image" src="https://github.com/user-attachments/assets/8dd53c5e-5602-4f27-b985-58904ab49f8d" />

<img width="417" height="231" alt="image" src="https://github.com/user-attachments/assets/722c801f-badc-4a3e-92d2-6be719defb70" />

<img width="350" height="164" alt="image" src="https://github.com/user-attachments/assets/66db3ec6-c4c5-4b01-be66-3359bd48aeda" />

<img width="452" height="166" alt="image" src="https://github.com/user-attachments/assets/0dbd714e-069f-4ef7-a311-9c8844fe9dbd" />


<img width="452" height="196" alt="image" src="https://github.com/user-attachments/assets/f4820ff9-dd1b-4214-bdb4-c0cec9c95d5b" />


To n get max votes
<img width="468" height="75" alt="image" src="https://github.com/user-attachments/assets/366570d8-4afa-4a01-b496-c0b01821f48a" />

<img width="350" height="130" alt="image" src="https://github.com/user-attachments/assets/35c45fb6-3582-4358-9ab6-7667459db8a0" />


Solve above using spark sql – see sparksqldemo.ipynb<img width="468" height="50" alt="image" src="https://github.com/user-attachments/assets/daea1a1e-942a-44a5-a674-72658cfe6c69" />

Revision Notes for Big Data Processing with Apache Spark
Introduction to Apache Spark
Apache Spark is a unified analytics engine for big data processing, with built-in modules for streaming, SQL, machine learning, and graph processing. It simplifies the process with a higher-level API and allows concise and expressive code for working with large datasets【4:0†source】.
Resilient Distributed Datasets (RDD)
RDD Operations
Actions vs. Transformations: Spark RDDs support two types of operations:

Transformation: Builds RDDs from other RDDs. Transformations are lazy computations which are not executed immediately.
Narrow Transformations: These are transformations like map and filter where only one child RDD partition needs to read data from one parent RDD partition.
Wide Transformations: These require data to be shuffled, for example, reduceByKey. These operations involve multiple partitions.
Actions: These trigger computation and return results to the driver program or write them to storage. They include operations like collect and saveAsTextFile.

Map and FlatMap
Map: A narrow transformation that applies a function to each item in an RDD and returns a new RDD containing the results. For instance, applying a function to square each element【4:16†source】.
FlatMap: Similar to map, but each input item can be mapped to zero or more output items (so flatMap can return a sequence of items for each input).
Spark RDD and Tasks
Stages, Jobs, and Tasks:
Job: Spark creates a job for each action that you perform on an RDD.
Stage: Each job is divided into stages based on the transformations that require a shuffle, such as a wide transformation.
Task: Each stage is split into tasks which are units of work sent to the Spark executor【4:5†source】【4:6†source】.
Introduction to Spark SQL
Spark SQL: It is a Spark module for structured data processing. Unlike RDD operations, Spark SQL allows you to express complex operations like joins, filters, and aggregations in a concise syntax referred to as SQL or via a DataFrame API【4:3†source】【4:8†source】.

Components of Spark SQL:

Catalyst Optimizer: An extensible query optimization framework which enables Spark to calculate the most efficient query execution plan.
Tungsten Project: An initiative to improve the Spark execution engine, which includes memory management and binary processing enhancements【4:8†source】.
Working with DataFrames and SQL in Spark
DataFrame API: Provides a higher-level abstraction over the RDDs which allows Spark SQL to optimize execution using the Catalyst optimizer. DataFrames can be created from a variety of sources such as structured data files, tables in Hive, or existing RDDs【4:9†source】【4:19†source】.

SQL Queries in Spark: Spark SQL allows users to run SQL queries on DataFrames, providing a declarative syntax to describe both transformations on the data as well as the data itself【4:8†source】.

Practical Examples:
Reading Data with Spark SQL:

You can read a CSV file into a DataFrame using spark.read.format("csv").option("header", "true").load(filePath).
To infer the schema and skip loading the data, specify the option inferSchema as true【4:13†source】.
Joining DataFrames: To join two datasets, Spark SQL lets you use SQL syntax, e.g., movies.join(ratings, movies("movieId") === ratings("movieId"), "inner")【4:18†source】.

Filter Operations: Using the filter method in DataFrames to select rows based on certain conditions, e.g., choosing movies that belong to a particular genre【4:10†source】.



Map transformation - A one-to-one transformation that applies a function to each element to produce an output element.

FlatMap Transformation - A transformation that maps each input item to zero or more output items, effectively flattening the results.

RDD - Resilient Distributed Dataset, a fundamental data structure of Spark for distributed data.
Spark SQL- A module in Spark that integrates relational processing with Spark's functional programming API.
 
Catalyst Optimizer - An optimization framework in Spark SQL for automatically optimizing query execution.

Tungsten Execution - A Spark runtime execution engine for CPU and memory efficient data processing.

Stage - A job division in Spark that executes a series of computations with wide transformations causing shuffles.

Job- A logically organized sequence of tasks triggered by an action in Spark.

Group By Key - A function used in Spark to group data based on a common key, often used in data aggregation.

Shuffle - The process of redistributing data across partitions to group data across the cluster.

Parallelize- A Spark function used to create an RDD from a collection (e.g., list, array).




























<img width="451" height="306" alt="image" src="https://github.com/user-attachments/assets/eca226f4-e9d7-4df7-ad98-57365852100e" />
