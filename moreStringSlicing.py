Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

mystring="0123456789"
mystring[0]
'0'
mystring[1]
'1'
mystring[2]
'2'

# mystring[start: stop: step]

# mystring[start: stop: step] you can have the start index without the stop and step. can have the stop without start and step.  step can be without start and stop.

#Using a slice to return only the even numbers in a string.
mystring[::2]
'02468'

#Using a slice to return only the odd numbers in a string.
mystring[1::2]
'13579'

#using a slice to return only odd numbers that are less than 7
mystring[1:7:2]
'135'

