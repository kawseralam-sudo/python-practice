students = [
    {"name": "Rahim", "marks": 85},
    {"name": "Karim", "marks": 35},
    {"name": "Kawsar", "marks": 92},
    {"name": "Hasan", "marks": 48},
    {"name": "Sakib", "marks": 67}
]

pass_count = 0
fail_count = 0
total_marks = 0
higest_mark = 0

for student in students:

    total_marks += student["marks"]

    if student["marks"] > higest_mark:
        higest_mark = student["marks"]

    if student["marks"] >= 40:
        pass_count += 1
        status = "Pass"
    else:
        fail_count += 1
        status = "Fail"

    print(student["name"], "-", student["marks"], "-", status)

print("Total Pass:", pass_count)
print("Total Fail:", fail_count)
print("Average Marks:", total_marks / len(students))
print("Highest Mark:", higest_mark)