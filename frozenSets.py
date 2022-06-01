Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
list1 = [1, 2, 3, 4]
list2 = [3, 4, 7]

fs1 = frozenset(list1)
fs2 = frozenset(list2)

fs1
frozenset({1, 2, 3, 4})
fs2
frozenset({3, 4, 7})
type(fs1)
<class 'frozenset'>
fs1.add(10)
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    fs1.add(10)
AttributeError: 'frozenset' object has no attribute 'add'

#Frozen sets are immutable.

fs1.remove(1)
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    fs1.remove(1)
AttributeError: 'frozenset' object has no attribute 'remove'

#Frozenset has no add or removing attributes

fs1.intersection(fs2)
frozenset({3, 4})
fs1.difference(fs2)
frozenset({1, 2})

fs1.union(fs2)
frozenset({1, 2, 3, 4, 7})
