'''
    Welcome...!
    Module # 2 (Sets)
    We will discuss about sets here to get familair with them

'''

# create set 
students = {'name', 'class', 'rollno', 'subject'}
print("\nWe created set is :", students)

# datatypes with sets
set_num = {1, 2, 3, 4, 5, 6}
print("\nSet with integer datatype:", set_num)
set_str = {'Awais', 'honey', 'muzammil'}
print("\nSet with string datatype is:", set_str)
set_mix = (1, 'Awais', 2, 'Honey', 3, 'Muzammil')
print("\nSet with mixed datatype:", set_mix)

# empty set
emp_set = set()
print("\nEmpty set:", emp_set, ",with datatype:", type(emp_set))

# duplicate numbers
numb = {1, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7 ,8 , 8, 9, 9, 0, 0}
print("\nElements can never be duplicate in set:", numb)

# add elements
bike = {'70cc', '100cc', '125cc', '150cc', '200cc'}
print("\nOriginal set is :", bike)
bike.add('300c')
print("\nUpdated set is :", bike)

# update sets
bikes = {'cd70', 'dream', 'pridor', '125'}
print("\nSet before update:", bikes)
bikes.update(bike)
print("\nSet after update:", bikes)

# remove elements in set
print("\nSet before Remove:", bikes)
bikes.remove('125cc')
print("\nSet after remove is:", bikes)

# iterate over set
for i in bikes:
    print("\nSet contains:", i)


'''
    Set Operations
'''

a = {1, 2, 3, 4, 5}
b = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

# set union
print("\nUnion using | ", a | b)
print("\nUnion using | ", a.union(b))

# set intersection
print("\nIntersection using &:", a & b)
print("\nIntersection using intersection():", a.intersection(b))

# set difference
print("\nDifference using - :", a - b)
print("\nDifference using difference():", a.difference(b))

# symmetric difference
print("\nSymmetric difference using ^:",a ^ b )
print("\nSymmetric difference using symmetric():", a.symmetric_difference(b))

# equal sets
if a == b:
    print("\nBoth sets are equal...")
else:
    print("\nSets are not equal...")

