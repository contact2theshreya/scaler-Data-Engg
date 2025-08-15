In hadoop u give jar file to hadoop framework and it perform computation and fetch data using distributed processing and return r data

U transfer buisness logic to hadoop

Yarn - what should get how much resources

HBASE-key value*nosql db on top of hdfs

OOZIE - cron job

pig - scripting on hdfs data,solar - indexing and searching

spark,mahout - to nrun ML modals

Ingest data in HDFS - scoop and flume

FS Image - bbackup of mrtadata of namenode 

Data node-store data in  blocks of fixed size /chunks of data

Here disk space is 3 times of bytes used(coz replication factor is 3)
<img width="652" height="414" alt="image" src="https://github.com/user-attachments/assets/4da8a921-95d6-4837-a6e9-97cdfc380786" />

Map reduce - 

Components of Hadoop
HDFS (Hadoop Distributed File System): It stores data across multiple machines, providing high throughput access to application data. It breaks files into blocks and distributes them across nodes in a cluster【4:9†handwritten.pdf】.

YARN (Yet Another Resource Negotiator): It manages and schedules resources across the cluster.

MapReduce: A programming model used for processing large data sets with a distributed algorithm on a Hadoop cluster【4:9†handwritten.pdf】.

ZooKeeper: It is used for maintaining configuration information, naming, providing distributed synchronization, and providing group services【4:13†transcript.txt】.

Additional Tools: Hadoop ecosystem includes various other tools such as Hive for data warehousing, Spark for processing large amounts of data in-memory, and Kafka for streaming【4:10†transcript.txt】.

Hadoop Versions
Hadoop 1.x: It had a single name node which was a single point of failure.
Hadoop 2.x: Introduced standby name nodes to avoid single points of failure.
Hadoop 3.x: Introduces improvements including better fault tolerance and potentially unlimited name nodes and data nodes【4:4†transcript.txt】.
Detailed Study of HDFS
Master-Slave Architecture
HDFS employs a master-slave architecture consisting of:

NameNode (Master): Manages the metadata and namespace. It keeps track of the file block locations【4:11†transcript.txt】.

DataNodes (Slaves): Responsible for storing the actual data. They report to the NameNode and handle read and write requests【4:9†handwritten.pdf】.

Communication between NameNode and DataNodes occurs through the TCP/IP protocol. DataNodes send heartbeat signals to ensure they are active【4:11†transcript.txt】【4:19†transcript.txt】.

Block Storage and Replication
HDFS stores files in blocks, typically 128 MB each. Blocks are replicated across nodes to ensure data reliability and availability, typically with a replication factor of 3【4:0†transcript.txt】【4:9†handwritten.pdf】.

File System Operations
Splitting: When you input a large file, HDFS splits it into blocks and stores each block across various DataNodes【4:1†transcript.txt】.
Rack Awareness: This ensures that data is not only replicated across nodes but also across different racks for better fault tolerance【4:12†transcript.txt】.
Challenges in Distributed Systems
Scalability: Vertical scaling (adding resources to the existing nodes) hits a limit, and horizontal scaling (adding more nodes) is preferred.

Fault Tolerance: It's crucial to maintain data consistency across distributed nodes. This necessitates a robust replication strategy【4:17†transcript.txt】【4:4†transcript.txt】.

Data Consistency: Ensuring consistently updated data across nodes can be a challenge【4:3†transcript.txt】.

Conclusion
Hadoop, as a framework, provides essential solutions for managing and processing large data sets in a distributed manner. Its architecture, primarily through HDFS, ensures data reliability, efficient storage, and scalability. Distributed systems are foundational in today’s data-driven world, addressing the needs of modern enterprises by allowing them to leverage large-scale computational power with cost-effectiveness【4:15†transcript.txt】.

Commodity server - basic server in hadoop that do not require massive data resource
