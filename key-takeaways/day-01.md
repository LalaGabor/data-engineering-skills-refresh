# Day 1 — Key Takeaways

* **Date functions:** rusty; need more practice.
* **Query optimiser:** can rewrite the SQL into a more efficient execution plan.
* **`ROW_NUMBER()`:** assigns a sequential number to each row within a window.
* **`OVER (...)`:** defines the window for a window function.
* **`PARTITION BY`:** divides the rows in the window into separate groups; the window function is evaluated independently for each group.
* **`COUNT(DISTINCT ...)`:** counts unique values rather than rows.
* **`HAVING`:** filters groups after aggregation, whereas `WHERE` filters rows before aggregation.
* **`GROUP BY`:** groups rows so aggregate functions such as `COUNT()` and `AVG()` can be calculated per group.
