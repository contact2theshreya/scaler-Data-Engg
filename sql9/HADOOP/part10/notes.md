Introduction to Spark Core Components
Spark is a powerful data processing framework designed for scalability and ease of use. It is typically structured into three main components or layers:

Cluster Management: This includes YARN and HDFS. It is responsible for resource allocation and management in a distributed computing environment【4:2†transcript.txt】.

Spark Core: Known as the "heart" of Spark, it provides low-level APIs and is involved with RDDs (Resilient Distributed Datasets), task scheduling, and DAG (Directed Acyclic Graph) scheduling【4:1†transcript.txt】.

High-Level APIs: Built on top of Spark Core, these include libraries for machine learning, SQL, and streaming, allowing for more abstract interactions with data【4:1†transcript.txt】.

Components Explored
Resilient Distributed Datasets (RDDs)
Definition: RDDs are immutable distributed collections of objects that allow for data operations across a Spark cluster. They form the backbone of Spark's data manipulation capabilities【4:3†transcript.txt】.

Creation: RDDs can be created from:

A file within a distributed file system (e.g., HDFS) using methods like sc.textFile.
A parallel collection in the resident programming language.
Another RDD through transformations【4:8†transcript.txt】.
Features of RDDs
Lazy Evaluation: RDD operations are computed only when an action requires a result to be returned to the driver program. This helps with optimization and efficiency【4:4†transcript.txt】.

In-Memory Computation: Data is processed in memory for speed and efficiency, only spilling to disk when there is a need due to memory constraints【4:15†transcript.txt】.

Fault Tolerance: RDDs automatically recover from node failures. If an executor fails, Spark can recreate lost data through lineage information【4:15†transcript.txt】.

Transformations vs Actions
Transformations: Operations that create a new RDD from an existing one. They are lazy, meaning computations are not carried out immediately. Types of transformations include:

Narrow: Operate on a single data partition, e.g., map, filter.
Wide: Cause a shuffle of data between partitions, e.g., groupByKey【4:11†transcript.txt】【4:18†transcript.txt】.
Actions: Trigger the execution of transformations, followed by returning a result to the driver. Examples include collect, count, and saveAsTextFile【4:8†transcript.txt】.

Example of Lazy Evaluation
When attempting to load a non-existent file using an RDD creation method like sc.textFile, no error is thrown until an action, such as collect or count, is executed【4:12†transcript.txt】.

Data Locality and Execution
Spark is designed to optimize data locality by placing computations as close as possible to the data it operates on. This minimizes data transfer across the network【4:0†transcript.txt】.

################ 

RDD

Resilient Distributed Dataset, fundamental data structure of Spark, used to perform parallel operations on the cluster.

Parallelize

Method to distribute a local data set to form an RDD.

Action - Operations in Spark that trigger the execution of previously specified transformations.

Transformation

Operations that create a new RDD from an existing RDD, like map or filter.

Lazy evaluation

Spark's strategy of delaying computation until an action is invoked for optimization purposes.

Map- A transformation that applies a function to all items in an RDD and returns a new RDD.

Collect- An action which retrieves the entire dataset from the cluster to the driver program.

Count-An action that returns the number of elements in an RDD.

Job-A sequence of transformations triggered by an action in Spark.

Stage- Segments of the job's execution, separated by shuffle boundaries.

Executor-A process launched on worker nodes in a cluster to run tasks and keep data in memory.
<img width="468" height="383" alt="image" src="https://github.com/user-attachments/assets/4b42a1b5-9175-45e4-b0fb-938ff29f8fe4" />
