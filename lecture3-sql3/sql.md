Ambigious column 
two column with same name which is eventually get resolved with alias

Types of Joins

Inner Join: Combines rows from two tables where there is a match between the columns in both tables.

Left Join (Left Outer Join): Returns all rows from the left table and matched rows from the right table. Unmatched rows in the right table result in NULLs【4:3†source】【4:5†source】.

Right Join (Right Outer Join): Opposite of Left Join, but not commonly used in production as left join can achieve the same results by switching the table positions【4:18†source】.

Full Join (Full Outer Join): Returns all records when there is a match in either left or right table records. MySQL does not support FULL OUTER JOIN directly【4:11†source】.

Self Join: A self join is a regular join but the table is joined with itself. It is often used to query hierarchical data【4:13†source】.
## example query

SELECT 
    employee_id,
    first_name,
    last_name,
    salary,
    CASE 
        WHEN job_id IN ('FI_ACCOUNT', 'AC_ACCOUNT') THEN 1
        ELSE 0
    END AS Accountant
FROM 
    employees
ORDER BY 
    employee_id ASC;

    /////////////////
    
    select employee_id,first_name,last_name,job_id
from employees E1
join departments D1
on E1.department_id=D1.department_id
join locations L1
on D1.location_id=L1.location_id
where L1.city='Seattle';

///////////////////////////

select
    employee_id,
    salary,
    case
        when salary > 2e4 then 'Class A'
        when salary < 1e4 then 'Class C'
        else 'Class B'
    end as 'Salary_bin'
from employees
order by 1;
