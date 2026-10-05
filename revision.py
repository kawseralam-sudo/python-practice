user = int(input("Enter the number: "))

i = 1
even_count = 0
odd_count=0


even_sum=0
odd_sum=0
for i in range(i,user):
    if i%2==0:
        even_count+=1
        even_sum=even_sum+i
    else:
        odd_count+=1
        odd_sum=odd_sum+i
    i+=1
print("Total even:",even_count)
print("Total odd",odd_count)
print(even_sum)
print(odd_sum)

