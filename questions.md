1)  Write SQL query that retrieves the customer ID and customer name from the customers table. It performs an inner join between the orders and customers tables based on the customer ID. The result set is grouped by customer ID and customer name. The groups are then filtered to include only those groups where the customers have purchased bread and milk but have not purchased eggs. The final result is ordered by customer ID in ascending order.

SELECT DISTINCT C.CUSTOMER_ID, C.CUSTOMER_NAME
FROM CUSTOMERS C
JOIN ORDERS O
ON C.CUSTOMER_ID = O.CUSTOMER_ID
GROUP BY C.CUSTOMER_ID, C.CUSTOMER_NAME
HAVING SUM(O.PRODUCT_NAME = 'BREAD') > 0
AND SUM(O.PRODUCT_NAME = 'MILK') > 0
AND SUM(O.PRODUCT_NAME = 'EGGS') = 0
ORDER BY CUSTOMER_NAME ASC;

2) <img width="324" height="290" alt="image" src="https://github.com/user-attachments/assets/c9627533-6660-4466-bc44-aa94bfb781e6" />

<img width="785" height="325" alt="image" src="https://github.com/user-attachments/assets/2fe4a6c4-36d0-4302-93ed-550df3383264" />

<img width="355" height="256" alt="image" src="https://github.com/user-attachments/assets/a84c3c63-b6dd-4450-8992-5eef98e4b9df" />


3) <img width="869" height="395" alt="image" src="https://github.com/user-attachments/assets/275a0d2b-0e8d-4cc7-a65b-b23c08f7a7eb" />


