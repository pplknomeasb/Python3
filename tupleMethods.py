Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
tuple2 = (1, 2, 3, 4)


len(tuple2)
4

min(tuple2)
1
max(tuple2)
4


tuple2 + (5, 6, 7)
(1, 2, 3, 4, 5, 6, 7)

tuple2 *2
(1, 2, 3, 4, 1, 2, 3, 4)

#slising tuples

tuple2[0:2]
(1, 2)

tuple2[1:]
(2, 3, 4)

tuple2[:]
(1, 2, 3, 4)

tuple2[:-2]
(1, 2)

tuple2[-2:]
(3, 4)

tuple2[::-1]
(4, 3, 2, 1)

tuple2
(1, 2, 3, 4)

3 in tuple2
True

3 not in tuple2
False

5 in tuple2
False


del tuple2

tuple2
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    tuple2
NameError: name 'tuple2' is not defined. Did you mean: 'tuple'?

