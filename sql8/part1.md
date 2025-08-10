Insertion in row based is faster than columnar coz in row based u need only one insertion in row whereas in columnar if u have 4 col that means u need to insert 4 times for a single record

for running aggregation exx how many people live in 22801 u just need to count 22801 in zip column so it is faster than row based whre we have to iterate each row 

compression has higher efficiency in columnar as we can compress more in columnar coz they have same data type of each column so we can compress easily 

big data uses columnar

we will store 1 year dat6a in OLTP and we move it timely to OLAP

partiotioning is diving data into other machines to make search faster

ingestion partition - data doesn't have timestamp example sensor data so u partition from the time u inserted in table ex u inserted sensor data in June 2025
