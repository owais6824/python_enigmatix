'''
    Welcome...! 
    Module # 2
    here we will discuss strings in python

'''

# creating strings
name = "Awais"
print(name)
name2 = 'Mubashra'
print(name2)

# access charachters in variable
# consider varaibles above
# print 1st index character of both variables called indexing
print("\nFirst character is", name[0])
print("\nFirst character is", name2[0])

# negative indexing
print("\nSecond character form end is ", name[-2])
print("\nSecond character form end is ", name2[-2])

# slicing
# we will access characters with range 
val1 = (name[2: 5])
print("\nLast charcters of name are :", val1)
val2 = name2[0: 3]
print("\nFirst characters of name are : ", val2)

# concatinating the strings / joining two strings
comp = val2 + val1
print("\nComplete name become ",comp)

# strings with multiple lines
comp_name = """\n
            Muhammad Awais
            
            Mubashra khizer
        here is the multiple line strings
"""

print(comp_name)


'''
        String operations
'''
# comparing two strings

string1 = "Hello, dear"
string2 = "Hello dear"
string3 = "Hello, dear"
print(string1 == string2)
print(string2 == string3)
print(string1 == string3)

# iterate the string
for letter in name:
    print("  -->",letter) 

# find length of the string
print(len(name))
print(len(name2))

# membership test
print("a" in string1)
print("a" in name2)

# escape sequences in python
stat = "\nHe said \"I'm working on python\""
print(stat) 

# string formating
nam = (f'{string1} .... {name}')
print(nam)