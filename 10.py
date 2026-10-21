# Generate numbers using generator function

def generate_numbers(n):
    for i in range(1, n + 1):
        yield i

# Function call
numbers = generate_numbers(5)

for num in numbers:
    print(num)