num = int(input("Enter a number: "))

try:
    assert num > 0, "Number must be positive"
    print("Number is:", num)

except AssertionError as e:
    print(e)
