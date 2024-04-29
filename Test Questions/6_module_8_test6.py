'''
    Welcome....!
    Module # 8 (Test 6)
    You get an array of numbers, and return the sum of all of the positive ones. 
    Example [1, -4, 7, 12] => 1+7+12 = 20. If there is nothing to sum return 0. 
    You can not use the if statement.

'''


numbers = [1, -4, 7, 12]
total = 0
for num in numbers:
    total += max(0, num)

print(total)

