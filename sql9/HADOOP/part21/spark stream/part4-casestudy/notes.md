


Batch systems process data in large chunks at set intervals, prioritizing high throughput over immediate results, while streaming systems process data continuously in real-time as it arrives, prioritizing low latency. Batch processing is used for tasks like monthly reports or data backups, whereas stream processing is ideal for real-time applications like fraud detection or social media monitoring. [1, 2] 
Feature [1, 2, 3, 4, 5, 6] 
Batch System 	Streaming System 
Data Processing 	Processes data in large, scheduled chunks. 	Processes data continuously as a live stream. 
Latency 	High (minutes to hours). 	Low (milliseconds to seconds). 
Use Cases 	Periodic reports, billing, data backups. 	Real-time analytics, fraud detection, live monitoring. 
Complexity 	Generally less complex due to predictable data. 	More complex due to constant, unpredictable data flow. 
Data Handling 	Processes a complete, consistent dataset. 	Handles individual records or micro-batches, with potential for out-of-order or missing data. 
Error Handling 	Errors are detected and corrected after processing is complete. 	Requires immediate fault tolerance and real-time error handling. 














<img width="451" height="702" alt="image" src="https://github.com/user-attachments/assets/d6217728-3581-4298-9b2c-27cffeda7193" />

Zepto is an e-commerce platform for purchasing groceries and coffee, used as a case study.

Spark stream - A component of Apache Spark that enables processing of real-time data streams.

Parquet - A columnar storage file format optimized for use with big data processing frameworks.

Medallion Architecture. -An architecture pattern using layers like raw, bronze, silver, and gold data for structured data processing.

Spark Script for Order Details
	•	Objective: Track order details to manage logistics and perform comprehensive data analysis on revenue streams by considering different parameters such as category and city-wise data splits【4:0†source】 .
	•	Procedure:
	1	Data Source Initialization:
	▪	Use PySpark to establish a Spark session.
	▪	Configure Kafka as a data broker for streaming data【4:0†source】 .
	2	Data Transformation:
	▪	Deserialization: Convert streaming data from JSON strings to structured formats using predefined schemas (event type, order ID, user ID, etc.)【4:17†source】 .
	▪	Use Spark functions like explode to flatten nested data structures for further analysis【4:4†source】 .
	3	Data Storage:
	▪	Store transformed data into Hadoop Distributed File System (HDFS) in Parquet format, enabling efficient querying and data analysis .
	4	SQL Analysis:
	▪	Execute SQL queries on Parquet files to derive insights on sales trends such as revenue, order distribution, and customer preferences【4:0†source】 .
