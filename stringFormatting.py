Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#Concantenation is taking 2 or more different strings and combining them into one.

x = "Cisco"
y = " Switch"
x + y
'Cisco Switch'

#The concantenation is complte


x * 3
'CiscoCiscoCisco'


#Searching through a string to indicate if a specific character, number, or set of characters occur can be done using the in function.
"o" in x
True


"b" in x
False

"b" not in x
True


"Cisco model: %s, %d WAN slots, IOS %f" % ("2600XM", 2, 12.4)
'Cisco model: 2600XM, 2 WAN slots, IOS 12.400000'


#Keeping a constant string template and changing the data within that string allows the user to output the same string but changing particular characteristics within the string.  %s calls for string input, %d calls for double input, %f calls for floating input and should be configured to eliminate any zero's towards the end of the floating number.

"Cisco model: %s, %d WAN slots, IOS %f" % ("2600XM", 2, 12.5)
'Cisco model: 2600XM, 2 WAN slots, IOS 12.500000'
#The  % sign must be placed between the function and the data being called by the function

#The floting number can be altered to only show a particular number of digits after the period position.
"Cisco model: %s, %d WAN slots, IOS %.2f" % ("2600XM", 2, 12.4)
'Cisco model: 2600XM, 2 WAN slots, IOS 12.40'
"Cisco model: %s, %d WAN slots, IOS %.1f" % ("2600XM", 2, 12.4)
'Cisco model: 2600XM, 2 WAN slots, IOS 12.4'
"Cisco model: %s, %d WAN slots, IOS %.f" % ("2600XM", 2, 12.4)
'Cisco model: 2600XM, 2 WAN slots, IOS 12'



#There are multiple ways of formatting.  In the following, the %s, %d, and %f are replaced with curly braces.  The % character that separated the methos from the parameters is replaced with .format.  Each open and close brace is matched with the parameters after.format.
"Cisco model: {}, {} WAN slots, IOS {}".format("2600XM", 2, 12.4)
'Cisco model: 2600XM, 2 WAN slots, IOS 12.4'



#Indexing can be used with the same type of formatting.  Inside the parenthesis is the parameter position to be called when putting the string together.
"Cisco model: {1}, {2} WAN slots, IOS {3}".format("2600XM", 2, 12.4)
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    "Cisco model: {1}, {2} WAN slots, IOS {3}".format("2600XM", 2, 12.4)
IndexError: Replacement index 3 out of range for positional args tuple
"Cisco model: {0}, {1} WAN slots, IOS {2}".format("2600XM", 2, 12.4)
'Cisco model: 2600XM, 2 WAN slots, IOS 12.4'
"Cisco model: {1}, {0} WAN slots, IOS {2}".format("2600XM", 2, 12.4)
'Cisco model: 2, 2600XM WAN slots, IOS 12.4'
"Cisco model: {1}, {1} WAN slots, IOS {1}".format("2600XM", 2, 12.4)
'Cisco model: 2, 2 WAN slots, IOS 2'
