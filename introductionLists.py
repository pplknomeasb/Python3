Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#A list is a sequence consisting of elements separated by comma and inclosed by square brackets and can have any data type.  A list may have any number of elements.  Lists are indexed and each element has a specific index in the list.  Lists are mutable.

list1 = [] #instantiating an empty list
type(list1)
<class 'list'>

list1=["Cisco", "Juniper", "avaya", 10, 10.5, -11]
len(list1)
6
list1[0]
'Cisco'
list1[1]
'Juniper'
list1[-1]
-11
list1[-2]
10.5
list1[100]
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    list1[100]
IndexError: list index out of range
list1
['Cisco', 'Juniper', 'avaya', 10, 10.5, -11]
list1[2]
'avaya'
list1[2]="HP"
list1[2]
'HP'
#Changing the element of a list.  All lists are mutable, the first index is always position 0.