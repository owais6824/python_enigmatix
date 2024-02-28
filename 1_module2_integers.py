'''
    welcome...! 
    Module # 2 (Integers)
    we will discuss about datatypes and operators

'''

# numeric data types in python....
num1 = 1
print(num1, " number has data type ", type(num1) )

num2 = 23.4
print(num2, " number has data type ", type(num2))

num3 = 2+3j
print(num3, " number has data type", type(num3))


# number system in python
print(0b0100110)
print(0o15)

# type conversion 
# implicitly
print(1 + 3.9)

# explicitly
num4 = int(23.6)
print(num4)


# Random module in python
import random

# use of random range
print("\nRandom number is ", random.randrange(10, 90))

# printing random element in the list
list = ['a', 'b', 'c', 'd', 'e', 'f']
print("\nRandom value from the list is ", random.choice(list))

# shuffle the list
random.shuffle(list)
print("\nshuffled list is", list)

print("\nAny random number is ", random.random())

# using math module
import math

# printing pi
print(math.pi)

# Trignomertic functions
print("\nPi is ", math.cos(math.pi))
print("\nExponential function", math.exp(30))
print("\nSin Inverse", math.sinh(2))
print("\nLog function", math.log10(67))
print("\nFactorrail", math.factorial(7))

