Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#Tuples introduction.  First out of scope.

#Tuples are immutable lists.  Contents cannot be added, removed, or changed.  Allows data to be stored in a sequence while remaining untouchable.  Tuples are organized lists that can store duplicate data.  Tuples are enclosed by parenthesis and separated by commas

mytuple = ()
type(mytuple)
<class 'tuple'>

#If the tuple contains one element, a comma must follow the element or it will not be regarded as a tuple

mytuple=(9)
type(mytuple)
<class 'int'>
mytuple=(9,)
type(mytuple)
<class 'tuple'>

#To access an element within a tuple, indexing is used

mytyple(0)
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    mytyple(0)
NameError: name 'mytyple' is not defined. Did you mean: 'mytuple'?
mytuple[0]
9

mytuple =(1, 2, 3, 4, 5)
mytuple[0]
1
mytuple[1]
2
mytuple[2]
3
3
3
mytuple[-1]
5

#elements of the tuple cannot be changed

mytuple[1] = 10
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    mytuple[1] = 10
TypeError: 'tuple' object does not support item assignment
#tuple does not support adding removing or changing of its elements


tuple1=("Cisco", "2600", "12.4")
(cendor, model, ios) = tuple1
cendor
'Cisco'
model
'2600'
ios
'12.4'

tuple2 = (1, 2, 3, 4)
(x, y, z) = tuple2
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    (x, y, z) = tuple2
ValueError: too many values to unpack (expected 3)

(a, b, c) = (10, 20, 30)
a
10
b
20
c
30


type(a)
<class 'int'>
type(x)
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    type(x)
NameError: name 'x' is not defined
type(cendor)
<class 'str'>
type(tuple2)
<class 'tuple'>


#Tuples are lists that are not mutable(immutable.)  Their type is 'tuple.'  The variable types used for each index is chosen when index values are set.  Does the floating numbers and integer numbers need quotes?

newTuple = ("Brennan", 12, 5.4)
type(newTuple)
<class 'tuple'>
(name, age, weight) = newTuple
type(age)
<class 'int'>
type(weight)
<class 'float'>
<class 'float'>
SyntaxError: invalid syntax
newTuple = ("brennan", "12", "5.4")
(name, age, weight) = newTuple
type(age)
<class 'str'>

#When enclosing all the data inside of quotation marks, it will always remain string and problems are ahead.