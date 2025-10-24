Spark streaming connect to netcap server through socket cojnectiona nd for every 1 sec duration we created microbatch then we process microbatch and wrote the output to console

Many consumer can read from one partition coz of sepearet offset 
To increase throughput we increase number of partition
U can also send msg to topic with key and hash (key) will then decide to call which partition (if u want to make partition user specific just like stateful server)

Inc consumer group consumer can be of same application but diff instance ex diff k8s pod
<img width="468" height="251" alt="image" src="https://github.com/user-attachments/assets/1b03373d-e793-4050-9529-3cd29b473981" />

<img width="452" height="35" alt="image" src="https://github.com/user-attachments/assets/b25ff519-77cb-43b0-8519-7812b08ee409" />

<img width="452" height="49" alt="image" src="https://github.com/user-attachments/assets/f523a2df-c8c7-4a8b-bdcf-af9f5b3df706" />

See zip file of this project<img width="468" height="50" alt="image" src="https://github.com/user-attachments/assets/8bf86d77-c643-4f06-bf4d-5bcb0044233e" />

<img width="452" height="246" alt="image" src="https://github.com/user-attachments/assets/ca9dd695-6722-48cf-850b-5104fa583486" />

<img width="452" height="149" alt="image" src="https://github.com/user-attachments/assets/58c31d96-9ea1-496d-80c0-0e42d50e69fb" />

<img width="452" height="192" alt="image" src="https://github.com/user-attachments/assets/cf0ebe9b-d0f9-4af9-8c02-1567d865ca75" />



Spark streaming is also up
Now open Grafana from docker port
<img width="468" height="100" alt="image" src="https://github.com/user-attachments/assets/430a4537-876d-4c4c-9cae-7e523b5e3a13" />

<img width="452" height="200" alt="image" src="https://github.com/user-attachments/assets/e2bca68c-82f9-48b8-af49-7880bbb9cbd0" />


Airflow component demo
<img width="468" height="75" alt="image" src="https://github.com/user-attachments/assets/491bc23c-d4e5-47c7-ab20-bdcc5350822a" />

<img width="452" height="202" alt="image" src="https://github.com/user-attachments/assets/e3d9dbbe-b80d-4755-99bd-f69990ce0bd2" />

Allare done by airflow-new job is triggeregd once old job is succeded<img width="468" height="50" alt="image" src="https://github.com/user-attachments/assets/ef5c25ec-96a3-4500-b8b7-e8422d949661" />


<img width="452" height="196" alt="image" src="https://github.com/user-attachments/assets/850f18b0-18d4-4666-b251-97a0c70eb72f" />

Fetch data->clean data and fetch data from orther source->run AI logic->make dashboard
Cycle is nit valid dag
Executor triggers task ex k8s is ececutor for airflow
<img width="468" height="100" alt="image" src="https://github.com/user-attachments/assets/041a9b09-d201-4c30-822e-8e5925aadf86" />

<img width="452" height="181" alt="image" src="https://github.com/user-attachments/assets/be4fdced-9b61-4bc1-8654-f3f88fbce6a7" />


Scheduler update dag data in metadata db and exectors and worker(nodes) runs based on metadata for running jobs
In dag files u define dag
<img width="468" height="117" alt="image" src="https://github.com/user-attachments/assets/c1f3a326-1fda-4085-acf3-5fbbc5c1afd3" />

<img width="452" height="146" alt="image" src="https://github.com/user-attachments/assets/bc5f13c7-ac3e-4835-9050-da3b09c39f40" />

Both consumer group will execute , but 3 will be idle<img width="468" height="50" alt="image" src="https://github.com/user-attachments/assets/24c20f94-a747-4502-8c94-d8f69f409aa1" />

////////////////
Agenda Overview
Kafka and Consumer Groups

Introduction to Kafka Consumer Groups and their architecture.
Demo using Kafka with a real-world application involving Binance API for cryptocurrency pricing.
Docker Usage

Setting up Docker for application environments.
Running Kafka and related services in Docker containers.
Airflow Introduction and Components

Understanding Airflow for orchestrating workflows.
Airflow's components: DAGs, schedulers, executors, etc.
Demo of Airflow

A practical demonstration of setting up and using Airflow.
Detailed Concepts
1. Kafka Overview
Kafka Architecture

It acts as a distributed messaging system, enabling real-time data feeds.
Involves Producers, Kafka Servers (Brokers), Topics, Partitions, and Consumer Groups【6:4†source】.
Producers and Consumers

Producers publish data to topics.
Consumer Groups allow multiple consumers to read partitions of a topic, enhancing parallel data processing【6:4†source】【6:12†source】.
Partitioning in Kafka

Kafka topics can be divided into multiple partitions to increase throughput.
Example analogy: Roads with multiple lanes allow more vehicles and faster travel compared to single-lane roads【6:16†source】【6:4†source】.
2. Kafka Demo
Real-time Data with Binance API

Fetches cryptocurrency price data like Bitcoin, Ethereum, etc., using Binance API【6:0†source】【6:17†source】.
Data published to Kafka, facilitating asynchronous processing【6:13†source】.
Spark Streaming

Acts as a consumer, processing data by transforming it (changing data types, adding timestamps) and storing it in InfluxDB, which is optimized for time series data【6:0†source】【6:14†source】.
Grafana for Visualization

Generates real-time visual charts using data stored in InfluxDB【6:0†source】.
3. Introduction to Docker
Docker enables easy configuration and deployment of applications by using Docker Compose files to manage multiple containers for tools like Kafka, Zookeeper, Spark, etc.【6:8†source】【6:10†source】.
4. Introduction to Airflow
Airflow Components

DAGs (Directed Acyclic Graphs) represent tasks and their dependencies, heart of workflow in Airflow【6:11†source】【6:7†source】.
Scheduler: Determines when workflows are executed.
Worker Nodes: Execute the tasks defined in the DAG.
Metadata Database: Stores metadata about tasks【6:9†source】.
Airflow Features & Use Cases

Designed for orchestrating complex workflows and developed by Airbnb.
Open-source and scalable, primarily for batch-oriented jobs【6:11†source】.
5. Airflow Demo
Set up and execute workflows defined in DAGs using Airflow.
Showcase interaction via GUI and Python scripting【6:7†source】【6:11†source】.
Conclusion and Practical Tips
Kafka is vital for real-time data streaming and asynchronicity in data processing.
Docker simplifies application setup across various environments.
Airflow is instrumental in managing dependencies and scheduling tasks in complex workflows.
Practical understanding and setup through demos solidify learning.
/////////////
spark streraming - A component of Apache Spark for processing live data streams
Influx db - A time series database optimized for fast, high-availability storage and retrieval

Grafana - A tool for creating dashboards and visualizing time series data
￼
Scheduler - In Airflow, it determines when DAGs should start

Executor - Executes tasks in Airflow, e.g., Celery or Kubernetes

Partitions - Units of parallelism in Kafka; a topic may have multiple partitions
