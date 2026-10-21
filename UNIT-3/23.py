import math

num = float(input("Enter a number: "))

print("\n----- Mathematical Operations -----")

print("Square Root     :", math.sqrt(num))
print("Square          :", math.pow(num, 2))
print("Cube            :", math.pow(num, 3))

print("Factorial       :", math.factorial(int(num)))

print("Logarithm        :", math.log(num))
print("Ceiling Value    :", math.ceil(num))
print("Floor Value     :", math.floor(num))

angle = float(input("\nEnter angle in degrees: "))

radian = math.radians(angle)

print("Sin Value        :", math.sin(radian))
print("Cos Value        :", math.cos(radian))
print("Tan Value        :", math.tan(radian))
