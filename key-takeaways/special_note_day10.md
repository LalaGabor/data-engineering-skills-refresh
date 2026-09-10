Python muscle memory is in fact rustier than thought. Today diagnosed slow performance in producing code like: 
customers = [
    {"id": 101, "name": " Alice ", "country": "Croatia"},
    {"id": 102, "name": " BOB ", "country": "Germany"},
    {"id": 103, "name": " Charlie ", "country": "Croatia"},
    {"id": 104, "name": " David ", "country": "Italy"},
]

revenues = [
    {"customer_id": 101, "revenue": 1250},
    {"customer_id": 102, "revenue": 850},
    {"customer_id": 103, "revenue": 2100},
    {"customer_id": 104, "revenue": 450},
]
combined = list(zip(customers, revenues)) # produces a list containing a 2 item tuple containing a dict in each item
filtered = []
for item in combined:
    if item[1]["revenue"] >= 800:
         filtered.append(item)
filtered.sort(key=lambda item: item[1]["revenue"], reverse=True)
for index, (customer, revenue) in enumerate(filtered, start=1):
     customer["name"] = customer["name"].strip().lower()
     print(f"{index}. {customer['id']} - {customer['name']} - {customer['country']} - {revenue['revenue']}")

Will add a non syllabus day to refresh instincts. Past projects largely "skipped ahead" to pandas
 without more deeply internalizing "raw" python for data, so I have assigned myself additional training