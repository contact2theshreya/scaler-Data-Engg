Clickstream problem- volume is huge so maintaining too many data classes is problem as this is dynamic/variety of data

Make key valueClickstream problem- volume is huge so maintaining too many data classes is problem as this is dynamic/variety of data

Make key value pair of data and send to Kafkaesque
 pair of data and send to Kafkaesque

<img width="452" height="296" alt="image" src="https://github.com/user-attachments/assets/67fe42a5-845b-4877-95e0-0978ebaf0dac" />

Slot time consumed is overall time consumed by each and every individual-worker,leaf root node

Inside partition if u make cluster(group of similar data) then search will be faster

HDFS (Hadoop Distributed File System) and Amazon S3 (Simple Storage Service) are both prominent solutions for storing large datasets, but they differ significantly in their architecture, deployment, and use cases. 

HDFS: 
•	Distributed File System: HDFS is a distributed file system designed to run on commodity hardware within a Hadoop cluster. It stores data across multiple nodes and provides high-throughput access. 
•	Tightly Coupled Compute and Storage: HDFS is typically deployed alongside the compute resources (e.g., Hadoop MapReduce, Spark) that process the data. This co-location enables data locality, where processing occurs on the same nodes where the data resides, minimizing data transfer and improving performance for batch processing. 
•	On-Premise or Hybrid: HDFS is commonly used in on-premise data centers or in hybrid cloud environments where organizations have invested in Hadoop infrastructure. 
•	File System Semantics: It offers traditional file system semantics, including hierarchical directories and atomic file operations (with some limitations). 
Amazon S3: 
•	Object Storage Service: S3 is a cloud-based object storage service offered by Amazon Web Services (AWS). It stores data as objects in a flat structure within buckets. 
•	Decoupled Compute and Storage: S3 allows for the independent scaling of storage and compute resources. This flexibility enables users to scale storage as needed without affecting compute capacity, and vice-versa. 
•	Cloud-Native: S3 is a cloud-native service, designed for scalability, durability, and availability in the AWS cloud. 
•	API-Driven Access: Data in S3 is accessed via APIs (REST, SDKs), providing broad accessibility from various applications and services. 
•	High Durability and Availability: S3 offers extremely high durability and availability, designed to withstand failures and ensure data integrity. [1] 
Key Differences Summarized: 
Feature 	HDFS 	Amazon S3 
Type 	Distributed File System 	Object Storage Service 
Architecture 	Tightly coupled compute and storage 	Decoupled compute and storage 
Deployment 	On-premise, hybrid 	Cloud-native (AWS) 
Data Structure 	Hierarchical file system 	Flat object storage 
Access 	HDFS commands, API 	REST API, SDKs 
Scalability 	Limited by cluster size 	Highly scalable, elastic 
Durability/Availability 	Dependent on cluster configuration 	Extremely high (AWS managed) 
Cost 	Hardware and operational costs 	Pay-as-you-go, storage classes 
Use Cases 	Batch processing, data locality-dependent workloads 	Data lakes, backups, archives, web content, cloud-native analytics 

Datbricks – optimized spark using photon project which improves efficiency of soark coz java and scala code is converted to c++ which is closer to computer
Data lake is slow coz it infer schema on every read so data quality is low u can maintain data quality if schema on write
<img width="468" height="647" alt="image" src="https://github.com/user-attachments/assets/f37effcd-962f-4ace-877b-8f28afefdb53" />

<img width="452" height="208" alt="image" src="https://github.com/user-attachments/assets/d3b5ebd3-b8e2-4496-9d99-8d00f455d8b3" />

<img width="452" height="208" alt="image" src="https://github.com/user-attachments/assets/1b4046d5-601f-4538-8b31-e1fe48aa9f89" />

U can create table on top of your raw data<img width="468" height="50" alt="image" src="https://github.com/user-attachments/assets/e3c92ba1-fded-4be8-82e3-f86d089132b9" />

<img width="452" height="142" alt="image" src="https://github.com/user-attachments/assets/6591d2b1-1366-456d-aab2-93d46b48ada3" />

On updateion ,transaction is created with updating data on new partition and then removing old partion link (immutable) -DATA lake
Older partition will now be storted in delta log files for historical purposes
<img width="468" height="87" alt="image" src="https://github.com/user-attachments/assets/a3be4724-617b-4749-8331-26bb5aab18f6" />


<img width="452" height="236" alt="image" src="https://github.com/user-attachments/assets/263fc80e-b50f-4aa2-92a6-efc3f582d118" />

Checkpoint.parquet file is history file used as a backup
Iceberg maintains metadata in hierarchial form which keeps metadata in manifest files of partition
<img width="468" height="74" alt="image" src="https://github.com/user-attachments/assets/56291f4d-cab9-40ef-81c7-3fc920764d03" />

<img width="391" height="147" alt="image" src="https://github.com/user-attachments/assets/db136f69-c93e-402f-8c8e-975d5360ad04" />

\
Snowflake uses iceberg and data lake is used by databricks
Processing Issue - An error occurred while handling the files, indicating a problem that needs resolution.
Re-uploading Files - Resending the files may help to correct the issue and allow for successful processing.

This class covers modern data storage and management concepts with a focus on Delta Lake, Iceberg, and medallion architecture in Databricks. It also explores comparisons with other technologies like Snowflake and Redshift.
Key Concepts
Delta Lake
Delta Lake is an open-source storage layer that brings ACID transactions to Apache Spark and big data workloads. It helps manage and operationalize a data lake.
•	ACID Transactions: Ensures reliable and atomic transactions, which means a series of operations are completed successfully, or none are. This is crucial for maintaining data integrity and consistency.
•	Schema Enforcement and Evolution: Delta Lake can enforce schemas when data is written, ensuring quality and consistency over time.
•	Time Travel: This feature allows the retrieval of historical data captured in the Delta Lake table. It can be helpful in audit histories and data backups.
•	Delta Log: A special folder where transaction logs are stored. The metadata essential for achieving immutability and version control is maintained here【4:0†source】【4:5†source】.
Medallion Architecture
Medallion Architecture is a hierarchical organizational structure that is used to manage and refine data in a data lake. It is composed of three layers:
1.	Bronze Layer: Raw data is ingested and stored here. It represents the landing zone for all incoming data with minimal transformations - often the raw ingestion or application logs【4:7†source】【4:18†source】.
2.	Silver Layer: This layer contains cleansed and filtered data. It's a place for applying business-level transformations and enrichments【4:19†source】.
3.	Gold Layer: Aggregate, business-level data resides in this layer. It is optimized for business-level queries and reporting【4:15†source】【4:19†source】.
Apache Iceberg
Apache Iceberg is an open-source table format for huge analytic datasets. Built to be an improvement over Hive tables, it allows the handling of petabytes of information with capabilities such as ACID transactions, schema evolution without downtime, and efficient garbage collection.
•	Hierarchical Metadata Storage: Iceberg maintains metadata hierarchically as a series of files, allowing efficient data read operations.
•	Immutability: Similar to Delta Lake, Iceberg treats changes as new files rather than altering existing ones, following immutable data design principles【4:3†source】【4:6†source】.
Comparisons with Other Technologies
•	Snowflake: Uses isolated processes for storage and compute which allows it to efficiently scale horizontally and vertically.
o	Snowflake's Utilization of Iceberg: Snowflake adopts Iceberg for implementing data lakehouse capabilities.
•	Redshift and BigQuery: These platforms are more traditional data warehouses with robust querying capabilities, but can face limitations with unstructured or semi-structured data【4:16†source】【4:17†source】.



<img width="451" height="685" alt="image" src="https://github.com/user-attachments/assets/56d06c19-514f-449a-bf99-58abb60c4e24" />
