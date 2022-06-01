Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
set1 = {1, 2, 3, 5}
set2 = {3, 5, 8}

set1.intersection(set2)
{3, 5}
 set1 ={1, 2, 3, 4}
 
SyntaxError: unexpected indent
set1 = {1, 2, 3, 4}

set1. intersection(set2)
{3}

#intersection allows 2 sets to be compared and the results are the indexes that match one another between the 2.

set2.intersection(set1)
{3}

set1.difference(set2)
{1, 2, 4}
set2.difference(set1)
{8, 5}

set1.union(set2)
{1, 2, 3, 4, 5, 8}

set1
{1, 2, 3, 4}
set1.pop()
1
set1
{2, 3, 4}

set1.clear()
set1
set()

