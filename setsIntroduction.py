Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#Sets are the same type as lists except with no duplicate elements

list4 = [1, 2, 3, 4, 5, 2, 3]
list4
[1, 2, 3, 4, 5, 2, 3]
set(list4)
{1, 2, 3, 4, 5}

set1 = set([11, 12, 13, 14, 15, 15, 15, 11])
set1
{11, 12, 13, 14, 15}
#Because sets do not allow duplicate data, it removes any occurance that happens more than once.  The original code has 8 indexes but because its a set and removes any duplicates, its now a 5 index set.

type(set1)
<class 'set'>

set2 = {11, 12, 13, 14, 15, 15, 15, 11}
type(set2)
<class 'set'>

len(set2)
5

11 in set2
True

10 in set2
False

10 not in set2
True

set2.add(16)
set2
{16, 11, 12, 13, 14, 15}

set2.remove(11)
set2
{16, 12, 13, 14, 15}

set2.add(16)
set2
{16, 12, 13, 14, 15}
set2.sort()
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    set2.sort()
AttributeError: 'set' object has no attribute 'sort'
set2.sort
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    set2.sort
AttributeError: 'set' object has no attribute 'sort'
sorted.set2()
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    sorted.set2()
AttributeError: 'builtin_function_or_method' object has no attribute 'set2'
sorted.set2
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    sorted.set2
AttributeError: 'builtin_function_or_method' object has no attribute 'set2'
sorted(set2)
[12, 13, 14, 15, 16]
