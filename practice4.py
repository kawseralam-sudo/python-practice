student = {
    "name": "Kawsar",
    "math": 80,
    "english": 75,
    "python": 90,
    "physics": 65
}

total_marks = (
    student["math"]
    + student["english"]
    + student["python"]
    + student["physics"]
)

average = total_marks / 4

highest = student["math"]
lowest = student["math"]

for key, mark in student.items():

    if key != "name":

        if mark > highest:
            highest = mark

        if mark < lowest:
            lowest = mark

print("Total marks:", total_marks)
print("Average marks:", average)
print("Highest mark:", highest)
print("Lowest mark:", lowest)