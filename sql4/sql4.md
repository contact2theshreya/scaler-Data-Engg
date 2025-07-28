<img width="486" height="266" alt="image" src="https://github.com/user-attachments/assets/ed439cf0-ee15-429d-9b58-1e79e528e465" />

Short circuiting using exist by checking if any id from any record of 2nd table matches we will not search in entire table and we will return directly true from there and we will then select record from first table

whereas in will compute all recored then return ans , if inner query has limited data then u can use subquery.

## Non equi join

<img width="444" height="299" alt="image" src="https://github.com/user-attachments/assets/da089841-a553-4938-a2fc-289066ed9699" />


<img width="319" height="226" alt="image" src="https://github.com/user-attachments/assets/be3ed44a-4514-4e0d-926c-6ca02cd1da69" />

Write a query to display the details of all those departments that don't have any working employees.

Result:

Return the columns 'department_id', and 'department_name'.
Return the results ordered by 'department_id' in ascending order.

<img width="435" height="393" alt="image" src="https://github.com/user-attachments/assets/f507b3fd-5150-4269-ae14-27de21a12fbb" />


STEP 1: Select department_id and department_name from the department’s table.

select d.department_id, d.department_name from departments d;

STEP 2: Using left join, join the tables departments and employees on department_id. (Left join because not all departments have working employees).

select d.department_id, d.department_name from departments d
left join employees e on d.department_id = e.department_id;

STEP 3: Use the ‘is null’ operator in the where clause to filter the records where there is no working employee.

select d.department_id, d.department_name 

## in normal subquery we store result of inner qury in memory but not in corelated subquery
from departments d 
left join employees e 
on d.department_id = e.department_id 
WHERE e.department_id is null
order by d.department_id;

<img width="470" height="50" alt="image" src="https://github.com/user-attachments/assets/8e595ecb-b3d5-4584-a173-d320774cef9d" />


 d1.department_name in ( 'Administration', 'Marketing', 'Human Resources');


<img width="1136" height="455" alt="image" src="https://github.com/user-attachments/assets/69f0af19-17ea-490a-ad3e-8513750d3e23" />

