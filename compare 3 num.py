a=int(input("Enter the first number:"))
b=int(input("Enter the second number:"))
c=int(input("Enter the third number:"))
if a>b and a>c:
    print("The large number is:",a)
elif b>a and b>c:
    print("The large number is:",b)
else:
    print("The large number is:",c)
    print("the min:",min(a,b,c))