- Window Aggregations do not collapse rows
- Thought patter for complex queries. (Roughly)
1. Define the required output
2. Identify the final grain
3. Identify the base tables needed
4. Build each required dataset
5. Decide on aggreation/WINDOW /Subquery/ JOIN
6. Apply calculations
7. Fileter at the correct stage
8. Validate the result
- REMINDER: ROWS BETWEEN is used to define the frame of the window for window aggregation