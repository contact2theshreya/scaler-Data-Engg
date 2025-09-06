<img width="888" height="545" alt="image" src="https://github.com/user-attachments/assets/5842efc1-bef5-4808-b71f-cbcbc81f4d9f" />

256 MB is divided in two nodes of 128MB each
and no of reducer configured is 1 that means we want output in single file


Clienr=t will talk to HDF internally to get the name node information about file and client will only give file metadata to resource manager like location of file etc

miving our poythin code to the machine that contains data

mapper parsed data into key value pair and if no of reducer configured is 1 then in each data node partition file will be 1 and hash(key)%no of reducer will go in that partition file 
