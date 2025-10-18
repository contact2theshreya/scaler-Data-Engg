Fraction cache – cache only some partition
Cache is always inmemory if u want to store it on disk then persiste(storage level=disk)
Memory – RAM
Heap and off heap will be in ram
Unpersist – clean up memory
If DF is being read two times then it gets cached
Once u write after aggregation then DAG completes
Executor is nothing but partition

Spark creates 200 partition by default
Before join do shuffling between partition to bring id in same partition
For less datat it usus some partition and rest of them will be empty
1 partition gets 1 core for execution

If u do broadcasting-then in all partition they will have same datat then u an avoid shuffling during join and partition wilol not be 200

Before writing to file apply collesce that is writing to file the partition which has data

/////////




![Uploading image.png…]()




Introduction
Welcome to today's session! In this class, we discussed partition management in Apache Spark, focusing on operations like coalesce, repartition, caching strategies, broadcasting in join operations, and practical optimizations.【6:0†transcript.txt】

Key Concepts
Coalesce and Repartition
Coalesce:

Purpose: Used to reduce the number of partitions in a DataFrame. It is beneficial when you have a DataFrame with many partitions but few of them have data.
Application: Applying coalesce optimizes resource usage by minimizing the number of executor cores needed.
Example: If you initially have 200 partitions but only 10 have data, using coalesce(10) reduces overhead by only allocating resources to partitions with data【6:1†transcript.txt】.
Repartition:

Purpose: Increases the number of partitions, often used to improve parallelism by distributing data more evenly across partitions.
When to Use: Helpful when a partition holds a large amount of data which could cause processing bottlenecks【6:3†transcript.txt】.
Methods: You can either specify the number of partitions or repartition by a specific column, distributing data based on that column's values【6:16†transcript.txt】.
Caching and Unpersisting
Caching:

Use Case: Cache data in memory when you reuse the same DataFrame multiple times. It's effective for improving performance and reducing computation time【6:5†transcript.txt】.
Unpersist:

Purpose: Clears cached data from memory when it's no longer needed, optimizing memory usage【6:7†transcript.txt】.
Broadcast Joins
Broadcasting:
Purpose: Useful for joining a large DataFrame with a much smaller DataFrame to prevent data shuffling.
Process: The small DataFrame is copied to each node, allowing Spark to perform join operations locally on each partition【6:17†transcript.txt】.
Considerations: Ensure the smaller DataFrame fits into the memory of each executor to prevent out-of-memory errors【6:12†transcript.txt】.
Practical Considerations
Data Skewness:

Partitions might be unevenly distributed, causing certain tasks to be slower than others. Techniques like broadcasting can mitigate these effects【6:5†transcript.txt】.
Memory Management:

Be cautious of the memory used for each partition and ensure proper configuration to handle various data sizes and workloads【6:10†transcript.txt】.
Conclusion and Homework
This class delved into efficient data partitioning techniques using coalesce, repartition, and broadcast joins.
Homework: Explore the impact of repartitioning by fixing partition IDs and observe if it reduces shuffles during joins【6:16†transcript.txt】.



Partition - A division of data in Spark used to distribute processing across nodes.

Repartition - Used to increase the number of partitions for better workload distribution.

Coalesce - Reduces the number of partitions in data to save resources and improve efficiency.

Adaptive Query Execution (AQE) - An optimization technique in Spark that dynamically adjusts query plans.

Broadcast Join - A Spark join where a small table is broadcast to all nodes to avoid shuffling.

Sort-Merge Join - A join in Spark where data is sorted and merged, commonly used for large datasets.

Shuffle - A process in Spark where data is redistributed across partitions, often leading to performance hits.

Executor - A node in Spark that runs computations on partitioned data in a distributed fashion.

Heap memory - Refers to the runtime memory allocated to Spark jobs for object storage.

Salting - A technique in Spark to prevent skew in data by adding a random value to keys during data partitioning.

Spark SQL Shuffle Partitions - A configuration setting determining the number of partitions after a shuffle operation.
