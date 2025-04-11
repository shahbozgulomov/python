fruit_list = ['apple','banana','kiwi','grapefruit','melon']
fruit_list = ['apple','banana','kiwi','grapefruit','melon']
fruit_list[2]
list1 = [1,2,3]
list2 = [4,5,6]
concatenated_list = list1 + list2
print(concatenated_list)
list3 = [1,2,3,4,5,6]
list4 = [list3[0],list3[3],list3[-1]]
print(list4)

movie_list = ['spiderman 1','spiderman 2','spiderman 3','rocky 1','rocky2']
movie_tuple = tuple(movie_list)
movie_tuple
list_cities = ['london','paris','birmingham','amsterdam']
if list_cities.index('paris') > 0:
    print('there is Paris in the list')
list = [1,2,3,4]
list += list
list
7.swap places
list = [1,2,3,4,5,6]
list[0],list[-1] = list[-1] , list[0]
list
8
tuple = (1,2,3,4,5,6,7,8,9,10)
tuple[3:7]
9
list_colours = ['blue','blue','red','red']
list_colours.count('blue')
10
tuple_animals = ('cat','leopard','lion','snake')
tuple_animals.index('lion')
11
tuple1= (1,2,3)
tuple2 = (4,5,6)
tuple3 = tuple1 + tuple2
tuple3
12 lenth
list
tuple
print(len(list))
print(len(tuple))
13 tuple to list
my_tuple = (1,2,3,4)
my_list = list(my_tuple)
print(my_list)

max and min in tuples
tuple = (1,2,3,4,5)
max_tuple = max(tuple)
min_tuple = min(tuple)
print(max_tuple)
print(min_tuple)
tuple1 = ('me','and','you')

a = (reversed(tuple1))
print(a)

# Homework: List and Tuple Exercises

## 1. Create and Access List Elements
Create a list containing five different fruits and print the third fruit.

## 2. Concatenate Two Lists
Create two lists of numbers and concatenate them into a single list.

## 3. Extract Elements from a List
Given a list of numbers, extract the first, middle, and last elements and store them in a new list.

## 4. Convert List to Tuple
Create a list of your five favorite movies and convert it into a tuple.

## 5. Check Element in a List
Given a list of cities, check if "Paris" is in the list and print the result.

## 6. Duplicate a List Without Using Loops
Create a list of numbers and duplicate it without using loops.

## 7. Swap First and Last Elements of a List
Given a list of numbers, swap the first and last elements.

## 8. Slice a Tuple
Create a tuple of numbers from 1 to 10 and print a slice from index 3 to 7.

## 9. Count Occurrences in a List
Create a list of colors and count how many times "blue" appears in the list.

## 10. Find the Index of an Element in a Tuple
Given a tuple of animals, find the index of "lion".

## 11. Merge Two Tuples
Create two tuples of numbers and merge them into a single tuple.

## 12. Find the Length of a List and Tuple
Given a list and a tuple, find and print their lengths.

## 13. Convert Tuple to List
Create a tuple of five numbers and convert it into a list.

## 14. Find Maximum and Minimum in a Tuple
Given a tuple of numbers, find and print the maximum and minimum values.

## 15. Reverse a Tuple
Create a tuple of words and print it in reverse order.
