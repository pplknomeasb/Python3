Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
my_string = "this is my first string"
my_string
'this is my first string'
my_string =
SyntaxError: invalid syntax
my_string = 'this is my first string'
my_string
'this is my first string'
#triple quotes are used to instantiate a string that spans over multiple lines
my_string = '''this
is
my
first
string'''
my_string
'this\nis\nmy\nfirst\nstring'

#\n indicates that a break, a new row, and new line is being instantiated
my_string = '''this\
is\
my\
first\
string'''
my_string
'thisismyfirststring'


#Python uses indexes to mark a specific position in a sequence of elements
#The first index starts with index 0, then 1, then 2 and so on
#When counting from right to left, and first index will be minus 1

string1 = "Cisco Router"
string1 [0]
'C'
string1[2]
's'
string1[5]
' '

string1[-1]
'r'
string1[-4]
'u'

len (string1)
12
12
12
#The len function counts the length of the variable that is being measured

string1[11]
'r'
string1[20]
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    string1[20]
IndexError: string index out of range
