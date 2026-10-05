students = [
    {"name": "Rahim", "marks": 75},
    {"name": "Karim", "marks": 42},
    {"name": "Kawsar", "marks": 91},
    {"name": "Hasan", "marks": 63},
    {"name": "Sakib", "marks": 28}
]

highest_mark = students[0]["marks"]
highest_name = students[0]["name"]

second_mark = 0
second_name = ""

third_mark = 0
third_name = ""

lowest_mark = students[0]["marks"]
lowest_name = students[0]["name"]

for student in students:

    if student["marks"] > highest_mark:

        third_mark = second_mark
        third_name = second_name

        second_mark = highest_mark
        second_name = highest_name

        highest_mark = student["marks"]
        highest_name = student["name"]

    elif student["marks"] > second_mark:

        third_mark = second_mark
        third_name = second_name

        second_mark = student["marks"]
        second_name = student["name"]

    elif student["marks"] > third_mark:

        third_mark = student["marks"]
        third_name = student["name"]

    if student["marks"] < lowest_mark:
        lowest_mark = student["marks"]
        lowest_name = student["name"]

print("Highest:", highest_name, ":", highest_mark)
print("Second Highest:", second_name, ":", second_mark)
print("Third Highest:", third_name, ":", third_mark)
print("Lowest:", lowest_name, ":", lowest_mark)
