'''
    Welcome...!
    Module # 2 
    We will discuss some methods in the lists

'''

# append() method
lst = ["Awais", "Honey", "Muzammil"]
print("\nValues before append:", lst)
lst.append("Ahsan")
print("\nValues after append are:", lst)

# extend() method
lst2 = ["Javaid", "Saqlain"]
print("\nList before using extend method:", lst2)
lst2.extend(lst)
print("\nList after using extend function", lst2)

# insert() method
cr_lst = ["audi", "rolls royce", "dodge"]
print("\nvalues before insert:", cr_lst)
cr_lst.insert(2, "mercedes")
print("\nvalues after insert:", cr_lst)

# remove() method
print("\nbefore using remove method:", cr_lst)
cr_lst.remove("dodge")
print("\nAfter remove method:", cr_lst)