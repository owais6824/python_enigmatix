'''
    Welcome...!
    Module # 2 (Sets Method)
    We are gonna discuss Sets Methods...

'''

# Set remove() method
set_num = {1, 2, 3, 4, 5, 6}
print("Set before removing element:", set_num)
set_num.remove(6)
print("\nSet after removing element:", set_num)

# Set add() method
set_vov = {'a', 'e', 'i', 'o'}
print("\nElements Before add:", set_vov)
set_vov.add('u')
print("\nElements after add:", set_vov)

# Set copy() method
sampl = {12, 34, 56, 78, 98, 90}
print("\nFirst declared Set by name (sampl):", sampl)
sampl2 = sampl.copy()
print("\nAccessing the sampl2 set:", sampl2)

# Set clear() method
number = {11, 22, 33, 44, 55, 66}
number.clear()
print("\nAll the elements are cleared with clear():", number)

# Set difference() Method
A = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
B = {1, 2, 3, 4, 5}
print("\nDifference of two sets is:", A.difference(B))

# Set difference_update() Method
A = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
B = {2, 4, 6, 8, 10}
print("\nA before A.difference_update(B):", A)
A.difference_update(B)
print("\nA after A.difference_update(B):", A)

# Set discard() Method
A = {'Awais', 'Honey', 'Muzammil', 'Hamza'}
print("\nSet before discard():", A)
A.discard('Hamza')
print("\nSet after discard():", A)

# Set intersection() Method
num = {1, 2, 3, 4, 5}
num2 = {6, 7, 8, 9, 10}
print("\nIntersection will be result in:", num.intersection(num2))

# Set intersection() Method
print("\nIntersection_update result will be as:", num.difference_update(num2))




