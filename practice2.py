numbers = [45, 12, 78, 34, 89, 23, 67, 10]
maximum = numbers[0]
minimum = numbers[0]
for number in numbers:
    if number > maximum:
        maximum=number
    elif number < minimum:
        minimum=number
print(maximum)
print(minimum)
print(maximum-minimum)