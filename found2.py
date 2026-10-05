try:
    search_name = input("Enter student name: ")

    found = False

    with open("list.txt", "r") as file:

        for line in file:

            if line.startswith("Name:"):

                name = line.replace("Name:", "").strip()

                if name.lower() == search_name.lower():
                    found = True
                    print("Student Found!")
                    print("Name:", name)

    if not found:
        print("Student Not Found!")

except FileNotFoundError:
    print("File not found")