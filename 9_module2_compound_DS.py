'''
    Welcome ...!
    Module # 2 (Compound Data-structures)
    We will discuss about all compound data structures....

'''

# Compound data-structures are as follows...

# Lists and its operations
name = ["Awais", "Honey", "Muzammil"]
print("Length of list is:", len(name))

print("\nList item at index 1 is:", name[1])
print("\nLast item of list :", name[-1])

print("\nIteration of lists can be done as :")
for nam in name:
    print("\n",nam)

print("\nRepition operator on list can be done as :")
print(name * 5)


# Tuples and its operations
ages = (21, 24, 23)
print("\nLast item of the tuple is :", ages[2])


# Dictionaries and its operations
com_dic = {"Awais" : 21,
           "Honey" : 24,
           "Muzammil" : 23}
print("Dictionary that we created is as:", com_dic)

# Now we will see how can we create dictionary from already list and tuple...
new_dic = dict(zip(name, ages))
print("\nDictionary from already list and tuple:",new_dic)