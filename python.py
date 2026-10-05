numbers = [12, 7, 25, 40, 9, 18, 33, 50,5]
count_even=0
count_odd=0
even_sum=0
odd_sum=0
for number in numbers:
    if number%2==0:
        count_even+=1
        even_sum+=number
    else:
        count_odd+=1
        odd_sum+=number

total=even_sum+odd_sum
print("Total Even:",count_even)
print("Total odd:",count_odd)
print("Total Even sum is:",even_sum)
print("Total odd sum:",odd_sum)
print("Even+odd=",total)

