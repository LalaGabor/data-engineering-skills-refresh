## Overview

Day 2 focused on JOIN behaviour, cardinality, grain, NULLs, and avoiding incorrect aggregations caused by row multiplication.

The main lesson was to identify the grain of each table and the required grain of the result before joining or aggregating.

## Topics covered

- JOIN cardinality
- One-to-one, one-to-many, many-to-one and many-to-many relationships
- Grain: what one row represents
- Row multiplication when joining independent many-side tables
- `INNER JOIN` vs `LEFT JOIN`
- `ON` vs `WHERE`
- NULL behaviour with `LEFT JOIN`
- Aggregating independent many-side tables before joining
- Establishing a customer + month grain
- Using `UNION` to combine activity months
- MySQL limitations around `FULL OUTER JOIN`