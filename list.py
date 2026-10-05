numbers = list(map(int, input("Enter 6 numbers: ").split()))

if len(numbers) != 6:
    print("Please enter exactly 6 numbers.")
else:
    if 60 in numbers:
        print("y")
    else:
        print("n")