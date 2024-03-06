'''
    Welcome....!
    Module # 2 (Dictionary)
    We will look forward to some concepts of dictionary in python

'''

# create dictionary
capitals = {
    'Punjab' : 'Lahore',
    'Sindh' : 'Karachi',
    'Balochistan' : 'Quetta',
    'khyberpakhtoonkha' : 'Peshawar'
}
print("Created dictionary is :", capitals)

# access items in dictionary
print("\nCapital for punjab is:", capitals['Punjab'])

# add items in dictionary
print("\nCapitals are:", capitals)
capitals['paksitan'] = 'Islamabad'
print("\nCapitals after update:", capitals)

# remove items from dictionary
print("\nCpaitals before remove:", capitals)
del capitals['paksitan']
print("\nCapitals after remove:", capitals)

# iterate through dictionary
for value in capitals:
    print(value)

print()

for value in capitals:
    value2 = capitals[value]
    print(value2)

'''
        dictionary methods

'''

# dictionary clear() method
numbers = {1 : 'one', 2 : 'Two', 3 : 'Three', 4 : 'four'}
numbers.clear()
print("\nNumbers are:", numbers)

# dicitonary copy() method
num = {1 : 'one', 2 : 'Two', 3 : 'Three', 4 : 'four'}
num2 = num.copy()
print("\nOriginal dictionary:", num)
print("\nCopied dictionary:", num2)

# dictionary fromkeys() method
keys = {1, 2, 3, 4, 5}
values = ['one', 'two', 'three', 'four', 'five']
numb = dict.fromkeys(keys, values)
print(numb)

# dictionary get() method
student = {'name' : 'Awais', 'age' : 21}
print("\nName :", student.get('name'))
print("\nSalary :", student.get('salary'))

# dictionary items() method
person = {'name' : 'Awais', 'Age' : 21}
print("\nItems on the dictionary are:", person.items())

# dictionary keys() method
num = {1 : 'one', 2 : 'Two', 3 : 'Three', 4 : 'four'}
print("\nKeys for the deicitonaries are:", num.keys())

# dictionary popitem() method
client = {'name' : 'Awais', 'Age' : 21, 'depart' : 'Computer Science'}
print("\nOriginal dictionary:", client)
print("\nPoped item is:", client.popitem())
print("\nUpdated dictionary :", client)

