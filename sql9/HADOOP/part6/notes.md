https://docs.google.com/document/d/18AjThKOmNqz2BZAgdnnXOpph6jlp0HEhw8zkORwXzeU/edit?tab=t.0#heading=h.upb400ham5gj

In hive architecture powerbi,tabeleu,python script acn be a client and read req goes to hive server and data comes to client

Example there is a beeline client  and command to connect through beeline client is

<img width="843" height="335" alt="image" src="https://github.com/user-attachments/assets/a21a6c5d-08e7-4b27-8188-6aa04a0442ef" />

1 single sql in hive consist of 4 steps

suppose u ran query to list product in sql

<img width="832" height="384" alt="image" src="https://github.com/user-attachments/assets/f752e20a-8f26-4c19-aee7-f85f009664b6" />

Now run query-explain extended <sql_query> to check what are the steps involved

<img width="683" height="338" alt="image" src="https://github.com/user-attachments/assets/36147d91-9749-4146-a7d4-c44d5fc00683" />

Data will be in HDFS and we are mapping data from HDFS to hive table to run qyery in hive

<img width="615" height="344" alt="image" src="https://github.com/user-attachments/assets/2f9f80c2-9284-4885-8992-1d58e8a41e7e" />

craete db using hive

<img width="507" height="33" alt="image" src="https://github.com/user-attachments/assets/8d95e9be-37e5-4cdd-8c34-3855258e712f" />


It goes to HDFS and inside hive the DB will be created
<img width="801" height="436" alt="image" src="https://github.com/user-attachments/assets/4ab07f7e-a884-40f5-a34b-ec81fecf21fa" />

Move hivedataset  from client to hdfs

<img width="486" height="48" alt="image" src="https://github.com/user-attachments/assets/dbbdba9d-b5b8-40d2-bf1d-5e80dedd7e90" />

We are trying to implement start schema in hive
Now create table inside Hive editor(in same folder query is ther)


<img width="644" height="358" alt="image" src="https://github.com/user-attachments/assets/cace1080-1f4b-463d-96e6-78073707792a" />

External table()u ownd ata but metadata is own by hive takes carew of 

<img width="465" height="54" alt="image" src="https://github.com/user-attachments/assets/346e8bbe-037f-4c73-9265-bd48c835ac7b" />

<img width="611" height="137" alt="image" src="https://github.com/user-attachments/assets/0deb2549-cad1-455e-a45d-2ebb4e141eb6" />

Load dtata in managed table from hdfs  whre Hive is owner, u don't give location of data

<img width="585" height="178" alt="image" src="https://github.com/user-attachments/assets/bea0d3a6-669a-4437-892a-e5a55370f9bb" />

<img width="289" height="131" alt="image" src="https://github.com/user-attachments/assets/75169a66-2197-4791-bc6f-33366d2c5f7b" />


In external table data will not move to hive unlike manage table where we load explicitly to external table

<img width="1168" height="755" alt="image" src="https://github.com/user-attachments/assets/7063f2f2-c4c4-4b68-b083-fa36e1de86ad" />

HIVE  -is on top which runs all below stage
----
MAp reduice
-----
YARN
--------
HDFS

File format example used in HDFS - Apache parquet wher u store data in columnar storage so compression would be easy then ex ion below u can compressed to <electronice,4> as 4 times electronics came 

parque also gives serialization and deserialization

Norte - we have implemented sstar schema using hive coz fact_sale table has FK of all dimesion table 

Bits/bytes can be accesed by computer faster
