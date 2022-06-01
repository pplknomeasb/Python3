Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
a = "Cisco Switch"
a.index("i")
1
#We were wanting to find out the position of the first i that the program picked up on and it is in the 1 index position

#The syntax of count will count the amount of times a character is used in a string set

a.count("i")
2
 #we have i 2 times in our string which is correct

#find directs the program to search for a specific string sequence and it will return the index where that sequence begins

a.find
<built-in method find of str object at 0x000002A54DA15BF0>
a.find("sco")
2
#this is correct because the s begins at the 2 index.  If the index never occurs then python will return the result negative 1 or -1

a.find("cs0
       
SyntaxError: unterminated string literal (detected at line 1)
a.find("cso")
       
-1


#The lower and upper functions allow the string to be changed to all lowercase or all uppercase
       
a.lower()
       
'cisco switch'
a.upper()
       
'CISCO SWITCH'

#The original string a has not been changed from its original instantiation.  The functions give a particular output without changing the original variable.
       
a
       
'Cisco Switch'


#startswith and endswith are boolean functions that measures the parameters against the string  to return a true or false result
       
a.startswith("C")
       
True
True
       
True
a.endswith("h")
       
True
a.endswith(q)
       
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    a.endswith(q)
NameError: name 'q' is not defined
a.endswith("q")
       
False

b = "   Cisco Switch    "
       
#Strip is a function that removes the white spaces from the beginning and the end of a string
       
b.strip()
       
'Cisco Switch'


#Strip allows one to search for particular characters to be removed
       
c="$$$Cisco Switch$$$"
       
c.strip{"$")
       
SyntaxError: closing parenthesis ')' does not match opening parenthesis '{'
SyntaxError: closing parenthesis ')' does not match opening parenthesis '{'
       
SyntaxError: invalid syntax
c.strip("$")
       
'Cisco Switch'


#Replace is a function that searches for a particular character and replaces it with another character that are instantiated in the parameters of the function.  It will remove the white spaces at the beginning and the end as well as the spaces that occur throughout the entire string
       
b
       
'   Cisco Switch    '
b.replace(" ", "")
       
'CiscoSwitch'
#all of the spaces are removed
       


#The split method splits a string into a substring
       
d = "Cisco, Juniper, HP< Avaya, Nortel"
       
#The string uses commas as the delimiter or as a separater of distinct values
       
d = "Cisco, Juniper, HP, Avaya, Nortel:
       
SyntaxError: unterminated string literal (detected at line 1)
d = "Cisco, Juniper, HP, Avaya, Nortel"
       
d.split(",")
       
['Cisco', ' Juniper', ' HP', ' Avaya', ' Nortel']



#The Join method allows one to add to a string for the user to have more control over the output
       

"_".join(a)
       
'C_i_s_c_o_ _S_w_i_t_c_h'
#the type of delimiter that is used is first placed inside of the quotes and a dot is then used to call the join method.  Inside of the parenthesis is the variable.  An underscore is placed in between all of the characters include the space that separates cisco and switch.