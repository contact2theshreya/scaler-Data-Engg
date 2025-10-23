
Spark Structured Streaming Output Types

Complete
Append
Update
Checkpointing in Spark Structured Streaming

Fault Tolerance
State Management
Introduction to Kafka

Kafka Architecture
Components of Kafka
Demo of Kafka【6:11†transcript.txt】【6:19†handwritten.pdf】.
Detailed Notes
Spark Structured Streaming Output Types
Complete Mode: Outputs all rows of the result table in every trigger, regardless of any updates made to the result set.

Append Mode: Adds only new rows since the last trigger to the output.

Update Mode: Similar to append but emits only the rows that were updated since the last trigger【6:13†transcript.txt】【6:19†handwritten.pdf】.

Example: For a series of input strings such as "hi hi hi how are you", the output captures distinct word counts. For instance:

hi appears 3 times
how, are, you appear once each【6:13†transcript.txt】【6:19†handwritten.pdf】.
Checkpointing in Spark
Purpose: Checkpointing is essential for achieving fault tolerance and managing state in Spark streaming applications.

How it Works:

It keeps track of offsets and state in a distributed environment using an HDFS path.
Before performing any action, the offset is recorded, and after the action, the results are committed via offsets【6:8†transcript.txt】【6:19†handwritten.pdf】.
Steps in Spark Streaming with Checkpointing:

Read the micro-batch.
Update offsets.
Execute transformations.
Commit results to the sink (like HDFS or a database).
Use checkpoints for recovery in case of failures【6:9†transcript.txt】【6:19†handwritten.pdf】.
Introduction to Kafka
What is Kafka?: Kafka is an event streaming platform capable of handling trillions of events a day. It is widely used for building real-time data pipelines and streaming apps.
Key Features: Persistence, high throughput, scalability【6:11†transcript.txt】【6:19†handwritten.pdf】.
Kafka Architecture
Components:

Producer: Creates data streams.
Broker: Servers in the Kafka cluster that store data.
Topic: A category to which messages are published.
Partition: Messages are split across partitions within topics.
Offset: An ID given to each message within a partition.
Consumer: Reads data streams.
Zookeeper: Keeps track of the Kafka cluster state【6:17†transcript.txt】【6:19†handwritten.pdf】.
Architecture Overview:

Kafka works as a cluster, which can be replicated for fault tolerance.
Messages are persisted, allowing consumers to read messages at varying rates【6:17†transcript.txt】【6:19†handwritten.pdf】.
Kafka Demo Steps
Start the Kafka service.
Create a topic.
Start a producer to send data to the topic.
Start a consumer to read data from the topic【6:10†transcript.txt】【6:19†handwritten.pdf】.
Example Use Cases and Features
Kafka serves as a bridge between producers and consumers, analogous to how a post office works in delivering messages.
It supports high-throughput messaging with robust scaling, parallelism through partitioning, and guarantees data persistence【6:14†transcript.txt】【6:19†handwritten.pdf】.

checkpointing - A Spark Streaming feature to maintain state and fault tolerance by storing offsets.

throughput - Kafka’s ability to handle high volumes of data transactions per second.
