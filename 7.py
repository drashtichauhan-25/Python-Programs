
class Animal:
    def show(self):
        print("This is Animal class")

class Dog(Animal):
    def show(self):
        print("This is Dog class")

class Puppy(Dog):
    def show(self):
        print("This is Puppy class")

    def __str__(self):
        return "This is a Puppy object"

# Creating object
p = Puppy()

# Demonstrating MRO
print("Method Resolution Order:")
print(Puppy.mro())

# Calling method
p.show()

# Demonstrating magic method
print("Magic Method:")
print(p)
