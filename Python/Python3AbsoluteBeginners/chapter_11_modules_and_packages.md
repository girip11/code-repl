# Modules and Packages
A python file is a module. It can contain methods, classes etc

## Using modules
```Python
# import module_name
# from module_name import *

# access names in the re module with re followed by the dot operator and then the name. Importing this was helps avoid any name collision in the current namespace.
import re

# imports all the methods, classes to the current namespace, so that the names can be called directly.
from random import *

```

A module can be imported at any point in the code. But all import `from module_name import *` can only be imported in the main body of the program. Using this wildcard import inside a method cause syntax error.

```Python
import re as regex
regex = __import__(re)

# info on __import__
help(__import__)

# runtime module import
module_name = 'random'
random_gen = __import__(module_name)
```

## Structuring modules
Good practice to have all the imports at the top. Important variables follow the module imports.
Module variables with leading underscore are treated internal to the module and are not imported to other modules when using wildcard import `from module import *`. But **explicit import is allowed**.


## __name__ variable
Used when module is executed on its own.

```Python
# module variables

# module methods

# module classes etc

# condition is True when the module is executed on its own
if __name__ == "__main__"
  # module execution code
```

## Reload module changes dynamically
using the python module **imp**. Module reloads are **additive**. For instance, add a method, rename the method, after the module reloads we will find both the methods available.
```Python
import my_module
import imp

# after changes in my_module
imp.reload(my_module) # reload the changed module.
```

## Finding module
* Module is searched in the current directory, followed by the directories specified in the **PYTHONPATH** and then the python standard library directories. Any name collision between custom module and standard library module would be a problem in that case.

* Module compiled to byte code and saved in **.pyc** file to avoid recompilation. Bytecode is platform independent.

## Python Packages
* top level directories and subdirectories inside
* **.py** files in the directory hierarchy
* **__init__.py** file in each directory in the package.
* When a package gets imported, **__init__.py**
 gets executed. **__init__.py** is a normal python file that can contain usual python constructs like class, conditional constructs etc.

## Importing modules from package
```Python
from package import module

# or

import package.module

# to know what modules from a package has been imported
dir(package)

```

## All module import from package
```Python
# the below changes need to be made in the __init__.py for importing all modules or importing everything inside a module.

# __init__.py
# import the below modules when the package gets imported
import module1, module2

# importing with the wildcard form
__all__ = ["module1"]

# above changes can be tested with 
# import package
# dir(package)
```

## Python packages
* standard modules - standard library is on **sys.path**.
* Contributed packages - packages at **Python Package Index**. Can use tools like **pip**.


---

## References:
* [Python3 for absolute beginners](https://www.amazon.in/Python-Absolute-Beginners-Tim-Hall/dp/1430216328)