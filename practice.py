numbers = [5, 2, 8, 5, 3, 2, 5, 8, 2, 5, 9]

kawsar={}
count_higest=0
most_number=0

for number in numbers:
    if number in kawsar:
        kawsar[number]+=1
    else:
        kawsar[number]=1

for number,count in kawsar.items():
    print(number, ":" ,count)
    if count>count_higest:
        count_higest=count
        most_number=number

print("Most repeted number is :", most_number)
print("count:",count_higest)