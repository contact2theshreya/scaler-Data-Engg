/home/--client
/user/-- - data node

Fair scheduler - give equal core resource to each job 

<img width="709" height="409" alt="image" src="https://github.com/user-attachments/assets/07382af0-6b75-4121-8c2d-b4ac54ce938e" />

Application master is per job

## MaP Reduce

Data processing for large cluster

<img width="557" height="478" alt="image" src="https://github.com/user-attachments/assets/0e77c2a6-4d9b-4d3f-a254-3b65f2b557c1" />

<img width="297" height="181" alt="image" src="https://github.com/user-attachments/assets/22f81b3f-ef7a-4ba8-9f58-dcf0551219e0" />

Run the code for mapper reducer with the input dataset


MapReduce
Understanding MapReduce
Purpose: A framework for processing large datasets in parallel and distributed environments. It breaks down processing into map tasks and reduce tasks【4:3†source】【4:14†source】.

Process:

Map Phase: The input data is divided into several parts which map tasks transform into intermediate key-value pairs.

Shuffle and Sort: Intermediate data is shuffled and sorted to be processed by the reduce phase.
Reduce Phase: Reduce tasks aggregate and process the intermediate data to produce the final output【4:16†source】.

Analogy for Understanding MapReduce

Election Counting Example:

Map: Tellers segregate votes into categories based on party, akin to how mapping organizes data into key-value pairs【4:14†source】.

Reduce: Tellers count the votes they were responsible for, which is similar to reducing aggregated mapped data sets【4:17†source】.

Use Cases of MapReduce

Ideal for tasks that involve batch processing of large amounts of data.

Successfully employed in situations where operations such as data filtering, aggregation, and summarization are required【4:16†source】.
