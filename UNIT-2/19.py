#Write a program to demonstrate iterators and iterables in Python.


# Iterable Example
fruits = ["Apple", "Banana", "Mango"]

print("Iterable using for loop:")
for fruit in fruits:
    print(fruit)

# Iterator Example
print("\nIterator using iter() and next():")

it = iter(fruits)

print(next(it))
print(next(it))
print(next(it))
