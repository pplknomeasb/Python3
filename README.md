# Python3
Will be taking on a Python 3 course created by stakskills.com.  

Upload one.  Learned how to use Python's IDE.  If one isn't capable of using the IDE, one is capable of using any notepad type program.  The file itself has to be saved in a .py format in order for Python to correctly execute the program.  For now, to run the program I open the cmd line and execute 'python D:\Python3\fileName.py' and the program within the file will run.  If any part of your directory has open spaces in the file's name or the program name, the file name has to be in double quotes like so; "D:\Python3\fileName.py".

Upload userInput.  The reason behind a program is to execute commands in order to give the end user a specific set of results.  The userInput program displays a command to the user to input a specif string.  The string set that the user inputs is stored in a variable named user_says.  Once the operation is executed, the variable user_says is called once more using the print operation and the string data is printed on the command line.

Upload variableDeclarations.  Declaring variables types in Python is done behind the scenes of Python.  my_var = 10; my_var becomes an integar type.  my_var = "hello"; my_var becomes a string type.  my_var = True; my_var becomes a boolean type.  a = b = c = 10; a, b, and c are all integar variables with a value of 10.  a, b, c = 1, 2, 3; a = 1 b = 2 c = 3.  The value's declared to the variables are stored within the program and will have a value reference to ensure speed.

#strings, numbers, booleans, lists, sets frozensets, tuples, ranges, dictionaries, none are built in datatypes
#mutability = can be modified after creation
#immutability = cannot be modified after creation


Chapter Strings
Formatting the output is crucial for communicating the information that is wanted by the end user.  The output that is generated can at times include information that isn't necessary to display everything, we have to utilize the mothods and operators in order display only what is appropriate to the user.  In the chapter of strings, we learned indexing rules, formatting upper and lowercase strings, deliminaters, strip, replace, split, join, and splicing.

Lists
Lists are capable of holding all datatypes and is mutable.  Lists are a way to organize data that have common characterists.  Lists come with methods like min and max which returns the lowest and largest values; these methods can be used on strings but neither method can be used if the list has multiple variable types.  .append allows you to add to the list and you can designate what position to add it in.  del allows you to delete from a list at a certain position or a specific character set; .pop and .remove gives the same results.  .count allows you to search for a specific element and it'll return the number of times that element occurs in the list.  .sort sorts the list of elements in ascending order and .reverse sorts the list elements in descending order.  sorted sorts the list in ascending order and creates a new list.  sorted(list, reverse = True) sorts the list in decending order and creates a new list.  .extend and list1+list2 concantenates the lists together.


Sets.  Sets are an unordered collection of unique elements.  No elemenets in a set can duplicate.  If it is instantiated to have multiple data sets that are similar, it'll remove all elements that are not unique.  You are able to see if there is specific data by using the in and not in methods to have a boolean result returned.  Sets are mutable; .add, .remove, .pop can all be used with sets.  FrozenSets are immutable so there is no ability to add too, remove from, or altering the data within the set.  The methods that you can use with frozen sets are .intersection, .difference, .union, .pop, and .clear.


Tuples are immutable organized lists that can contain duplicate data; however data cannot be added, removed, or changed within tuples.  A Tuple can contain as little as one data piece, but during delcaration a comma must be placed after the first data piece or the data will not be declared as a tuple.  The same indexing and slicing rules apply as for strings and lists.  Numbers in general should not be placed within quotes unless a particular type of edit will be required in order for Python to recognize integars and floats as they are.  


Ranges are instantiated like lists, however, the same rules do not apply.  Ranges cannot be sliced.  A range can be converted to a list in order for it to be sliced.


Dictionaries.  Dictionaries are an unordered set of key-value pairs.  They will be displayed in the output line in the order that the contents are intitiated within the dictionary.  dict1 = {} creates an empty dictionary.  dict1 = {"One": "1", ""Two": "2"} creates a dictionary with two key-value pairs.  Dictionaries are mutable i.e. contents can be added, removed, and altered after the ditionaries initialization.  Dictionaries have 3 methods.  dict.keys() which returns all the keys in the dictionary, dict.values() which returns all of the values within the dictionary, and dict.items() which returns all of the keys and values as a tuple.  

Conversions between data types.  str() converts to a string.  int() converts to integer.  float() converts to float.  list() converts to a list.  tuple() converts to tuple.  set() converts to set.  bin() converts to binary representation.  hex() converts to a hexadecimal representation.  int(variable, 2) converts binary back to decimal.  int(variable, 16) converts from hexadecimal back to decimal.
