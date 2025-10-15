SHS
A tool to investigate and monitor the stages and tasks in Spark jobs.

Data Skew - A situation where a disproportionate amount of data ends up in one partition, causing performance issues.

Wide Transformation - A Spark operation that requires shuffling data across the network (e.g., 'join', 'group by').

Task Deserialization Time - Time spent converting a task back from a serialized form on the executor.

GC Time - Time the JVM spends performing garbage collection, indicating potential memory issues.

Locality Level-Indicates how close tasks are run to their data; affects execution efficiency.

Execution Time - The complete duration a task takes to execute, including waiting times.

Dynamic Resource Allocation - Allows Spark to automatically add or remove jobs based on resource availability.

Shuffle Read/Write - The amount of data read/written during shuffle stages, indicating possible data skew.

Executor Bottlenecks - Occurs when some executors perform significantly slower; could be due to uneven task distribution.

Task Result Fetch Time - Duration taken to retrieve task results from the executor to the driver.

Job Stages- Discrete segments in a Spark job execution, each containing tasks that can be parallelized.


Spark Lecture Revision Notes
Introduction to Spark
Apache Spark is an open-source distributed general-purpose cluster-computing framework. It provides an interface for programming entire clusters with implicit data parallelism and fault tolerance.

Key Concepts
Driver and Executors:
Driver: The master node in which the Spark application is running.
Executors: Worker nodes that carry out the task of computation on the data and return the result.
Spark Architecture
Partitioning and Shuffling
Data within Spark is distributed across multiple nodes, a process essential for parallelism known as partitioning.
Shuffling is a process of redistributing data across partitions, which facilitates data aggregation based on a key.
Example:
Aggregating country data counts illustrates how data is distributed across partitions and then shuffled to enable counting, showing local aggregation followed by global aggregation【4:0†transcript.txt】.

Optimization and Execution
Spark History Server
The Spark History Server is a tool that helps in investigating execution tasks, helping to identify where jobs, stages, and tasks might encounter inefficiencies【4:1†transcript.txt】.

Causes and Solutions for Out-of-Memory Errors
Data Skewness:

This occurs when certain partitions contain significantly more data than others, leading to inefficiencies and potential out-of-memory errors.
Solution: Adjust partitioning logic to ensure uniform data distribution【4:16†transcript.txt】【4:17†handwritten.pdf】.
Unoptimized Transformations:

Utilizing operations that involve wide dependencies like join and groupBy without optimization can lead to data skewness and inefficiency【4:2†transcript.txt】【4:5†transcript.txt】.
Driver Out-of-Memory:

Often caused by broadcasting large variables.
Avoid serialization processes that happen in driver memory using collect or pandas as they cause excessive memory use【4:5†transcript.txt】.
Performance Tracking
Analyze job performance using Spark's ability to visualize through Directed Acyclic Graphs (DAG), track task execution time, and identify bottlenecks through stage timelines【4:12†transcript.txt】【4:13†handwritten.pdf】.
Practical Recommendations
Broadcasting: Only broadcast small datasets to executors to avoid memory issues, and minimize the use of expensive shuffle operations【4:4†transcript.txt】.
Adjusting Partition Size: Modify the number of partitions to better balance load across executors, potentially using partition coefficients【4:16†transcript.txt】.
Monitor Executors: Keep checking metrics related to task execution times, garbage collection, shuffle read/write activities, etc., to diagnose memory leaks or system stress【4:11†transcript.txt】【4:17†handwritten.pdf】.
Common Issues & Debugging
Data Skewness Detection: Identifying skewness by monitoring output sizes; excessive data transfer and tasks taking significantly longer indicates skewed distribution【4:15†transcript.txt】【4:14†transcript.txt】.
Memory Management: Regularly review execution plans, optimize SQL queries, and manage cache usage to prevent bottlenecks【4:12†transcript.txt】.
This structured overview provides a summary of techniques, tools, and strategies used in Spark for efficiently managing distributed data and computations, emphasizing performance tuning and memory management to avoid common pitfalls.
