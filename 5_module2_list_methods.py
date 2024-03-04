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

# count() method
lst3 = ["a", ["c", "d"], ["c", "d"], ("m", "n"), ("m", "n")]
count = lst3.count(("m", "n"))
print("\nCount number for (\"m\", \"n\") is:", count)

# pop method
car_lst = ["Civic oriel", "Civic reborn", "Civic Rebirth", "Honda city", "Honda fit", "Honda vezel"]
print("\nValues before using POP:", car_lst)
pop1 = car_lst.pop()
print("\nUsing pop without index:", pop1)
print("Updated List:", car_lst)
pop2 = car_lst.pop(-1)
print("\nPOP last element of list:", pop2)
print("Updated List:", car_lst)
pop3 = car_lst.pop(-3)
print("\nPOP 4th Element in List:", pop3)
print("Updated List:", car_lst)

# reverse() method
car_lst = ["Civic oriel", "Civic reborn", "Civic Rebirth", "Honda city", "Honda fit", "Honda vezel"]
car_lst.reverse()
print("\nReversed list with reverse method is:", car_lst)
rvrs_lst = car_lst[::-1]
print("\nReverse list using slicing operator:", rvrs_lst)
for car in reversed(rvrs_lst):
    print("\n\t\t", car)

# sort() method
lst_srt = [12, 45, 6, 56, 46, 45,43, 3, 5 ,35 , 35, 2.5, 3432, 355, 35]
lst_srt.sort()
print("\nList sorted:", lst_srt)
lst_srt.sort(reverse= True)
print("\nReverse sorted list is:", lst_srt)
srt_str = ["Awais", "Muzammil", "Javaid", "Saqlain", "Ahsan"]
srt_str.sort()
print("\nSorted string list:", srt_str)
srt_str.sort(reverse = True)
print("\nReverse string list:", srt_str)

# copy() method
ls = srt_str.copy()
print("\nCopied list will be as:", srt_str)

# clear() method
ls.clear()
print("\nList empty using clear():", ls)
del ls[:]
print("\nList empty using del:", ls)
