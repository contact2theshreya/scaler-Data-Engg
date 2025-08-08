https://docs.google.com/document/d/1Yd3gnfnRx97hDCHeiXY1dzIVkNKwEX39DzZdf-xvRiI/edit?tab=t.0

# CTE -common table expression
function in programming language -compilation is fast and execution is same coz no need to generate byte code again and again
similar to function in programming language we have CTE in sql(reuse sql query ,parsed once and execute again and again)

<img width="1119" height="545" alt="image" src="https://github.com/user-attachments/assets/7e81d1a2-39cc-4a1f-bd46-1ee99bc305b1" />

Here avg_total_purchase is one CTE and this is being used in another CTE greater_than_avg so we have written multiple CTE seprated by comma and in final query we have used
greater_than_avg.

## Views

if u want to reuse the query ,in case of CTE u can only use CTE only in 1 query

<img width="1504" height="792" alt="image" src="https://github.com/user-attachments/assets/2b7a1008-bfee-4cdb-a4b1-8d1beb5ff84e" />

CTE only improves compilation time but not performance
view is across session and it is db scoped

In SQL, both **views** and **CTEs (Common Table Expressions)** are used to simplify complex queries and improve readability, but they serve different purposes and have different characteristics. Here's a comparison:

### **1. View**

* **Definition**: A view is essentially a stored query that you can treat like a table. It doesn't store data itself but presents data from one or more underlying tables based on a predefined query.

* **Persistence**: Once created, a view is persistent. It exists in the database schema and can be reused in multiple queries.

* **Usage**: A view is used to encapsulate complex queries, especially when you need to join tables, apply filters, or aggregate data frequently.

* **Performance**: Views can sometimes lead to performance issues if they are based on very complex queries or large datasets. However, because the underlying query is executed every time the view is referenced, there's no storage overhead for the view itself.

* **Syntax**:

  ```sql
  CREATE VIEW view_name AS
  SELECT column1, column2
  FROM table_name
  WHERE condition;
  ```

* **Example**:

  ```sql
  CREATE VIEW active_users AS
  SELECT id, name, email
  FROM users
  WHERE status = 'active';
  ```

  You can then query the view like a table:

  ```sql
  SELECT * FROM active_users;
  ```

### **2. CTE (Common Table Expression)**

* **Definition**: A CTE is a temporary result set that is defined within the execution scope of a `SELECT`, `INSERT`, `UPDATE`, or `DELETE` statement. It is like a temporary view that only exists for the duration of the query it’s part of.

* **Persistence**: A CTE is **not persistent**. It only exists for the duration of a single query and is not stored in the database.

* **Usage**: CTEs are often used for simplifying complex queries, especially when you have subqueries or recursive queries. They make code easier to read and maintain.

* **Performance**: Since CTEs are only temporary and evaluated during the execution of a query, they generally have no performance overhead, but they can be recomputed multiple times within the query. Using `WITH` statements (CTEs) makes complex joins or hierarchical queries more efficient.

* **Syntax**:

  ```sql
  WITH cte_name AS (
      SELECT column1, column2
      FROM table_name
      WHERE condition
  )
  SELECT * FROM cte_name;
  ```

* **Example**:

  ```sql
  WITH active_users AS (
      SELECT id, name, email
      FROM users
      WHERE status = 'active'
  )
  SELECT * FROM active_users;
  ```

### **Key Differences**:

| Feature          | View                                                                                    | CTE                                                                                           |
| ---------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- |
| **Persistence**  | Persistent, stored in database schema                                                   | Temporary, valid only within the query execution                                              |
| **Scope**        | Can be reused across queries                                                            | Valid only within the query it's defined in                                                   |
| **Performance**  | Can sometimes have overhead (depends on complexity)                                     | Doesn't store anything permanently, recalculated every time                                   |
| **Use Case**     | Frequently used for abstracting complex queries across multiple queries or applications | Simplifying complex queries or breaking down logical steps for readability in one-off queries |
| **Modification** | You can't update data in a view directly unless it's a **simple view** (no joins, etc.) | Can be part of a query that modifies data (INSERT, UPDATE, DELETE)                            |
| **Recursive**    | Not recursive                                                                           | Can be recursive (for hierarchical data)                                                      |

### **When to Use Each:**

* **Use a view** when:

  * You need a reusable query that abstracts complexity.
  * You need to join multiple tables or have complex aggregation that needs to be accessed frequently.
  * You need the abstraction to persist across sessions and be accessible to other users or applications.

* **Use a CTE** when:

  * You need a temporary result set that simplifies a complex query.
  * You need to break down a large query into logical steps.
  * You need to handle recursive queries or hierarchical data.

### Example of Recursive CTE:

```sql
WITH RECURSIVE OrgChart AS (
    SELECT employee_id, manager_id, employee_name
    FROM employees
    WHERE manager_id IS NULL
  UNION ALL
    SELECT e.employee_id, e.manager_id, e.employee_name
    FROM employees e
    JOIN OrgChart o ON e.manager_id = o.employee_id
)
SELECT * FROM OrgChart;
```

In this case, a recursive CTE helps fetch an organizational chart from hierarchical data.

### Conclusion:

* **Views** are persistent and can be reused throughout the application.
* **CTEs** are temporary and are useful for breaking down complex queries within a single execution scope.

Both can improve readability and make SQL code more maintainable!

