employees = [
    {"name": "Rahim", "salary": 25000},
    {"name": "Karim", "salary": 32000},
    {"name": "Kawsar", "salary": 28000},
    {"name": "Hasan", "salary": 40000},
    {"name": "Sakib", "salary": 35000}
]

higest_selary=0
higest_employee=""

for employee in employees:
    if employee ["salary"] > higest_selary:
        higest_selary=employee["salary"]
        higest_employee=employee["name"]


print("Get to higest salary person name is:",higest_employee)

print("salary:",higest_selary)