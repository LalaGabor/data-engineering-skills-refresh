## Key takeaway

Window functions do not determine their own ordering. The window specification controls the **partition and ordering**, while the function determines the calculation performed over that window.

Reminder: The grain must be target grain at aggregation roll up. Otherwise the rolledup aggregation will be present in incorrect rows. For example if the target grain is customers.
We want sum(sales) per customer. But if we keep sale_id in the table we could have the sum(sales) in each customer_id + sale_id combination. This can have knockon effects.


Reminder: RANK() takes no argument. The order of the target values being determined by ORDER BY

REMINDER: Identify the target output, and the target grain. Then identify the intermediate tables required for aggregation/joining/filtering/window functions etc.
Then build the query. Best practice for complex queries