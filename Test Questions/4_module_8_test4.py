'''
    Welcome...!
    Module # 8 (Test 4)
    You are given a string. Suppose a character 'c' occurs 4 times in the string. 
    Replace these consecutive occurrences of character 'c' with (4, c) in the string....

'''
 
def str_occr(string):
    str_new = ''
    count = 1

    for i in range(len(string)):
        if i < len(string) - 1  and string[i] == string[i + 1]:
            count += 1
        else:
            str_new += f"({count}, {string[i]})"
            count = 1

    return str_new.strip()

strng = "1222311"
print(str_occr(strng))
        