<img width="1111" height="346" alt="image" src="https://github.com/user-attachments/assets/e42c98d6-9271-4808-af48-0c597f18f9e9" />

A data warehouse is optimized for reporting and analysis, while a database is optimized for transaction processing

Your manager asked you for insights on the data that is stored in the Hive table. You’ll need to fire SQL Query to get insights from the data. What happens to a SQL query when it is run in Hive?

It is converted into a java class file and executed as a MapReduce job

Facts are numerical, while dimensions are categorical
Facts are the measurements/metrics or facts from your business process. Dimension provides the context surrounding a business process event. In simple terms, they give “Who, What, Where” of a fact.

We know that Dimensions are categorical but here “Name Of the product”, “Name of the customer”, “Date of sale” all of these values
is categorical but Dimension is with context to “Facts”.

Here Fact is Sales so dimension is Date of Sale

<img width="838" height="260" alt="image" src="https://github.com/user-attachments/assets/d962b789-6bd6-4d2a-a1a0-9e7bee2345c2" />


Fact table:Dimension table is 1:M

You are working at an E-commerce company as a Data Engineer. In the Company’s Data Warehouse, you are storing information about Shipments. A shipment's delivery status changes. What type of Slowly Changing Dimension (SCD) is this scenario?

Correct Answer: SCD Type 2
Type 2 - Creating a new additional record
when you order something online, you can track your delivery of your order. You can clearly see the status of your delivery changes. It’s not overwritten. Previous status also get stored in the database and always new record gets created.
