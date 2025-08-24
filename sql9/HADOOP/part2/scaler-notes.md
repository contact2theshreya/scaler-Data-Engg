Hadoop Distributed File System (HDFS) and YARN - Comprehensive Study Notes
Overview
In this session, we covered the architecture and workings of Hadoop Distributed File System (HDFS) and YARN (Yet Another Resource Negotiator). This framework is crucial for managing and processing large datasets across clusters of computers using simple programming models.

Hadoop Distributed File System (HDFS)
HDFS is designed to reliably store very large files across machines in a large cluster. It uses a distributed file system designed to run on commodity hardware.

Key Components
NameNode:

Acts as the master server.
Manages the file system namespace and controls access by clients.
Holds the metadata including permissions, block locations, etc.【4:13†source】.
DataNode:

Acts as the slave and is responsible for storing the actual data.
DataNodes perform read and write operations as per client requests.
The data is stored in blocks (standard size: 128 MB). A large file is split into multiple blocks, each stored across different nodes【4:11†source】【4:4†source】.
Secondary NameNode:

Works as a backup to the NameNode to prevent data loss.
It helps in periodically merging the namespace image with the edit logs.
Data Placement and Replication
Block Storage and Replication:
Each file is split into blocks and stored in a fault-tolerant manner, replicated across multiple nodes.
The default replication factor is 3 (one original and two copies)【4:11†source】.
There’s a replication algorithm that ensures one block copy is created in a different rack to handle potential failures within a single rack【4:6†source】.
HDFS Operations
Write Operation:

The client contacts the NameNode to get the list of suitable DataNodes.
Data is split and sent to the listed DataNodes. On completion, an acknowledgment is sent back to the NameNode【4:13†source】【4:12†source】.
Read Operation:

To read data, the client asks the NameNode, which provides the locations of the data blocks. The client retrieves the data directly from the DataNodes in a prescribed order【4:12†source】.
Metadata Operations:

Operations such as listing files or creating directories are handled entirely by the NameNode, as they involve only metadata【4:10†source】.
Handling Failures
Heartbeats:
DataNodes send periodic heartbeats to verify their availability and functionality. Failure to send a heartbeat could mean node failure, and steps will be taken to replicate the data【4:15†source】.
YARN (Yet Another Resource Negotiator)
YARN is a resource management layer for Hadoop, separating resource management from application scheduling and monitoring. This separation enhances the system's scalability and efficiency.

Components
Resource Manager:

Scheduler: Allocates resources across the cluster using various algorithms like FIFO or Capacity Scheduling【4:9†source】.
Application Manager: Accepts job-submissions and manages the lifecycle of applications【4:9†source】.
Node Manager:

Monitors the resources (CPU, Memory) on a node and reports back to the Resource Manager.
Manages the containers on the machine【4:17†source】【4:19†source】.
Application Master:

Manages the execution of jobs and handles the resource requirements of a single job【4:19†source】.
Job Execution
YARN splits the functionalities of job-tracking into Resource Manager and Application Master. It allows multiple data processing engines such as interactive SQL, real-time streaming, batch processing, and others to run and process data stored in HDFS【4:5†source】【4:6†source】.

Container Execution
Applications in YARN run within containers, which are considered as resource allocation units within a node. Containerization makes the system resource-efficient and scalable【4:19†source】.
