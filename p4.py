num=int(input("Enter the number:"))

orginal=num
reverse=0

while num>0:
    digit=num%10
    reverse=reverse*10+digit
    num=num//10
if orginal==reverse:
    print("palindrom")
else:
    print("not palindrom")