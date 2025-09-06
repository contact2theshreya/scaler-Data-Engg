Fact and dimension table in olap

https://medium.com/airbnb-engineering/data-infrastructure-at-airbnb-8adfb34f169c

RDBMS does not give us fact and dimension so we have to extract data and then transform as per fact and dimension and then load the data

We sometimes denormalised data for reporting purpose ex 10years data in joining takes a lot time so we denormalise it and combine it with other data to avoid joining

Aggregation we do on fact table

I dataware house unlike data lakes we can only have structured data

Star schema - join dimension table with  fact table


Revision Notes: Data Warehousing and Hive
Introduction to Data Warehousing
Data warehouse is essentially a storage unit that supports business analytics and reporting. It typically contains a large volume of both current and historical data. A data warehouse is designed to answer business questions by aggregating massive amounts of data, often transforming raw data into urgent business analytics【4:12†source】.

Data Warehouse Components
Fact Table vs. Dimension Table
Fact Table: Stores quantitative data for analysis and is often denormalized. This table contains the metrics or facts of the business process, such as sales revenue or a number of items sold. It aggregates on numbers and metrics that you want to measure【4:12†source】【4:8†source】.

Dimension Table: Contains the descriptive attributes related to the fact data, often supporting filtering and grouping. Dimensions are ways of understanding the facts that give them context and answers to "who", "what", "where", and "when". For example, time, location, and product details are typically dimensions【4:12†source】【4:16†source】.

Schema Structures
Star Schema: Simplistic structure where a single fact table is connected to multiple dimensions. It is powerful for querying but might lead to data duplication【4:12†source】.

Snowflake Schema: Similar to a star schema, but here, dimensions are normalized, splitting data into additional tables. This reduces data redundancy but might increase complexity due to multiple joins【4:12†source】.

Galaxy Schema: Also known as the fact constellation schema. It supports multiple fact tables that share dimension tables, catering to multiple business processes【4:12†source】.

Slow Changing Dimensions (SCD) and Surrogate Keys
SCD: Reflects changes in dimension tables over time. SCD can be types like SCD Type 1 where changes overwrite existing data, or SCD Type 2 where historical data is preserved【4:12†source】.

Surrogate Keys: A sequentially incrementing number that is often used to uniquely identify each row in the fact table, ensuring faster joins and better performance across databases【4:12†source】.

Apache Hive as a Data Warehouse
Apache Hive is a data warehouse infrastructure tool that facilitates reading, writing, and managing large datasets stored in distributed storage using SQL【4:0†source】.

Architecture of Hive
HDFS (Hadoop Distributed File System): Backbone of Hive's storage capabilities, offering scalable and reliable data storage【4:13†source】.

MapReduce/YARN: Hive translates SQL queries into MapReduce jobs, executing them on Hadoop【4:10†source】.

Hive Server and Client: Acts as a communication layer. Hive uses a Client-Server architecture where you interact through HiveQL【4:3†source】.

Metastore: Stores metadata about schemas and partitions, crucial for query optimization【4:0†source】.

Use Case: Airbnb
Airbnb used Hive to solve substantial data warehousing needs, leveraging its ability to perform detailed analytics on the large datasets they collected. Their infrastructure took advantage of Hive on top of HDFS for efficient storage and retrieval【4:10†source】.
