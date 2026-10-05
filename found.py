student_count = 0

with open("list.txt", "r") as file:

    for line in file:
        if "========== Student" in line:
            student_count += 1

print("Total Students:", student_count)