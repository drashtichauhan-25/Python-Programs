# math function direct call

import math

print(math.sqrt(25))


#math function with object

import math as m

print(m.floor(30.5))
print(m.ceil(30.5))

#import specific function from the module

from math import factorial

print(factorial(5))


#import ,multiple module

from math import pow, sqrt, factorial

print("Power:", pow(5, 5))
print("Square Root:", sqrt(25))
print("Factorial:", factorial(5))
