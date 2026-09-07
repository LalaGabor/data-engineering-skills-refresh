Key Learnings/Reminders
-customer = () is a tuple, customer = set() is an empty set
-order.values() returns all values; use order["customer"] to access the value associated with the key ["key"]
-Lists use append but sets use add()
-Common data manipulation pattern: create an empty collection, loop, check a condition, then add/manipulate the collection. 
	- This pattern can be condensed syntactically to a list/set/dict comprehension

- Syntax for a list comprehension:
 	- syntax [expression for item in iterable if condition]
	- real [order["customer"] for order in orders.february if order["status"] == "complete"]

Reminder: strings are immutable, methods do not change they create a new. therefore we must assign ("reassign") the new manipulated string to the target variable (name)

Loops, conditional, types (basic knowledge was relatively "there")