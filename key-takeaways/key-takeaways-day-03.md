Takeaways:

-NOT IN resolves to UNKNOWN when encountering a NULL
-WHERE only returns TRUE rows
-Aggregations ignore NULLs in rows 
- DATE_TRUNC returs a string vs YEAR or MONTH returning a datetime field
- WHERE, then GROUP BY, then HAVING
- Filters from outer query do not apply to inner query
- Correct thought pattern for complex query, identify correct grain, then subdivide where necessary staying with grain
- WINDOW functions and aggregation/calculations must be separated via CTE or query