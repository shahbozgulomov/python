fruit_list = ['apple','banana','kiwi','grapefruit','melon']
fruit_list[2]
'kiwi'
list1 = [1,2,3]
list2 = [4,5,6]
concatenated_list = list1 + list2
print(concatenated_list)
[1, 2, 3, 4, 5, 6]
list3 = [1,2,3,4,5,6]
list4 = [list3[0],list3[3],list3[-1]]
print(list4)
[1, 4, 6]
movie_list = ['spiderman 1','spiderman 2','spiderman 3','rocky 1','rocky2']
movie_tuple = tuple(movie_list)
movie_tuple
('spiderman 1', 'spiderman 2', 'spiderman 3', 'rocky 1', 'rocky2')
list_cities = ['london','paris','birmingham','amsterdam']
if list_cities.index('paris') > 0:
    print('there is Paris in the list')
there is Paris in the list
list = [1,2,3,4]
list += list
list
[1, 2, 3, 4, 1, 2, 3, 4]
7.swap places

list = [1,2,3,4,5,6]
list[0],list[-1] = list[-1] , list[0]
list
[6, 2, 3, 4, 5, 1]
8

tuple = (1,2,3,4,5,6,7,8,9,10)
tuple[3:7]
(4, 5, 6, 7)
9

list_colours = ['blue','blue','red','red']
list_colours.count('blue')
2
10

tuple_animals = ('cat','leopard','lion','snake')
tuple_animals.index('lion')
2
11

tuple1= (1,2,3)
tuple2 = (4,5,6)
tuple3 = tuple1 + tuple2
tuple3
(1, 2, 3, 4, 5, 6)
12 lenth

list
tuple
print(len(list))
print(len(tuple))
6
10
13 tuple to list

my_tuple = (1,2,3,4)
my_list = list(my_tuple)
print(my_list)
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
Cell In[36], line 2
      1 my_tuple = (1,2,3,4)
----> 2 my_list = list(my_tuple)
      3 print(my_list)

TypeError: 'list' object is not callable
max and min in tuples

tuple = (1,2,3,4,5)
max_tuple = max(tuple)
min_tuple = min(tuple)
print(max_tuple)
print(min_tuple)
5
1
tuple1 = ('me','and','you')

a = (reversed(tuple1))
print(a)
