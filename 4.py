import random


print("----- Random Number Generator -----")

# Random integer
num = random.randint(1, 100)
print("Random Number :", num)

# Random decimal number
decimal = random.uniform(10, 50)
print("Random Decimal:", decimal)

# Random numbers from a range
numbers = random.sample(range(1, 101), 5)
print("5 Random Numbers:", numbers)

# Random choice
subjects = ["Python", "DBMS", "AI", "Data Science", "Java"]
print("Random Subject:", random.choice(subjects))

# Generate 6-digit OTP
otp = random.randint(100000, 999999)
print("Generated OTP:", otp)
