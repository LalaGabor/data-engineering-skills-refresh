Todays Key Takeaways
- Correlated subqueries evaluates rows from the outer query one at a time
- example SELECT * FROM customers WHERE EXISTS (SELECT 1 FROM orders WHERE ....amount > 200)

- Key pattern: Complex query required? Think: "Which grain is required for output?"
-Reminder Group By group then calculate then roll up to selected group

- To acheive a rolling average, use the window function ROWS BETWEEN

- An alternative to finding totals via SUM(x) ...GROUP BY is to use SUM (x) OVER (). This sums in the window not through roll up.

- Reminder: The size of a WINDOW is equivalent to the current row plus preceding rows in the partition