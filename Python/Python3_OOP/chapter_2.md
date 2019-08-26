# Objects in python
**NOTE**: These notes will be useful if you have read the book atleast once.

## Simple class
Recommended indentation - 4 spaces.
```Python
# class name follows CamelCase (PEP8)
class SimpleClass:
  """
    This is python docstring, used for documenting.
    Follows indentation. This statement follows the ":".
    Docstrings enclosed within ''' or \"\"\", so that document can be formatted as multiline string
  """
  pass

simpleClass = SimpleClass()
print(simpleClass)
print(simpleClass.__class__.__name__)

# help using docstring
help(SimpleClass)
```

## Class with Attributes
**dot notation** - assign value to an objects's attribute.

```Python
class Point:
  pass

p1 = Point()
p1.x = 5
p1.y = 10
print(p1.x, p1.y)
```

## Class with method
Method requires one mandatory argument and conventionally named as **self**.

Missing the **self** argument causes **TypeError** to be thrown by the interpreter. 

**Never name a method with leading and trailing double underscores**

```Python
class Point:
  #  self is a required argument.
  def reset(self):
    self.x = 0
    self.y = 0

p1 = Point()
p1.x = 5
p1.y = 10
print(p1.x, p1.y)
# invocation using object
# python takes care of passing the object to the method
p1.reset()
print(p1.x, p1.y)

# method invocation using Class
Point.reset(p1)

```

## Constructor/initialization function
**constructor** function is named `__new__`, while initialization function is named `__init__`. 

Constructor function is called before object construction and accepts exactly one argument the **class name** and returns the created object. handy in metaprogramming.

```Python
class Point:
  def __init__(self, x = 0, y = 0):
    self.set(x, y)

  def set(self, x, y):
    self.x = x
    self.y = y
  
  def reset(self):
    self.set(0, 0)
```

## Modules
A python file is a module.
```Python
import module

# import specific class from a module
from module import Class

# import everythin inside a module to current namespace
# this is highly discouraged.
# imports everything defined in that module and all those names imoprted in to that module.
from module import *

# import multiple classes
from module import Class1, Class2

# import specific class with alias 
# so that there is no name collision
from module import Class as TestClass

```

## Organizing modules
Collection of modules in a folder is python package. Name of the folder is also the package's name.

By placing a file **__init__.py** a folder is recognized as package by python interpreter.

Modules can be imported using **absolute** and **relative** imports.

## Absolute imports
```Python
#  Consider the package, module hierarchy
# main.py
# package
#   module1
#   module2

# To import module1 inside main.py using absolute import, syntax is as follows.
# Assume module1 has a class Class1
# Syntax-1: not recommended
import package.module1
cl1Obj = package.module1.Class1()

# syntax 2
from package import module1
cl1Obj = module1.Class1()

# syntax 3
from package.module1 import Class1
cl1Obj = Class1()
```

## Relative imports
```Python
# package
#   module1
#   module2
# Import class1 inside module1 in to module2 using relative import
from .module1 import Class1

# preceding dot(.) stand for current package
# double dot(..) to refer to parent package of current module's package

```

**__init__.py** is used for defining variables, classes. Import only very frequently used ones in __init__.py
```Python
# package
#   module1
#   module2
# __init__.py
# to access a class Class1 in module1 as package.Class1
# following entry is placed in __init__.py
from .module1 import class1

# above declaration makes **Class1** accessible as package.Class1 instead of package.module1.Class1
```

## Organizing module contents
Module level code is executed when the module is imported. placing executable code in modules may slow the startup process.

Placing code inside function or a class would delay the code execution till the function is invoked or class is instantiated and method is invoked on it.

Every module has special(magic) variable `__name__`. When imported, this variable is set to the name of the module, while run as script, this variable is set to **__main__**

```Python
#python module code here
#.....

# conventionally named as **main** function
def main():
  # code that does something when this module alone is run like a script

# this way when this module gets imported,
# we can avoid any module level code execution.
if __name__ == "__main__":
  main()

```

Class can be defined inside a function, function can also be define inside another function. Those classes adn function won't be visible outside of the enclosing function.

## Access control
* All methods and attributes - public accessible. Forced guidelines, best practices. 

* Methods and atributes for internal use **prefixed with underscore** and described about the same in its docstings.

* Stringly enforce private method and attributes, prefix with **double underscores**. Python does name mangling on those methods and attributes, so that they just can't be accessed directly by outside objects using their name. The attribute/method name will be **_<classname><attr/methodname>**. Inside methods can access directly using the name(auto unmangling).

```Python
class Secret:
  def __init__(self, passwd):
    self.__passwd = passwd
  
  # class methods
  pass

secret = Secret('123456Hello')
# raises AttributeError
print(secret.__passwd)

# works fine
print(secret._Secret__passwd)

```

## pip, venv and 3rd part Python libraries
```Bash
# pip is the package manager
# doesnot ship with python by default
# ensurepip module installs pip
# use sudo to run as root on linux
[sudo] python -m ensurepip

# check if pip is installed
pip --version

# installing a package
# this installs the package to system python directory
# only system installers to install to system python directory
pip install "package_name"

# virtual python environment in working directory
cd working_dir
python -m venv env # env is the virtual environment name
source env/bin/activate

# after this pip command issued inside the directory will work on this directory only. won't install to system python directory.
```


---

## References:
* [Python3 Object oriented programming by Dusty Phillips](https://www.amazon.in/dp/B005O9OFWQ/ref=dp-kindle-redirect?_encoding=UTF8&btkr=1)