Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#Formatting using f-strings also called formatted string literals

#Ways to embed variables and expressions inside strings

"Cisco model: {2}, {1} WAN slots, IOS {2}".format("2600XM", 2, 12.4)
'Cisco model: 12.4, 2 WAN slots, IOS 12.4'

model = '2600XM'
slots = 4
ios = 12.3

f"Cisco model: {model}, {slots} WAN slots, IOS {ios}"
'Cisco model: 2600XM, 4 WAN slots, IOS 12.3'

#The format method is called using lowercase f for the f string at the beginning of the sequence.  Inside the curly braces are the variables that were instantiated prior to calling for the output.  We can also add an expression to the variable name.  The expression itself is added with the variable in the curly braces.

f"Cisco model: {model}, {slots * 2} WAN slots, IOS {ios}"
'Cisco model: 2600XM, 8 WAN slots, IOS 12.3'

#we now have an expression multiplier added to the slots to be multiplied by 2 before establishing the output.

f"Cisco model: {model.lower}, {slots * 2} WAN slots, IOS {ios}"
'Cisco model: <built-in method lower of str object at 0x000001AB85415E30>, 8 WAN slots, IOS 12.3'
f"Cisco model: {model.lower()}, {slots * 2} WAN slots, IOS {ios}"
'Cisco model: 2600xm, 8 WAN slots, IOS 12.3'

#Here the lower expression is added to the model number.  The number is not altered but the lettering from uppercase is changed to lowercase.  