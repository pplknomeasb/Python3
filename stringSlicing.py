Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#name of variable pointing to the string followed by square brackets.  collon to right of first number.
mystring[10:15]
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    mystring[10:15]
NameError: name 'mystring' is not defined
mystring [10: 15]
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    mystring [10: 15]
NameError: name 'mystring' is not defined
string1 = "O E2 10.110.8.9 [160/5] via 10.119.254.6, 0:01:00, Ethernet2"
string1[5:15]
'10.110.8.9'


#string1 includes a few data pieces and the IP address being one of them.  We are wanting to slice out the index that includes the IP address.  string1 is declared and now we're wanting to extract a particular piece of data.  The square brackets inclose the parameters that the wanted data is a part of which is the first IP address.

string1[5:]
'10.110.8.9 [160/5] via 10.119.254.6, 0:01:00, Ethernet2'
#IF the second parameter is left blank then the string to be returned will start with the parameter given and it will return the entire string starting at the index within the string.

string1[:5]
'O E2 '
#If the first parameter is left blank and only the second parameter is given then the string that will be returned will start at index 0 and end with the index given in the code.


string1[-1]
'2'
string1[-2]
't'
#Slicing using negative indexes start at the right most part of the string.  Negative 1 is the right most character and -2 is one place to the right from the end of the string.

string[-9:-1]
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    string[-9:-1]
NameError: name 'string' is not defined. Did you mean: 'string1'?
string1[-9:-1]
'Ethernet'
string1[-5:]
'rnet2'
string[:-5]
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    string[:-5]
NameError: name 'string' is not defined. Did you mean: 'string1'?
string1[:-5]
'O E2 10.110.8.9 [160/5] via 10.119.254.6, 0:01:00, Ethe'
string1[::2]
'OE 01089[6/]va1.1.5.,00:0 tent'
'OE 01089[6/]va1.1.5.,00:0 tent'
'OE 01089[6/]va1.1.5.,00:0 tent'

#If one wants to slice and return every other character in a string, [::#]  The # will be the number of characters that that will be missed in between each string print command.
string1[::5]
'O10 /i.2,1 r'


string1[::-1]
'2tenrehtE ,00:10:0 ,6.452.911.01 aiv ]5/061[ 9.8.011.01 2E O'
'2tenrehtE ,00:10:0 ,6.452.911.01 aiv ]5/061[ 9.8.011.01 2E O'
'2tenrehtE ,00:10:0 ,6.452.911.01 aiv ]5/061[ 9.8.011.01 2E O'
#Using the previous command allows you to pring the string in reverse order