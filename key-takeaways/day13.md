Learning: Kwargs in practice:

If one wants to have "optionally used" keyword arguments one can use **kwargs and combine with keyword=get("passed_argument"["keyword"],0/NULL) to optionally use that argument.
Practically their primary is use is in decorators, middleware etc which is not highly relevant at my level of skill

Learning: Check list length / number of items in list with len()

Learning: To check if a keyword exists in a dictionary use: if keyword in dict: (not if dict[keyword] exists())

Usefulness of exception handling in DE python. 
Pass errors up to higherlevel functions.

Eg loader_file_34() fails. Then log the error and raise it. The higher level loader might decide to retry_pipeline(), delete_file_28...etc depending on the data/file structure
Not just for "print(error happened) as in toy exercises.