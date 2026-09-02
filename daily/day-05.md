# Day 5 — SQL Analytics

* Continued advanced SQL from Day 4.
* Practised correlated subqueries with `EXISTS`.
* Added date-based cohort analysis using `DATE_FORMAT()`.
* Built cohort revenue and customer activity analysis.
* Calculated retention and revenue retention.
* Practised `LAG()` and `LEAD()` for period comparisons.
* Built running totals with `SUM() OVER (ORDER BY ...)`.
* Built moving averages with `AVG() OVER (... ROWS BETWEEN ...)`.
* Practised percentage change and percentage-of-total calculations.
* Used `PARTITION BY` for customer-level running totals.
* Discussed defensive SQL patterns, especially `NULLIF()` for zero denominators.
* Developed a structured approach to complex queries:
  **identify grain → identify intermediate datasets → aggregate → window/subquery operations → join → calculate → filter → validate**.
* Discussed data-engineering terminology such as grain, intermediate datasets, and query-layer separation.
* Final complex SQL exercise started, combining CTEs, aggregation, correlated subqueries, windows, joins, dates, and defensive SQL.

## Key takeaway

The focus shifted from memorising SQL syntax toward **query decomposition, grain awareness, validation, and choosing the simplest correct implementation**.

## Next

**Day 6 — Difficult mixed SQL problems**, including a deliberate revisit of correlated subqueries.
