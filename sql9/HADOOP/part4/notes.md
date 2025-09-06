<img width="888" height="545" alt="image" src="https://github.com/user-attachments/assets/5842efc1-bef5-4808-b71f-cbcbc81f4d9f" />

256 MB is divided in two nodes of 128MB each
and no of reducer configured is 1 that means we want output in single file


Clienr=t will talk to HDF internally to get the name node information about file and client will only give file metadata to resource manager like location of file etc

miving our poythin code to the machine that contains data

mapper parsed data into key value pair and if no of reducer configured is 1 then in each data node partition file will be 1 (for each mapper)and hash(key)%no of reducer will go in that partition file

parallel process  - pick partion 1 from all mapper and process it parallely and save its output in file 1,similarly pick partition 2 from all mapper and process it parallely and save in file 2 

Mapper.py

<img width="910" height="526" alt="image" src="https://github.com/user-attachments/assets/af0c619d-d766-430e-9bf0-327e2972b1f2" />

If u run map command with 0 reducer then u get intermediary output of mapper in some output file

<img width="581" height="375" alt="image" src="https://github.com/user-attachments/assets/1fabde60-a885-4eb2-adb5-863c79fc0a07" />

<img width="685" height="272" alt="image" src="https://github.com/user-attachments/assets/12a62ffa-3525-46b3-b6d3-06f038f6ed55" />

mapred streaming \ -D mapreduce.job.reduces=0 \ -D mapreduce.job.maps=2 \ -input /user/userjuly2025019/logAnalyser/*.log \ -output /user/userjuly2025019/output_zero_reducer/ \ -mapper mapper.py \ -reducer reducer.py \ -file /home/userjuly2025019/mapper.py \ -file /home/userjuly2025019/reducer.py

Map Reduce With 1 Reducer - Command

mapred streaming \ -D mapreduce.job.reduces=1 \ -D mapreduce.job.maps=2 \ -D mapreduce.job.maps=2 \ -input /user/userjuly2025019/logAnalyser/*.log \ -output /user/userjuly2025019/output_one_reducer/ \ -mapper mapper.py \ -reducer reducer.py \ -file /home/userjuly2025019/mapper.py \ -file /home/userjuly2025019/reducer.py

Shuffle - take key,value pair combinen them in sorted order using merge sort

<img width="579" height="432" alt="image" src="https://github.com/user-attachments/assets/00dfc02d-79b8-4963-82f0-f985763e7f7d" />

<img width="292" height="157" alt="image" src="https://github.com/user-attachments/assets/0cfd3392-f765-4a66-bfd1-45fed03a1512" />

<img width="205" height="325" alt="image" src="https://github.com/user-attachments/assets/02e6e680-da7d-4e0d-afe5-43104eacddc3" />


## Reducer.py - combine count of each keyas they are in sorted ordert by key so iterate them one by one

<img width="761" height="435" alt="image" src="https://github.com/user-attachments/assets/0b400d59-bb36-49f8-a5c2-e938373e3057" />

No wrun with reducer logic instedad of cat

<img width="289" height="172" alt="image" src="https://github.com/user-attachments/assets/c8b7299f-b43a-49d0-91e1-3020575c5b40" />

<img width="265" height="275" alt="image" src="https://github.com/user-attachments/assets/bb6cc62f-1aaf-46e9-86e0-41ebc3843bab" />

Container
Containers are slots which contain RAM, CPU, and the execution engine for logic processing【4:0†source】.

Name node
A component in HDFS which maintains metadata and directs data block placements

Datanode
Nodes where actual data is stored in HDFS, organized into blocks

Mapreduce
Nodes where actual data is stored in HDFS, organized into blocks

Yarn
Nodes where actual data is stored in HDFS, organized into blocks

HDFS
Hadoop Distributed File System, used for storing large data sets across multiple nodes

Maop task
The initial processing task that takes input, parses it into records, and produces a set of intermediate key/value pairs

Reduce task
Aggregates intermediate data from Map Tasks, sorts and combines it into final results【

Shuffle and sort
Processes that occur between Map and Reduce phases where output from Mappers are sorted and transferred to Reducers

File input split
A way Hadoop divides input files into manageable pieces for individual map tasks



