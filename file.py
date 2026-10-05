with open("data.txt", "w") as file:

    file.write("Name: Kawser\n")
    file.write("Age: 22\n")
    file.write("Department: CSE\n")

with open("data.txt","a") as file:
    
    file.write("How are you?\n")
    file.write("I am fine\n")

with open("data.txt", "r") as file:
    data = file.read()

print(data)
