# Sum of digits using while loop

num = int(input("Enter a number: "))

sum = 0

while num > 0:
    digit = num % 10      # Get the last digit
    sum = sum + digit     # Add digit to sum
    num = num // 10       # Remove the last digit

print("Sum of digits =", sum)
