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
