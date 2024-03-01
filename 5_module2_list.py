'''
    Welcome...!
    Module # 2 (list)
    we will discuss about concepts of list to get familiar with it....

'''

# create list in python
list = [1, 2, 3, 4, 5]
print("\nHere is the list that was created", list)

# create an empty list 
emp_lst = []
print("\nSee this list is empty", emp_lst)

# list of integers
in_lst = [12, 34, 56, 78, 90, 100]
print("\nLsit with numbers is", in_lst)

# list of string
st_lst = ["Awais", "Honey", "Muzammil"]
print("\nlist with string elements is", st_lst)

# list with  mixed type data
mix = [1, "Awais", 2 , "Muzammil", 3, "Honey"]
print("\nMixed datatype list", mix)

# access element with index 
list2 = ["Naeem", "Ali", "Ahmad", "Ahad"]
print("\nElement with index 2 is", list2[2])

# Negative indexing
list3 = [11, 22, 33, 44, 55]
print("\nLast element of the list is", list3[-1])

# slicing list
list4 = [66, 24, 2, 3, 34, 345]
print("\nResult for slicing is", list4[2 : 4])
print("\nSlicing till end", list4[3 : ])
print("\nSlicing all the list", list4[ : ])

# add elements in list
lst = ["Asad", "Ali", "Aamir", "Asim"]
print("\nList before append", lst)
lst.append("Ayyub")
print("\nList after append", lst)

# add elements in specific index
lst_m = ["Bilal", "Basit", "Basheer"]
print("\nList before insert", lst_m)
lst_m.insert(0, "Bilawal")
print("\nList after insert", lst_m)

# adding data with iterables
lst.extend(lst_m)
print("\nExtened list will be as :", lst)

# change list item
print("\nList before changing", lst_m)
lst_m[1] = "Awais"
print("\nChanged list is ", lst_m)

# remove item from list 
lst2 = [23, 24, 25, 26, 27, 28, 29]
print("\nBefore remove data is ", lst2)
lst2.remove(27)
print("\nAfter remove list", lst2)

# deleting by indexes 
car_lst = ["Audi", "BMW", "Bentley", "Rolls Royce", "Jaguar", "Toyota", "Honda"]
print("\nCars list before delete", car_lst)
del car_lst[5]
print("\nCars list after deletion", car_lst)
del car_lst[4 : 6]
print("\nDelete with range", car_lst)

# length of list
print(len(car_lst)) 

# iteration in list
for cars in car_lst:
    print("\nCar list contains", cars)

