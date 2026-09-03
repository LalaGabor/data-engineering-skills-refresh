# Day 6 — SQL

* Reviewed `UNION` vs `UNION ALL`.
* Covered requirements for unioned queries:

  * same number of columns
  * compatible data types
  * positional column matching
  * column names inherited from the first query
* Discussed why `UNION ALL` is preferable when duplicates represent legitimate records.
* Completed an interview-style exercise combining two order sources with `UNION ALL`.
* Practised aggregating after the union to customer grain.
* Practised `LAG()` ordered by a calculated measure.
* Practised window aggregates with `SUM(...) OVER ()` for percentage-of-total calculations.
* Continued reinforcing query decomposition by grain and intermediate result.
* Reviewed `RANK()` syntax:

  * `RANK() OVER (...)`
  * ranking is controlled by `ORDER BY` inside the window
  * `PARTITION BY` defines independent ranking groups.
* Reviewed multiple expressions in `PARTITION BY` and `ORDER BY`.

