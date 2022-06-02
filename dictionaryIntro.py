Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.


#Dictionary-  unordered set of key value pairs separated by commas and enclosed in curley braces.  Way of storing data to be modified.

#No indexing by numbers but by keys which is to the left side of the colon.
#Vendor: Cisco, Model: 2600, IOS: 12.4, Ports:4 is the information specific for a router.  The Vendor would be used as the key which in turn I believe has to be unique.

dict1 = {}
type(dict1)
<class 'dict'>

dict1 = {"Vendor": "Cisco", "Model": "2600", "IOS": "12.4", "Ports": "4"}
d1 = {1: "First Element", 2: "Second Element"}

dict1
{'Vendor': 'Cisco', 'Model': '2600', 'IOS': '12.4', 'Ports': '4'}

#unique value pairs.  Would be rare to have the same valued pairs in an entire dictionary so make sure we reduce redundancies in the future.

#Dictionaries are completely mutable.  The valued pairs contents can be changed after initialization, keys added, and keys deleted.  
