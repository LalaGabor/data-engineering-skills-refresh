Reminder. DO NOT USE UPDATE as a dict method. Simply "assign" a value to the dict key and this will be "appended" to the dictionary.

Syntax like: dict[key] = value. 
Then dict = {**dict, key:value}