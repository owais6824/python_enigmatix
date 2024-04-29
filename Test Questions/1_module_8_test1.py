'''
    Welcome...!
    Module # 8 (Test 1)
    Write a function which will take integer as input and print each digit at separate line.
    You are not allowed to use str or any other method or any other method that convert the integer to string...

'''

def print_int(number):
    if number == 0:
        return

    while number > 0:
        num = number % 10
        print(num)
        number //= 10

print_int(int(input("Enter number:")))

    