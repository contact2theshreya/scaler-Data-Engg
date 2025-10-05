In  dynamodb u cam import from s3

<img width="468" height="50" alt="image" src="https://github.com/user-attachments/assets/3a897d49-24c3-41ac-8440-373b575bc4c5" />

<img width="285" height="146" alt="image" src="https://github.com/user-attachments/assets/97dca6bf-97e7-41e1-9ce8-8a2509661f05" />

Now create crawler with dynamodb db<img width="468" height="50" alt="image" src="https://github.com/user-attachments/assets/e10295ef-b9a5-4a23-966b-8eb61b941466" />

<img width="254" height="155" alt="image" src="https://github.com/user-attachments/assets/9c68f786-36d3-4414-afd7-fa02c6a6e314" />

Create db as well in asw glue to store in data catalog and select that crated DB from dropdown<img width="468" height="67" alt="image" src="https://github.com/user-attachments/assets/f9b8bc99-b08a-4368-9012-c067061b01b8" />

<img width="297" height="92" alt="image" src="https://github.com/user-attachments/assets/9be8d492-ba61-4655-a058-37dcfa5d9772" />

Now do etl to convert raw data to golden data so that. U can use it for machine learning etc
Create etl to remove null values
<img width="468" height="75" alt="image" src="https://github.com/user-attachments/assets/f08d3956-8f07-4714-b028-9f67ccac4157" />

<img width="452" height="226" alt="image" src="https://github.com/user-attachments/assets/bdc2b55a-59f9-4627-b8e1-f9c900d1f1db" />

And output to s3<img width="468" height="50" alt="image" src="https://github.com/user-attachments/assets/b6787dd2-b0af-4a9e-99dd-0da5aeeff804" />

<img width="252" height="102" alt="image" src="https://github.com/user-attachments/assets/47ec0b9e-435e-4ada-8a8c-9edbda64d2ec" />


Athena is for analytics which takes data from s3 and schema from catalog  and runs a sql on top of it

Map reduce see 1 task perform it then move to next task ex-adding a column in existing table
Wheras spark first tries to plan how task is exacly implemented and create a graph of task then it implements so this lazy 
<img width="468" height="201" alt="image" src="https://github.com/user-attachments/assets/6c7621f9-38dc-4e5b-bcaf-a59be6ba2928" />


////////////////////

<img width="485" height="344" alt="image" src="https://github.com/user-attachments/assets/af64f151-d136-477f-9065-f8c0b0ed1275" />

<img width="1106" height="721" alt="image" src="https://github.com/user-attachments/assets/2dd19e3b-ecfb-497a-92f8-e02396c37a61" />

<img width="1106" height="720" alt="image" src="https://github.com/user-attachments/assets/c015c276-bab1-4713-9279-adce77256094" />

<img width="1151" height="732" alt="image" src="https://github.com/user-attachments/assets/7a49969f-733d-43c4-9172-0b183cf31810" />

<img width="1078" height="715" alt="image" src="https://github.com/user-attachments/assets/810fe00d-28b7-4b41-8049-f0e3fa633cc2" />





GLUE
 
A fully managed ETL service that processes data and moves it between various data stores.

Pyspark - A Python API for Spark that allows you to write Spark applications using Python.

Spark submit – A command to submit spark application to cluster

Athena - An interactive query service to analyze data in Amazon S3 using SQL.

DAG - Directed Acyclic Graph, represents the execution plan of Spark jobs.
<img width="468" height="150" alt="image" src="https://github.com/user-attachments/assets/dbe7c6e3-aef4-4d35-804f-b04be57db3ac" />


AWS Data Lakes
AWS Glue
AWS Glue is a fully managed data integration service that facilitates data preparation for analytics. Key components include:

Glue Crawler: Automatically scans your data sources to infer schemas and detect partitions.

Glue Data Catalog: A centralized metadata repository that acts like a Hive Metastore.

ETL Processing: Uses PySpark to transform data.

AWS Athena
Amazon Athena is a serverless query service that enables the analysis of data directly in Amazon S3 using standard SQL. It is often paired with AWS Glue to query data stored in S3 through the cataloged schemas.

S3 and Data Storage
Amazon S3 is a highly scalable, durable, and secure object storage service. It plays a critical role in storing raw and processed data within data lakes .

Demo Architecture
Source: Data starts from DynamoDB where the Netflix data is stored. This NoSQL database is similar to MongoDB or HBase.

ETL Process: Data is extracted from DynamoDB, transformed using Glue, and then loaded into S3.

Analytics: Once the data is prepared, it can be queried using Athena .

Introduction to Apache Spark
Apache Spark is a unified analytics engine for large-scale data processing. It offers the following advantages:

Fewer I/O Operations: Unlike MapReduce, Spark reduces the need for multiple reads and writes by performing operations in-memory .

In-memory Processing: This results in higher speed because data is processed in the RAM instead of disks.

Lazy Execution: Spark builds a Directed Acyclic Graph (DAG) when you define operations, deferring execution until an action (like show or count) is called .
Spark Architecture

Spark Driver: This is the master node responsible for scheduling tasks across the cluster.

Cluster Manager: Manages resources and schedules jobs (e.g., YARN, Kubernetes).

Worker Nodes: These nodes execute tasks assigned by the manager .

PySpark Basics
PySpark enables Python programming for Spark, allowing access to the Spark shell and supporting SQL-like operations on large datasets.

Basic Commands: Examples include from pyspark.sql import SparkSession, which creates a Spark session for executing SQL queries.

Executing Jobs: You can create Spark applications using Jupyter Notebooks, submitting them as .py files, or using PySpark shell .

Data Lake ETL Process

Data Ingestion: Load raw data into S3.

ETL Execution: Use Glue to transform data, e.g., clean null values, enrich the dataset with additional columns, etc.

Storing Clean Data: Load processed data back to S3 in designated output buckets.

Schema Management: Use Glue crawlers to create schemas that Athena leverages for query execution .
