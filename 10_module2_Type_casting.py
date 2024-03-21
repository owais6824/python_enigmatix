'''
    Welcome...!
    Module # 2 (Type Casting)
    Here we will discuss type casting techniques in python...

'''

# Taking inputs without type casting
integer = input("Enter the integer:")
print(f"You entered: {integer} and its type is {type(integer)}")

'''
        Look we entered an integer but
        compiler is taking that as string...
        Here the concept for the type casting is used.....
'''

# Taking input with some specific type casting
integer1 = int(input("\nEnter an integer: "))
print(f"You entered {integer1} and its type is {type(integer1)}")

float_num = float(input("\nEnter the float input :"))
print(f"You entered {float_num} and its type is {type(float_num)}")

string = str(input("\nEnter the string :"))
print(f"You entered {string} and its type is {type(string)}")