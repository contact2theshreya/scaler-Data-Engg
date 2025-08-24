store data in more than 1 machine,spark and storm is more efficient than map reduce

Name node and data node can be present in more than 1 machine with config file that where and how it has to communicate
with nodes from diff machine


Client will first connect to name node and will send file then name node will connect to data node and then client will connect to data node and will write the chunks data to data node
as soon as 1 block is written in data node , it will send ack to name node to store the metadata

Name node gives data node info to client and client readsd data from data node

Data node send heartbeat to name node to indicate he is alive

LIST the files - hdfs dfs -ls /usr/

<img width="586" height="57" alt="image" src="https://github.com/user-attachments/assets/9b5cb682-0c4a-404e-8d25-74a075b24f16" />

Yarn provides machine to process data

Yarn consist of resource manager, scheduler and application manager

List of files ,Create a directory is name node operation

 Write data ,copy data is data  and name node  opeartion
 
Read data is data node operation

Cut paste/move data is name node operation(it doesn’t move actual data, it only moves file structure tcure)

In copy data we also move data to diff dat node/block
