Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.


#Conversions

num = 2
f = 2.5

type(num)
<class 'int'>
type(f)
<class 'float'>

num2 = str(num)
num2
'2'

type(num2)
<class 'str'>
f2 = str(f)
f2
'2.5'

type(f2)
<class 'str'>

str = "5"
type(str)
<class 'str'>


in1 = int(str)
type(in1)
<class 'int'>


floater1 = float(str)
type(floater1)
<class 'float'>


num1 = 2
f = float(num1)
type(f)
<class 'float'>


f1 = int(f)



tup1 = (1, 2, 3)
list1 = list(tup1)


tup = tuple(list1)


list1
[1, 2, 3]

set1 = set(list1)




num = 10
num_bin = bin(num)
num_bin
'0b1010'


num_hex = hex(num)
num_hex
'0xa'




bin_to_num = int(num_bin, 2)
bin_to_num
10

hex_to_num = int(num_hex, 16)
hex_to_num
10

#Converting a binary to a number must always have a base of 2.  Converting a hex to a number always has a base of 16