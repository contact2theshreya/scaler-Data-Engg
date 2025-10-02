
If u store entire data in all nodes then joining will be faster, this is distribute all style
Distribute style even  -  use it if there is no way to divide that is if table does not have PK ex log does not have id,we filter based on time range so we can divide this data across multiple nodes
There is no need to join on log table
U can create table in redshift clister and load data from s3 using IAM


<img width="406" height="169" alt="image" src="https://github.com/user-attachments/assets/6775e054-9e63-4891-91b1-d82c2956434d" />

<img width="362" height="92" alt="image" src="https://github.com/user-attachments/assets/26d62515-240e-46af-b04d-486a615f49b7" />

<img width="434" height="249" alt="image" src="https://github.com/user-attachments/assets/2407f4a0-f5f0-46ef-970c-7298a60cd223" />

<img width="243" height="110" alt="image" src="https://github.com/user-attachments/assets/258cbcbe-0ee4-490c-8115-d507b4d8ee27" />

In aws we call key type as none distribution
Raw data -null values,videos,non normalized datta
Data lakes – u don’t define schema before writing to datat lakes,we transform raw datat in data lakes only if it is required 
Data ware house – u 100% trandorm it to remove unnecessary data and later on u load it

In meta source of data lake I need schema and schema is present in glue which linke to dynamo and create schema and etl step will output to s3

<img width="452" height="367" alt="image" src="https://github.com/user-attachments/assets/e7d04bec-a50a-43cd-b80e-7d3421341a2d" />

<img width="371" height="243" alt="image" src="https://github.com/user-attachments/assets/f5be9307-cd7f-491d-bc9d-038b3cb28754" />

<img width="452" height="281" alt="image" src="https://github.com/user-attachments/assets/a3c2c80c-579d-4544-b017-a0e4b0349d47" />

<img width="452" height="305" alt="image" src="https://github.com/user-attachments/assets/9dda0452-8fa3-4526-a3fe-29a94b71635e" />

<img width="452" height="300" alt="image" src="https://github.com/user-attachments/assets/cf99f0f5-12a4-4669-9762-f134a05a1458" />

Distribution key

A method in AWS Redshift to distribute data across nodes for parallel processing.

Sort key

AWS Redshift method to define how data is ordered within each node.

AWS Redshift

A fully managed data warehouse service from Amazon.

Dynamo db

Managed NoSQL database service on AWS for semi-structured data.

AWS Glue

ETL service from AWS that automates the process of data cataloging and processing.

AWS Athena

Serverless query service to analyze data in Amazon S3 using SQL.

Data Governance

Policies and procedures to manage data availability, usability, and security.

Auto Distribution Style

AWS Redshift feature that adjusts data distribution strategy based on workload.




