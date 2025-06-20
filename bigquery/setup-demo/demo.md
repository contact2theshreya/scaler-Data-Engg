<img width="479" alt="image" src="https://github.com/user-attachments/assets/eed31b98-f0e7-4784-a409-df5bb33aa8b2" />

<img width="395" alt="image" src="https://github.com/user-attachments/assets/c6f148f8-33ab-4b30-b3f6-776710fee0a6" />

<img width="488" alt="image" src="https://github.com/user-attachments/assets/95bb9ed0-6484-4972-b67d-02bdffc6506b" />

<img width="477" alt="image" src="https://github.com/user-attachments/assets/b882a006-f2f2-4562-a2c7-d7c005a95b0c" />

<img width="483" alt="image" src="https://github.com/user-attachments/assets/4be77071-317e-4beb-a5dc-ddbf5e772bb4" />

round(col_value,2)

SELECT
       market_date,
       customer_id,
       vendor_id,
       quantity,
       cost_to_customer_per_qty,
       quantity * cost_to_customer_per_qty AS total_amount
  FROM farmers_market.customer_purchases
  LIMIT 10;
Here, total_amount is an alias for the calculated field .

 ## Questions
1)  Write a query to report the movies with an odd-numbered ID and a description that is not "boring".

Return the result table ordered by rating in descending order.

SELECT * FROM cinema WHERE MOD(id, 2) = 1  AND description != 'boring'
ORDER BY rating DESC;





