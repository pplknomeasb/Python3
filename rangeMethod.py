Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

#Range datatype

r = range(10)
r
range(0, 10)
type(r)
<class 'range'>

list(r)
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

type(list)
<class 'type'>
type(r)
<class 'range'>
a=list(r)
type(a)
<class 'list'>
len(a)
10

#lists can be created from a range

r[0]
0
r[-9]
1
10 in r
False
7 not in r
False
7 in r
True
r.index(4)
4

list(r)[2:5]
[2, 3, 4]
#SLICE WITHOUT DEVELOPING ANOTHER VARIABLE 