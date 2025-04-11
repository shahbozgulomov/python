#. Sort a Dictionary by Value
#Write a Python script to sort (ascending and descending) a dictionary by value.
dict1 = {'a':1,'b':2,'c':3}
ascending = dict(sorted(dict1.items()))
print(ascending)
descending = dict(sorted(dict1.items(), reverse = True))
print(descending)
### 2. Add a Key to a Dictionary
Write a Python script to add a key to a dictionary.
#adding a key to the dictionary called dict1
updated_dic = dict1.update([('d',5)])
print(updated_dict)
Concatenate Multiple Dictionaries
Write a Python script to concatenate the following dictionaries to create a new one.
dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}
concatenated_dic = dic1|dic2|dic3
concatenated_dic


#generating and printing a dictionary that contains a number (between 1 and n) in the form `(x, x*x)`.

squared_dic = {n :  n**2 for n in range(1,n)}
squared_dic
#square dictionary 1 to 15
squared_dic = {n :  n**2 for n in range(1,16)}
squared_dic
# a Python program to create a set.
my_set = {1,2,3,4,5}
my_set
#Write a Python program to iterate over sets.
my_set
for element in my_set:
    
    element
#adding a value to my_set
new_set = my_set.add(8)
new_set
#clearing a set
cleared_set = my_set.clear()
cleared_set
#removing an element if there is 
removed_set = my_set.remove(4)
removed_set


