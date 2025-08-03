with subquery ( u  run subquery and it iterate all row )for each row\\ - o(n^2)


with window function entire table is scanned once by storing result in some array -o(n) then main query is run

## comparision visualization

https://claude.ai/public/artifacts/5080b72c-71fb-4d76-9e38-54a34d9df855?fullscreen=true

https://claude.ai/public/artifacts/d91d267d-4242-428b-90e6-3046f43f539a?fullscreen=true

window function is executed after where clause

<img width="658" height="354" alt="image" src="https://github.com/user-attachments/assets/96819d05-0946-4a25-9f11-2fb7cfaab4f2" />

so this is not possible 

<img width="521" height="161" alt="image" src="https://github.com/user-attachments/assets/7125a361-de1d-4a5c-9a54-4985d95bbbae" />

over(),  over and partition, over and order by ,  or u can use all 3 together

over()  -scans entire tablke as 1 logical unit

## window frames

ca;culate cummulative of each frame(GROUPED BY DEPT)
ex - for 'A' unbounde prec-null,curr row -A
     for 'C' unbounde prec-B,curr row -C

AVG (SAL OF ROW c OF it DEPT)

<img width="657" height="410" alt="image" src="https://github.com/user-attachments/assets/bb52c767-f79d-4eb0-88ec-f34dbc3cf4b0" />

tHIS IS CUMMULATIVE sum as we also take unbounded oreceding in current riow calc

The PARTITION BY and ORDER BY clauses within the OVER() clause in SQL window functions define the scope and order of operations for the window function.
PARTITION BY:
The PARTITION BY clause divides the result set into independent groups, or "partitions," based on the specified column(s).
The window function is then applied to each of these partitions separately.
If PARTITION BY is omitted, the entire result set is treated as a single partition. 
For example, PARTITION BY DepartmentID would create separate partitions for each department, allowing you to calculate department-specific metrics like average salary within each department.
ORDER BY:
The ORDER BY clause defines the logical order of rows within each partition (or within the entire result set if no PARTITION BY is used).
This ordering is crucial for window functions that depend on the sequence of rows, such as ranking functions (e.g., ROW_NUMBER(), RANK()) or cumulative aggregations (e.g., SUM(...) OVER (ORDER BY ...)).
For example, ORDER BY Salary DESC within a department partition would order employees by salary in descending order, allowing you to find the highest-paid employee in each department. 
Example:
Code

SELECT
    EmployeeName,
    Department,
    Salary,
    RANK() OVER (PARTITION BY Department ORDER BY Salary DESC) AS DepartmentRank
FROM
    Employees;
In this example:
PARTITION BY Department divides the employees into groups by their department.
ORDER BY Salary DESC orders the employees within each department from highest to lowest salary.
RANK() then assigns a rank to each employee based on their salary within their respective department.

SUM(SalesAmount) OVER (...):
The SUM() window function then calculates the cumulative sum of SalesAmount within each Region partition, following the SaleDate order. The cumulative sum resets for each new region.

https://www.sqlshack.com/sql-partition-by-clause-overview/

