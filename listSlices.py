Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#String slicing and List slicing are similar

var1[5:10] #instantiating the slice of var1 to start at the 5th index and go as far but not including the 10th index.
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    var1[5:10] #instantiating the slice of var1 to start at the 5th index and go as far but not including the 10th index.
NameError: name 'var1' is not defined. Did you mean: 'vars'?
#or nah

list3 = [1, 2, 3, "a", "b", "c"]
list3
[1, 2, 3, 'a', 'b', 'c']

#extracting the first 3 elements of the list
list3[0:3]
[1, 2, 3]

lists3[:3]
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    lists3[:3]
NameError: name 'lists3' is not defined. Did you mean: 'list3'?
list3[:3]
[1, 2, 3]


#Slicing contents of a list that start in the middle

list3[2:5]
[3, 'a', 'b']
list3[2:]
[3, 'a', 'b', 'c']
list3[:]
[1, 2, 3, 'a', 'b', 'c']
list3[-1]
'c'
list3[-2]
'b'
list3[-4:-1]
[3, 'a', 'b']


list3[-3:]
['a', 'b', 'c']

list3[:-3]
[1, 2, 3]

list3[::2]
[1, 3, 'b']
list3[::-1]
['c', 'b', 'a', 3, 2, 1]
