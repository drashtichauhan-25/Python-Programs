print('1. Addition')
print('2. Multiplication')
print('3.Division')
print('4.Subtraction')

choice=int(input("enter choice:"))
a=int(input("enter A"))
b=int(input("enter B"))

if choice==1:
    print("Addition of two number is:",a+b)
elif choice==2:
    print(" Multiplication of two number is:",a*b)
elif choice==3:
    print("Division of two number is:",a/b)
elif choice==4:
    print("Subtraction of two number is:",a-b)

else:
    print("invalid choice")

