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

## window function

PARTITION BY: This optional clause divides the result set into partitions or groups, and the ranking is applied within each partition separately. If omitted, the entire result set is treated as a single partition.

First day of job

In SQL, the FIRST_VALUE() function is a window function used to retrieve the first value in an ordered set of values within a defined window or partition.

select distinct emp.first_name,
first_value(jhist.start_date) over(partition by jhist.employee_id 
order by jhist.start_date) as 'first_day_job'
from job_history jhist 
join employees emp 
on jhist.employee_id = emp.employee_id
order by emp.first_name;

or

select e.first_name, t.start_date as first_day_job from
(select employee_id, start_date,
dense_rank() over(partition by employee_id order by start_date) as job_num
from job_history) t, employees e
where e.employee_id = t.employee_id
and t.job_num = 1
order by e.first_name asc

atlweast 28Years = 
 DATEDIFF('2022-06-08', hire_date)/365 >= 28

<img width="674" height="306" alt="image" src="https://github.com/user-attachments/assets/8b097a01-aedb-47b5-b12e-14b1ce34f55c" />


<img width="744" height="406" alt="image" src="https://github.com/user-attachments/assets/6ba7ba95-a555-44bb-ad86-5f6055edf067" />


<img width="672" height="319" alt="image" src="https://github.com/user-attachments/assets/3d637498-8111-4984-a9fc-78e313426b5e" />


 select id, visit_date, people
from
(select id, visit_date, people, 
lead(people) over (order by id asc) as next1,
lead(people,2) over (order by id asc) as next2,
lag(people)over (order by id asc) as prev1,
lag(people,2)over (order by id asc) as prev2
from mall
)as mall_ppl
where (people >= 100 and next1 >= 100 and next2 >= 100) or 
(people >= 100 and prev1 >= 100 and prev2 >= 100) or
(people >= 100 and prev1 >= 100 and next1 >= 100)
order by visit_date;

SELECT id, visit_date, people:
– This line specifies the columns that will be selected and returned in the result set.
– The query will retrieve the id, visit_date, and people columns.

FROM (SELECT ... ) as mall_ppl:
– This line introduces a subquery that selects specific columns from the mall table and assigns them aliases.
– The subquery is given the alias mall_ppl.

SELECT id, visit_date, people, lead(people) over (order by id asc) as next1, lead(people,2) over (order by id asc) as next2, lag(people) over (order by id asc) as prev1, lag(people,2) over (order by id asc) as prev2 from mall:
– This subquery selects the id, visit_date, and people columns from the mall table.
– Additionally, it uses window functions to calculate the values for the next two rows and the previous two rows.
– lead(people) retrieves the value of people in the next row, while lead(people,2) retrieves the value of people in two rows ahead.
– lag(people) retrieves the value of people in the previous row, while lag(people,2) retrieves the value of people two rows behind.
– These calculated values are aliased as next1, next2, prev1, and prev2, respectively.

WHERE (people >= 100 and next1 >= 100 and next2 >= 100) or (people >= 100 and prev1 >= 100 and prev2 >= 100) or (people >= 100 and prev1 >= 100 and next1 >= 100):
– This line specifies the conditions for filtering the result set.
– It selects rows where people is greater than or equal to 100 and meets one of the following conditions:
(1) next1, next2, and people in consecutive rows are all greater than or equal to 100, (2) prev1, prev2,
and people in consecutive rows are all greater than or equal to 100, or (3) prev1, next1,
and people in consecutive rows are all greater than or equal to 100.

ORDER BY visit_date:
– This line specifies the order in which the final result set should be sorted.
– It will sort the result set by the visit_date column in ascending order.

<img width="871" height="283" alt="image" src="https://github.com/user-attachments/assets/a253c126-f5a9-4a15-8910-7d7923e70191" />

<img width="890" height="289" alt="image" src="https://github.com/user-attachments/assets/7218821f-9cf4-43cc-ba50-6674a32c416e" />

<img width="953" height="356" alt="image" src="https://github.com/user-attachments/assets/50836c5c-4fad-411d-ad25-a4a37ebc8237" />

<img width="676" height="115" alt="image" src="https://github.com/user-attachments/assets/defda99c-57f4-44eb-bfd3-423f5fdbff95" />

: Memory leaks can cause a Node Manager to use more resources than it should, even when it is not
running any containers. It is important to identify and fix memory leaks as soon as possible to prevent performance’
issues and resource contention in the cluster.

<img width="1094" height="434" alt="image" src="https://github.com/user-attachments/assets/2c0895b5-1518-4ac7-8449-4cc407138561" />

<img width="1158" height="548" alt="image" src="https://github.com/user-attachments/assets/ac32f8fa-8372-47fe-bf09-638d5cabc5d2" />

<img width="1146" height="676" alt="image" src="https://github.com/user-attachments/assets/e8f19a4b-b0ed-4aa0-a322-5f4e4e010225" />

<img width="1146" height="554" alt="image" src="https://github.com/user-attachments/assets/078501af-ad98-40e0-8ed6-5cc2ce8e8fbc" />

<img width="1168" height="503" alt="image" src="https://github.com/user-attachments/assets/4124c449-1f69-4ce6-ad02-7c50bac8f49f" />

