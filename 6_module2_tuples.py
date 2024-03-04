'''
    Welcome...!
    Module # 2
    We will discuss about tuple and its concepts...

'''

# create tuple
numbers = (2, 3, 4, 5, 6, 7, 8, 9)
print("Created tuple is:", numbers)

# tuple from tuple construct
names = ['Awais', 'Ahmad', 'Ali']
tu_name = tuple(names)
print("\nTuple created with tuple construct:", tu_name)

# empty tuple
emp_tup = ()
print("\nEmpty tuple is :", emp_tup)

# tuple with different datatypes
num = (23, 24, 25, 26, 27, 28, 29)
print("\nTuple with int datatype:", num)
string = ('Awais', 'Ali', 'Bilal', 'Basit')
print("\nTuple with string datatype:", string)
mixed = (1, 'Awais', 2, 'Ali', 3, 'Honey')
print("\nTuple with mixed datatype:", mixed)

# access tuple items
nam = ('Ford', 'Ram', 'Bmw', 'Audi')
print("\nThird index item in tuple:",nam[3])

# length of tuple
print("\nLength of tuple above is:", len(nam))

# iterate through tuple
for cr in nam:
    print("\nNames contain:", cr)

# check tuple item
print("\n",'mercedes' in nam)
print("\n",'Audi' in nam)

# one item tuple
m = ('Awais')
print("\nOne item tuple:", m)

# delete tuple
del mixed
print("\nDeleted mixed Tuple.")

# tuple count() method
print("\nCount for Audi is:", nam.count('Audi'))

# tuple index() method
print("\nIndex for Audi is:", nam.index('Audi'))