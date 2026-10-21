
# Write mode
f = open("demo.txt", "w")
f.write("Hello Python\n")
f.close()

# Read mode
f = open("demo.txt", "r")
print("File Data:", f.read())
f.close()

# Append mode
f = open("demo.txt", "a")
f.write("Welcome to Python")
f.close()

# Read updated data
f = open("demo.txt", "r")
print("Updated Data:")
print(f.read())
f.close()
