Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

#Exploring further into dictionarys

dict1 = {"Vendor": "Cisco", "Model": "2600", "IOS": "12.4", "Ports": "4"}
dict1
{'Vendor': 'Cisco', 'Model': '2600', 'IOS': '12.4', 'Ports': '4'}

dict1["IOS"]
'12.4'

dict1["Vendor", "Model"]
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    dict1["Vendor", "Model"]
KeyError: ('Vendor', 'Model')
dict1["Vendor" and "Model"]
'2600'

#Dictionaries are

dict1
{'Vendor': 'Cisco', 'Model': '2600', 'IOS': '12.4', 'Ports': '4'}

dict1["RAM"] = "128"
dict1
{'Vendor': 'Cisco', 'Model': '2600', 'IOS': '12.4', 'Ports': '4', 'RAM': '128'}
dict1["IOS"] = "6970"
dict1
{'Vendor': 'Cisco', 'Model': '2600', 'IOS': '6970', 'Ports': '4', 'RAM': '128'}

del dict1["Ports"]


dict1
{'Vendor': 'Cisco', 'Model': '2600', 'IOS': '6970', 'RAM': '128'}


len dict1
SyntaxError: invalid syntax
len(dict1)
4

"IOS" in dict1
True

"IOS2" not in dict1
True

dict1.keys
<built-in method keys of dict object at 0x000001C9CEAD96C0>

dict1.keys()
dict_keys(['Vendor', 'Model', 'IOS', 'RAM'])

#dict1.keys vs dict1.keys().  .keys references a place in memory for the dictionary.  .keys() references a methos to return the keys within the dictionary.

dict1.values()
dict_values(['Cisco', '2600', '6970', '128'])

# .values() returns all of the values within the dictionary



# .items() method returns a list of tuples with each dictionary pair

dict1.items()
dict_items([('Vendor', 'Cisco'), ('Model', '2600'), ('IOS', '6970'), ('RAM', '128')])



type(dict1.keys())
<class 'dict_keys'>

type(dict1.values())
<class 'dict_values'>

list(dict1.keys())
['Vendor', 'Model', 'IOS', 'RAM']

list(dict1.values())
['Cisco', '2600', '6970', '128']

list(dict1.tuples())
Traceback (most recent call last):
  File "<pyshell#59>", line 1, in <module>
    list(dict1.tuples())
AttributeError: 'dict' object has no attribute 'tuples'
list(dict1.items())
[('Vendor', 'Cisco'), ('Model', '2600'), ('IOS', '6970'), ('RAM', '128')]
[('Vendor', 'Cisco'), ('Model', '2600'), ('IOS', '6970'), ('RAM', '128')]
[('Vendor', 'Cisco'), ('Model', '2600'), ('IOS', '6970'), ('RAM', '128')]



dict2 = {"dOfWeek": "Thursday", "tOfDay": "Noon", "wHappening": "Nothing", "hungry?": "69"}

type(dict2)
<class 'dict'>

dict2.items()
dict_items([('dOfWeek', 'Thursday'), ('tOfDay', 'Noon'), ('wHappening', 'Nothing'), ('hungry?', '69')])
dict2.values()
dict_values(['Thursday', 'Noon', 'Nothing', '69'])
dict2.keys()
dict_keys(['dOfWeek', 'tOfDay', 'wHappening', 'hungry?'])

list(dict2.items()) = a
SyntaxError: cannot assign to function call here. Maybe you meant '==' instead of '='?
list(dict2.items()) == a
Traceback (most recent call last):
  File "<pyshell#73>", line 1, in <module>
    list(dict2.items()) == a
NameError: name 'a' is not defined
a()
Traceback (most recent call last):
  File "<pyshell#74>", line 1, in <module>
    a()
NameError: name 'a' is not defined
