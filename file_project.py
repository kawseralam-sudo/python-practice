with open("list.txt", "w") as file:
    pass

student_count = 1

while True:

    name = input("Enter your name: ")
    age = input("Enter your age: ")
    department = input("Enter your department: ")

    with open("list.txt", "a") as file:
        file.write(f"\n========== Student {student_count} ==========\n")
        file.write(f"Name: {name}\n")
        file.write(f"Age: {age}\n")
        file.write(f"Department: {department}\n")

    print("Student data has been saved!")

    student_count += 1

    choice = input("Do you want to add another student? (yes/no): ")

    if choice.lower() != "yes":
        break


with open("list.txt", "r") as file:
    data = file.read()

print("\n========== All Student Data ==========")
print(data)