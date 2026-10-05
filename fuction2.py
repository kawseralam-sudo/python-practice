def calculate_total(bangla, english, math):
    return bangla + english + math


def calculate_average(total):
    return total / 3


def calculate_grade(average):

    if average >= 80:
        return "A+"
    elif average >= 70:
        return "A"
    elif average >= 60:
        return "A-"
    elif average >= 50:
        return "B"
    elif average >= 40:
        return "C"
    else:
        return "F"


def check_result(bangla, english, math):

    if bangla >= 40 and english >= 40 and math >= 40:
        return "Pass"
    else:
        return "Fail"


# Student information

name = input("Enter student name: ")

bangla = int(input("Enter Bangla marks: "))
english = int(input("Enter English marks: "))
math = int(input("Enter Math marks: "))


# Calculate

total = calculate_total(bangla, english, math)

average = calculate_average(total)

grade = calculate_grade(average)

result = check_result(bangla, english, math)


# Output

print("\n----- Student Result -----")

print("Name:", name)
print("Bangla:", bangla)
print("English:", english)
print("Math:", math)

print("Total:", total)
print("Average:", average)
print("Grade:", grade)
print("Result:", result)