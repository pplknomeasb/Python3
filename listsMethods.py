Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#tools provided to assist with list altering

lists2 = [-11, 2, 12]
min(list2)
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    min(list2)
NameError: name 'list2' is not defined. Did you mean: 'lists2'?
list2 = [-11, 2, 12]
min(list2)
-11
max(list2)
12
list3 = ["a", "b", "c"]
min(list3)
'a'
max(list3)
'c'

list1 = ["Cisco", "Juniper", "Avaya", 10, 10.5, -11]
max(list1)
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    max(list1)
TypeError: '>' not supported between instances of 'int' and 'str'

#comparisons like min and max cannot be used within a list that has multiple variable types within it.

list1
['Cisco', 'Juniper', 'Avaya', 10, 10.5, -11]
list1.append(100)
list1
['Cisco', 'Juniper', 'Avaya', 10, 10.5, -11, 100]

#Append allows you to add data to a list set

del list1[4]
list1
['Cisco', 'Juniper', 'Avaya', 10, -11, 100]
#del allows you to remove data from a list using the position number in the list

list1.pop(0)
'Cisco'
list1
['Juniper', 'Avaya', 10, -11, 100]
#[LIST].pop(index#) will remove from the list as well

list1.remove("Juniper")
list1.
SyntaxError: invalid syntax
list1
['Avaya', 10, -11, 100]
#The [LIST].remove method searches for the characters in the list by passing through the parameters of the method and removes it.

list1.insert(2, "Nortel")
list1
['Avaya', 10, 'Nortel', -11, 100]
#[LIST].insert inserts the data passed within the method and adds it to the list at the position indexed.


#Combinding lists together can be used using the extend moethod.

list1
['Avaya', 10, 'Nortel', -11, 100]
list2
[-11, 2, 12]
list1.extend(list2)
list1
['Avaya', 10, 'Nortel', -11, 100, -11, 2, 12]

list1.index(-11)
3

list1.append(10)
list1
['Avaya', 10, 'Nortel', -11, 100, -11, 2, 12, 10]
list1.count(10)
2

#Here we added 10 to the list increasing the number of times 10 occurs in the list.  count method was to count the number of times 10 occurs which it returns 2.

list2
[-11, 2, 12]

list2.append(1)
list2.append(25)
list2.append(500)
list2
[-11, 2, 12, 1, 25, 500]
list2.sort()
list2
[-11, 1, 2, 12, 25, 500]

list2.reverse()
list2
[500, 25, 12, 2, 1, -11]

#.sort sorts the list in ascending order.  .reverse sorts the list in descending order.

sorted(list2)
[-11, 1, 2, 12, 25, 500]


sorted(list2, reverse = True)
[500, 25, 12, 2, 1, -11]

help(sorted)
Help on built-in function sorted in module builtins:

sorted(iterable, /, *, key=None, reverse=False)
    Return a new list containing all items from the iterable in ascending order.
    
    A custom key function can be supplied to customize the sort order, and the
    reverse flag can be set to request the result in descending order.

list1+list2
['Avaya', 10, 'Nortel', -11, 100, -11, 2, 12, 10, 500, 25, 12, 2, 1, -11]
list2*3
[500, 25, 12, 2, 1, -11, 500, 25, 12, 2, 1, -11, 500, 25, 12, 2, 1, -11]
