# Executable files and organization

## Python scripting
Default is UTF-8 encoding.

```Python
# adding the below statement to beginning of python scripts in unix based systems
#! /usr/bin/env python

# or 

#! /usr/bin/python

# If system contains multiple python versions
#! /usr/bin/env python3

# or 

#! /usr/bin/python3
```
Pythonic - programming approaches idiomatic to python

## Python script structure
More on style guide can be found in the references.
```Python
#! /usr/bin/python3

"""
  Doc string explaining about the script 
"""
# version, author information
__version__ = 0.1
__date__ = "10-07-2019"
__maintainer__ = "user@example.com"

# import statements
# standard library imports first
import re
import random

# third party imports

# local application specific imports

# globals and constants

# class, function declarations

# use spaces instead of tabs and use 4 spaces
```

## Importing modules
```Python
# import  a module
# Syntax: import <modulename>
import sys

# functions, objects inside module accessed using the dot notation
for arg in sys.argv:
  print(arg)

# argv[0] contains the path to the python script itself

# import specific objects from a module
# Syntax: from <module_name> import <object>
# once imported explicitly, the object can be accessed directly. But this is undesirable since there could be name collision resulting due to imports from various module.
from sys import argv
print(argv[0])

# providing a custom name to imported object
from sys import argv as arguments

```

## Using exec() and eval()
Both are built-in functions. Use these with caution (security issues).
`exec(string)` - execute arbitrary strings as python statements
`eval(string)` - evaluate a python statement. example conditional expressions

```Python
# using exec
fruits = ["Apple", "Orange", "Mango"]
code = "for fruit in fruits: print(fruit)"
exec(code)

# using eval
value = eval(input("Enter a number:"))
print(eval("value > 100"))
```

---

## References:

* [Python3 for absolute beginners](https://www.amazon.in/Python-Absolute-Beginners-Tim-Hall/dp/1430216328)
* [Python Style guide](https://www.python.org/dev/peps/pep-0008/)
* [Python naming conventions](https://medium.com/@dasagrivamanu/python-naming-conventions-the-10-points-you-should-know-149a9aa9f8c7)
* [realPython style guide notes on PEP(Python Enhancement Proposal)8](https://realpython.com/python-pep8/)