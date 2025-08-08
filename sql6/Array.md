## Array/repeated data data type

List of valuyes in  a column

create table project_name.dataset_name.table name .. - cmd to create table in big query

Get all user id when views>10 and has accepted i strue

<img width="1600" height="816" alt="image" src="https://github.com/user-attachments/assets/50170ecf-7248-49d3-a5a5-1099abed6b88" />

<img width="580" height="242" alt="image" src="https://github.com/user-attachments/assets/f756ccfe-cd00-4c9e-b906-0a1267c812f5" />


<img width="430" height="243" alt="image" src="https://github.com/user-attachments/assets/97c874eb-4165-492f-8129-823801ef88ff" />


<img width="540" height="296" alt="image" src="https://github.com/user-attachments/assets/8db994ae-3126-463a-b7c9-33865b42b56b" />

<img width="481" height="116" alt="image" src="https://github.com/user-attachments/assets/c72b5c5e-6cc0-4a2b-b8d9-f6b9dbe9673d" />

<img width="372" height="44" alt="image" src="https://github.com/user-attachments/assets/05974583-7abf-4894-97f1-4a537b2e8cab" />

In **Google BigQuery**, the `ARRAY` data type is used to store repeated values, meaning you can have a list of values within a single field of a record. This is useful when you need to handle multi-valued data, such as multiple phone numbers for a person, multiple items in an order, or multiple tags associated with a document.

### Key Features of Arrays in BigQuery:

* An array can store **any type** of data: `STRING`, `INT64`, `FLOAT64`, `BOOLEAN`, `DATE`, etc.
* You can use **array functions** to manipulate and query arrays (e.g., `ARRAY_LENGTH`, `ARRAY_CONTAINS`, `ARRAY_AGG`).
* BigQuery supports **nested arrays**, where arrays can contain arrays, making it possible to create complex, multi-level structures.

### How to Define an Array in BigQuery:

When defining a table in BigQuery, you can declare an array column by specifying the `ARRAY` data type for that column.

#### Example 1: Creating a Table with an Array Column

```sql
CREATE OR REPLACE TABLE my_dataset.employees AS
SELECT
  1 AS employee_id,
  'John Doe' AS name,
  ['123-456-7890', '987-654-3210'] AS phone_numbers;  -- Array of phone numbers
```

In this example:

* The `phone_numbers` field is defined as an array of `STRING` values. This means each employee can have multiple phone numbers stored in that field.

#### Example 2: Querying Array Data

You can query arrays using BigQuery's built-in functions.

```sql
SELECT
  employee_id,
  name,
  phone_numbers
FROM
  my_dataset.employees
WHERE
  ARRAY_LENGTH(phone_numbers) > 1;  -- Retrieve employees with more than one phone number
```

This query retrieves all employees who have more than one phone number stored in the `phone_numbers` array.

#### Example 3: Flattening Arrays Using `UNNEST`

To convert an array to a set of rows (also called "flattening" the array), you can use the `UNNEST` function.

```sql
SELECT
  employee_id,
  name,
  phone_number
FROM
  my_dataset.employees,
  UNNEST(phone_numbers) AS phone_number;
```

In this example:

* `UNNEST(phone_numbers)` takes the array of phone numbers and "flattens" it so that each phone number appears in a separate row.

### Array Functions in BigQuery

Here are some useful functions for working with arrays:

1. **`ARRAY_LENGTH`**: Returns the number of elements in an array.

   ```sql
   SELECT ARRAY_LENGTH(phone_numbers) AS num_phone_numbers
   FROM my_dataset.employees;
   ```

2. **`ARRAY_CONTAINS`**: Checks if an array contains a specific element (note: BigQuery does not have a direct `ARRAY_CONTAINS` function, but you can use `ARRAY` with `IN` for similar behavior).

   ```sql
   SELECT
     employee_id,
     name
   FROM
     my_dataset.employees
   WHERE
     '123-456-7890' IN UNNEST(phone_numbers);  -- Check if the phone number is in the array
   ```

3. **`ARRAY_AGG`**: Aggregates values into an array. This is useful for grouping and combining values into arrays.

   ```sql
   SELECT
     employee_id,
     ARRAY_AGG(phone_number) AS all_phone_numbers
   FROM
     my_dataset.employees
   GROUP BY
     employee_id;
   ```

4. **`ARRAY` constructor**: You can also create arrays using the `ARRAY` constructor function.

   ```sql
   SELECT
     employee_id,
     ARRAY[phone_number] AS phone_numbers
   FROM
     my_dataset.employees;
   ```

5. **`ARRAY` with `DISTINCT`**: Get distinct elements from an array.

   ```sql
   SELECT
     employee_id,
     ARRAY(SELECT DISTINCT phone_number FROM UNNEST(phone_numbers) AS phone_number) AS unique_phone_numbers
   FROM
     my_dataset.employees;
   ```

6. **`ARRAY_TO_STRING`**: Converts an array into a string by concatenating the elements with a separator.

   ```sql
   SELECT
     employee_id,
     ARRAY_TO_STRING(phone_numbers, ', ') AS phone_numbers_str
   FROM
     my_dataset.employees;
   ```

### Example Use Case: Storing Multiple Tags for an Item

You might store multiple tags for a product in an array. Here's an example:

```sql
CREATE OR REPLACE TABLE my_dataset.products AS
SELECT
  101 AS product_id,
  'Laptop' AS product_name,
  ['electronics', 'computer', 'laptop', 'technology'] AS tags;
```

You can query this table to find products with a specific tag, for example:

```sql
SELECT
  product_id,
  product_name,
  tags
FROM
  my_dataset.products
WHERE
  'laptop' IN UNNEST(tags);
```

### Nested Arrays

BigQuery also supports **nested arrays**, where an array contains other arrays or structs. For example:

```sql
CREATE OR REPLACE TABLE my_dataset.orders AS
SELECT
  1 AS order_id,
  '2023-08-01' AS order_date,
  [
    STRUCT('item1' AS product_name, 2 AS quantity),
    STRUCT('item2' AS product_name, 1 AS quantity)
  ] AS items;
```

In this case, `items` is an array of structs, where each struct has two fields: `product_name` and `quantity`.

You can query nested arrays as follows:

```sql
SELECT
  order_id,
  item.product_name,
  item.quantity
FROM
  my_dataset.orders,
  UNNEST(items) AS item;
```

### Conclusion

Arrays in BigQuery are a powerful feature that allows you to handle repeated or multi-valued data efficiently. With array functions, you can manipulate, query, and aggregate data stored in arrays, enabling more advanced use cases like handling lists, sets, and even nested data structures.

If you have any specific questions or need more examples, feel free to ask!
