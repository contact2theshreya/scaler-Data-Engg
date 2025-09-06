Revision Notes for MapReduce in Hadoop
Introduction
MapReduce is a programming model used for processing large data sets with a distributed algorithm on a cluster. It is a core component of the Hadoop framework. In our class, we discussed several aspects of MapReduce, including its phases, logic, and analogy to real-world processes.

MapReduce Phases
The MapReduce process consists of several key phases:

Map Phase: The 'map' function processes input key-value pairs to generate a set of intermediate key-value pairs.

Shuffle and Sort Phase: The system performs shuffle and sort operations on the output of the map task.

Partition Phase: The partition logic is responsible for directing the output key-value pairs to a particular reducer.

Reduce Phase: The 'reduce' function processes the list of intermediate key-value pairs to produce a set of output values.

Developer Responsibility
The developer's responsibility in MapReduce is primarily with the map and reduce functions. The partition, shuffle, and sort phases are managed by the framework itself .

Detailed MapReduce Workflow
Here’s how the MapReduce workflow was described in the class:

Input: The client submits a job to YARN, which calls the MapReduce API. The input data is split based on the HDFS (Hadoop Distributed File System) block size. For example, a 256MB file is split into two 128MB blocks for processing【4:5†transcript.txt】.

Assignment: The Resource Manager assigns the job to an Application Master, which then coordinates resource allocation【4:5†transcript.txt】.

Containers & Execution: Containers are set up on Data Nodes, and Map tasks are initiated on these nodes. The Python code necessary for processing is moved to the data location for execution【4:9†transcript.txt】.

Mapper Execution: The map tasks read the input data and produce intermediate key-value pairs, typically representing the data to process【4:10†transcript.txt】.

Shuffle and Sort: Intermediate data from the map tasks are shuffled and sorted. The sorted data is prepared for the reduce phase【4:12†transcript.txt】.

Reducer Execution: The reduce tasks process the sorted key-value pairs to generate the final output. The number of reducers affects the number of output files【4:12†transcript.txt】【4:19†transcript.txt】.

Output: The final result is written to HDFS, and resources can be reclaimed post-processing【4:18†transcript.txt】.

Analogies Discussed
The MapReduce process was likened to a tiger eating its food, where the tiger represents the processing engine and the food represents the data【4:11†transcript.txt】.
An election commission analogy was used to describe how data is processed. Different keys (political parties) have different values (votes), analogous to records in a MapReduce job【4:16†transcript.txt】.
