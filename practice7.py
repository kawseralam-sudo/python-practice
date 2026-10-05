students = [
    {"name": "Rahim", "marks": 80},
    {"name": "Karim", "marks": 45},
    {"name": "Kawsar", "marks": 90},
    {"name": "Hasan", "marks": 44},
    {"name": "Sakib", "marks": 30}
]

pass_count = 0
fail_count = 0
total_marks = 0

for student in students:

    # Total marks
    total_marks = total_marks+ student["marks"]

    # Pass / Fail
    if student["marks"] >= 40:
        pass_count += 1
    else:
        fail_count += 1

# Average
average = total_marks / len(students)

print("Pass:", pass_count)
print("Fail:", fail_count)
print("Total Marks:", total_marks)
print("Average:", round(average,2))