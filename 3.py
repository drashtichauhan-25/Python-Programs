class Student:
    # Class variable
    college = "ABC College"

    def __init__(self, name, age):
        # Instance variables
        self.name = name
        self.age = age

# Creating objects
s1 = Student("Drashti", 22)
s2 = Student("Aananadi", 21)

# Displaying instance variables
print("Student 1:", s1.name, s1.age)
print("Student 2:", s2.name, s2.age)

# Displaying class variable
print("College:", Student.college)
