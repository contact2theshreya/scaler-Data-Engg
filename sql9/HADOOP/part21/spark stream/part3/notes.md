Apache Flink - An open-source distributed data processing framework for streaming and batch processing.

Spark streaming - A framework for real-time data stream processing using micro-batches.

Real-Time Streaming - Processing data as it comes in without delay, exemplified by Apache Flink.

Micro-Batch Processing -v A method used in Spark Streaming to process data in small batches.

Stateful Processing - Maintaining state of operations for fault tolerance in distributed systems. 
 
Event driven arch - A framework where events trigger actions, used in Apache Flink.

Event Time Processing - Handling data based on original occurrence time rather than arrival time in Flink.

Agenda
Introduction to Apache Airflow
Demo for Airflow
Real-life example
Introduction to Apache Flink
Apache Flink internals
Comparison: Spark vs. Flink
Apache Airflow
Overview
Apache Airflow is an open-source platform designed for orchestrating complex data workflows. It is developed using Python, allowing workflows to be defined as code, commonly referred to as Directed Acyclic Graphs (DAGs). Originally developed by Airbnb, it has been widely adopted due to its flexibility and extensibility .

Components of Apache Airflow
DAG (Directed Acyclic Graph):

The heart of Airflow, defining the sequence of tasks and their relationships. DAGs ensure that each task is executed with dependencies aptly resolved【6:0†source】.
Scheduler:

A background job that orchestrates the execution of tasks and monitors DAG directories to enqueue task instances for execution【6:0†source】.
Metadata Database:

Stores details about task runs, task durations, success/failure states, and dependencies. While the default is SQLite, production setups often use Postgres【6:0†source】.
Web Server and UI:

Provides a UI for users to monitor and interact with various workflows and DAGs【6:0†source】.
Workers:

These are the machines (physical or virtual) where actual task execution happens. They can run tasks defined in various scripts like Python or Bash【6:0†source】.
Logs:

Keeps unstructured data on task execution, enabling debugging and monitoring .
Use Cases
Batch-oriented workflows: Airflow is optimal for orchestrating tasks that require sequential execution with dependencies .
Example in Airflow
ETL Pipeline:
Tasks in a typical Airflow DAG might include data extraction, transformation, and loading (ETL) processes, each defined as a separate task within the DAG .
Apache Flink
Overview
Apache Flink is an open-source distributed data processing framework tailored for both batch and streaming workloads. It excels in real-time data processing, offering significant performance benefits for stream processing .

Features of Apache Flink
Event-Driven Architecture:

Processes each piece of data individually as an event, enabling precise handling of streaming data .
Stateful Processing:

Maintains state information across events to ensure accurate processing and fault tolerance. States can be stored in systems like HDFS or S3 .
Fault Tolerance:

Achieved through checkpointing and state maintenance, ensuring resilience against failures .
Scalability:

Flink can scale both horizontally and vertically depending on workload needs .
True Stream Processing:

Unlike micro-batch processing (e.g., in Spark Streaming), Flink processes data in real-time as it arrives .
Comparison: Apache Spark vs. Apache Flink
Batch vs Streaming:
While both can handle batch processing, Flink is more optimized for real-time streaming, offering session-based window functions not available in Spark .
Fault Tolerance:
Both systems use state and checkpoints for fault tolerance, but Flink's event-driven architecture offers an edge for stateful stream processing .
Machine Learning Capability:
Spark currently leads with more developed machine learning capabilities .
Example in Flink
Real-Time Streaming:
Handles transactions such as bank operations in real time, managing each transaction as a separate event .

/////////

Defines task that are part of workflow in dag file<img width="468" height="50" alt="image" src="https://github.com/user-attachments/assets/5963645c-4ac7-4826-a3d4-8f623896c402" />


<img width="452" height="259" alt="image" src="https://github.com/user-attachments/assets/48f8c6da-8814-451e-9a3f-958fc24cfee3" />

<img width="250" height="146" alt="image" src="https://github.com/user-attachments/assets/64932544-7b11-4cac-a12a-acfc09ef78a8" />

<img width="258" height="122" alt="image" src="https://github.com/user-attachments/assets/f660fc9a-e17e-4fd4-b6f6-6ea7513d38e3" />

<img width="452" height="237" alt="image" src="https://github.com/user-attachments/assets/001e98a5-d5c8-4a15-88de-e66194f47b08" />


Kafka doesn’t process event whereas apache flink does(transformation like groupby)
Kafka is source of apache flink
Spark streaming/flink is consumer of kafka
<img width="468" height="125" alt="image" src="https://github.com/user-attachments/assets/d60e5179-285d-4abe-a090-c9bd7765fa12" />
