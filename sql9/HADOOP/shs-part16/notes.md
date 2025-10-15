In today's class, we explored several advanced topics relating to debugging Spark applications, specifically focusing on memory management within Spark's execution engine. The goal was to understand the causes of memory issues and learn strategies to optimize resource usage within Spark applications.

Key Topics Covered:
Out of Memory Issues in Spark
Spark Executor Memory Structure
Tungsten Project Execution Engine
DataFrame Caching and Persistance
Broadcasting and Joins
Salting, Repartitioning, and Coalescing
1. Out of Memory Issues in Spark
Spark applications may face out-of-memory (OOM) errors either on the driver or executor side. Common causes include:

Broadcasting large DataFrames causing serialization stress on the driver.
Excessive accumulation of partitions.
Memory-intensive operations like collect or toPandas that bring large datasets to the driver.
Inefficient memory configuration, incorrect partition management, or caching unoptimized datasets【4:0†source】.
Managing Driver Out-of-Memory Errors
Avoid broadcasting disproportionate datasets.
Limit the number of partitions by following the guidance of fewer but larger partitions.
Ensure driver memory is correctly sized for the operations being performed【4:5†source】.
Addressing Executor Out-of-Memory Errors
Optimize memory allocation across Spark executors.
Use user-defined functions carefully, as they are memory intensive【4:1†source】.
2. Spark Executor Memory Structure
Spark's executor memory is divided into:

Reserved Memory: Similar to emergency reservations like "Tatkal" train tickets, primarily held aside for necessities.
User Memory: Reserved for custom user-defined functions (UDFs) and data structures.
Storage Memory: Used for caching DataFrames, defaulting around 30% of executor memory.
Execution Memory: Used for operations like shuffles, joins, sorts, etc.【4:10†source】.
Heap and Off-Heap Memory:

Heap Memory: Part of RAM used traditionally for Java object storage.
Off-Heap Memory: Suggested with the advent of the Tungsten engine, reducing pressure from garbage collection【4:11†source】【4:18†source】.
3. Tungsten Project Execution Engine
Tungsten is an optimizing engine within Spark that handles execution, especially with Whole Stage Code Generation (WSCG):

WSCG: Combines multiple operations during the same stage to avoid shuffling and promote efficiency in execution【4:4†source】.
Enhances performance by supporting off-heap memory and minimizing computational overhead after compilation【4:18†source】.
4. DataFrame Caching and Persistence
Caching and persist operations are important in reducing the repetitive computation of the same large datasets, effectively saving time and resources:

Cache: Stores data only in memory; offers increased speed but limited storage capability【4:6†source】.
Persist: Offers flexibility with multiple storage levels—memory, disk, and off-heap storage【4:6†source】.
Pros and Cons of Storage Levels:

Memory Only: Fastest but limits to smaller datasets.
Memory and Disk: Middle ground efficiently using memory, only spilling over to disk when necessary.
Disk Only and Off-Heap: Suitable for larger datasets where disk storage or off-heap options are preferred【4:15†source】【4:16†source】.
5. Broadcasting and Joins
The course promised to dig deeper into techniques for optimizing joins in future sessions, focusing on:

Removing shuffles where unnecessary.
Using broadcasting for small to medium-sized datasets, hence reducing move complexity.
6. Salting, Repartitioning, and Coalescing
Discussed as strategies to manage data distribution effectively:

Salting: Addresses skew in data allowing balanced processing loads.
Repartitioning and Coalescing: Change the number of partitions to optimize processing efficiency【4:13†source】.
Conclusion
Today's discussions aimed to provide insights into optimizing memory and computational efficiencies when managing Spark applications. With an understanding of Spark's internal memory framework, Tungsten execution strategies, and data management techniques like caching/persisting, learners can better handle complex data processing tasks. The subsequent classes will continue building out from this foundation into advanced strategies for managing data flows in Spark.

Out of Memory - Occurs in Spark when memory allocation exceeds available resources in driver or executors【4:5†transcript.txt】

Executor Memory - Divided into heap and off-heap memory in Spark for managing data storage and calculations【4:5†transcript.txt】

Tungsten Execution Engine - Optimizes Spark processes with whole-stage code generation and off-heap memory usage

Whole Stage Code Generation (WSCG) - A technique for optimizing the execution of queries in Spark by generating optimized bytecode

Catalyst Optimizer - Generates optimized logical and physical execution plans in Spark

Persist - Method to store RDDs on various storage levels such as memory, disk in Spark

Cache - Stores RDDs in memory for fast iterative processing in Spark

User Defined Function (UDF) - Custom functions to perform operations not natively supported by Spark's built-in functions

Broadcast Join - Optimizes joining a large dataset with a smaller dataset in Spark by distributing the smaller dataset to all worker nodes

Salting - Technique to manage skewed data distribution by introducing fake keys in partitioning

Repartition - Adjusts the number of partitions of an RDD to balance workload evenly across nodes

Coalesce - Reduces the number of partitions in an RDD, typically for narrowing transformations
////////////

No job will be created as we are not asking to infer schema(tell spaerk to identify schema as u don’t know)

<img width="274" height="107" alt="image" src="https://github.com/user-attachments/assets/f678a8b4-1b0f-4aab-941e-ba90e8a9270c" />

Run pyspark – to see spark jobs

<img width="452" height="49" alt="image" src="https://github.com/user-attachments/assets/c9b92641-fee9-4b03-8a9b-68df406c5e0e" />



As collect is an action so it should trigerred job
Withcolumn is narrow transformation,u don’t need to shufflre data
Join requires shuffle coz keys can be in 2 diff partition so first bring them in 1 partition to join them
Show()-trigger job
If we broadcast large df in driver it ill try to searilice and memory will go ,collect(),topandas() will agin serialize in driver

User defined function – when u do something which is not inbuilt in spark
Ex-adding column(done by UDF) in this case it uses user memory
Off heap memory is not a part of heap memory so GC doesn’t work on off heap memory so it is ur responsibility to remove it

We don’t shuffle data inside 1 stage, u create a stage if it requires shuffling
Wscg – tungsten engine takes stage 1 and generate wscg(byrte code-compiled code)

 and catalyst optimize – plan generation

<img width="451" height="450" alt="image" src="https://github.com/user-attachments/assets/c4eb26da-f19d-41d6-ab18-3cfda7108a89" />

