class Student:
    college = "MARWADI UNIVERSITY"     # Class variable

    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Instance method
    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)

    # Class method
    @classmethod
    def show_college(cls):
        print("College:", cls.college)

    # Static method
    @staticmethod
    def message():
        print("Welcome to Python Programming")


# Create object
s1 = Student("Drashti", 22)

# Calling instance method
s1.display()

# Calling class method
Student.show_college()

# Calling static method
Student.message()
