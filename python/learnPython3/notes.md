# Notes
* Chapterwise notes from the book **Learn to code in python3**

## Chapter 1

* Python is interpreted language. Statement by statement interpreted.
* Group of statements form a block. Method/function comprises of blocks.
* Indentation very important for interpreter to identify tokens.
* No tab or whitespace before the beginning of a statement.

## Chapter 2

Identifier naming rules
* Identifier names case sensitive
* Start with either alphabets(lower and upper case) or underscore
* remaining characters can contain only alphabets, digits or underscore
* reserved words cannot be used as identifiers.
* `print` for console output and `input` for console input.
* `print('messsage', end='')` prints the message to console and ends with empty string. By default print method ends the string with new line.
* All reserved keywords are small case except the keywords **True** and **False**.
* Type conversions
  ```Python
    # Converts to int
    int('1')

    float('1.234')

    # eval converts input to appropriate type
    # if we pass a string to eval and if the value is 4
    # type is returned as int, if the value is 4.3 then the
    # type of the returned variable is float.
    x = '1'
    # prints int
    print(type(eval(x))

    x = '1.0'
    # prints float
    print(type(eval(x))

    x = '12xf
    # Error
    print(type(eval(x)))
  ```

## Chapter 3
* The operators are 
    - '+' addition
    - '-' subtraction
    - '*' multiplication
    - '/' floating point division. Returns the quotient of the division as a floating point
    - '//' Integer division. returns quotient of the division as integer.
    - '%' Modulus - returns the remainder of division
    - '\*\*' exponent operator __a \*\* b__ is interpreted as 'b' times 'a' or 'a' to the power of 'b'
    - unary '+' and '-'
* unary operators have higher precedence than binary operators and unary operators are right associative.
* Operator precednce - PEDMAS
    `P(paranthesis)E(Exponent)D(/, // and %)M(multiplication)A(addition)S(subtraction)`
* Division and multiplication same precedence and addition and subtraction in same precedence.
* All the binary operators are left associative except the assignment operator which is right associative.
* Chained assignment 
```Python
# Right most expression executed first
a = b = c = d
```
* Arithmetic shorthand operators
  ```Python
    x *= 5 # same as x = x * 5 
  ```

## Chapter 4 - Conditional expresssions
if syntax
```Python
# if block
if condition:
    block

# if else
if condition:
  block
else:
  block

# if else if else block
if condition:
  block
elif condition:
  block
else
  block

# conditional expression
exp1 if condition else expr2

# example
result = (5 * 10) if eval(input('Enter number')) > 0 else 0
```

* **and**, **or** and **not** are the logical operators in python. While `**and,  or**` operators are binary, **not** is unary operator.

## Chapter 5
Iteration syntax:
```Python
# while loop
while condition:
  block

# for loop
for loop_var in range():
  block
```
* break and continue keywords exists in python. functionality is same as in C language.
* Break usage is not recommended.

## Chapter 6:
Python has modules that consists of utility methods. Some of the useful python modules are math, time, random.
* **math** contains methods to find log, sqrt, power, trigonometric functions etc
* **random** contains methods like randint, randrange, seed, choice etc
* **time** module contains important methods sleep, clock etc
Synatx for importing methods inside modules
```Python
# Syntax to import specific methods only
from module import method1, method2

# import all methods inside a module.
# this is not a recommended (its discouraged) as this may introduce
# ambiguity in methods named same in local program.
from module import *

# import tyhe entire module
# methods can be referred using the qualified name only.
# A methods qualified name is "module_name.method_name"
import module
```

## Chapter 7
User defined functions syntax
```Python
# return keyword to return result from a method.
def method_name(parameter_list):
    method_block
```
* Usually **main** method is written and treated as the driver to call in to other methods.
* Documentation string(short as doc string) in python is a string enclosed between ''' or """ and present in the beginning of a file or beginning of a function.
  

## Chapter 8
* global variables are declared outside all the functions.
* global variables usage discouraged inside functions
* Python supports default parameters. non default parameters hsould come before default parameters.
* function is a special kind of object. 
  ```Python
    print(type(sqrt))
    # output will be <class ’builtin_function_or_method’>
  ```
* Function can be assigned to a variable and invoked through the variable.
  ```Python
    x = print
    x('hello world')  # prints 'hello world'
  ```

## Chapetr 9
* list elements gets defindd within []
  ```Python
    lst = [1, 2, 3, 4, 5]
    print(len(lst)) # prints the length of the list

    # define empty list
    empty_list = []

    # list concatenation
    list1 = [1,2,3]
    list1 += [4] # list1 = list1 + [10] is also same
    print(list1) # prints 1 2 3 4

    # append operation works only with another list
    # we cannot join a list and a non list

    # creating a list from range
    list_range = list(range(10)) # creates a list containing integers from 0 to 9

    # list element duplication
    list1 = [0] * 10 # returns a list of size 10 filled with 0s
    list2 = [1, 2] * 2  # list becomes [1, 2, 1, 2]
  ```
* lists are mutable data structures
* comparing list with equality operator(==) compares each element in the list.
* **is** operator checks if list1 is alias of list2, in other words if both the list variables point to the same list data structure in memory.
* **list_copy** functions copies the contents of input list and creates and returns a new list 
* slicing the list `list[begin_index: end_index]`. Default begin_index is 0 and default end_index is length of the list to be sliced. Slices the array from begin index to end index - 1.
* slice assignment
  ```Python
    # how the slice assignment works
    # first take the slice out of the list specified on the LHS
    # then insert the list present on the RHS to the beginning index of the slice in he LHS list
    lst = [1, 2, 3, 4, 5, 6]
    lst[2: 5] = [10, 20, 30] # lst will now be [1, 2, 10, 20, 30, 6]
    # note slice [3,4,5] is removed and new list elements are added/inserted at the slice start index.
    lst[2:2] = [100] # lst will now contain [1,2,100,10,20,30,6]
    # empty list sliced and new list elements inserted from index 2. 
  ```
* lists passed to functions as parameters, the parameter variable becomes alias of the list passed. 
* Lists in python are mutable, heterogeneous (can contain objects of any type)

## Chapter 10
 Sample programs to work on lists

## Chapter 11
* Objects in python contains data and methods.
* Methods between __ (double underscores) is meant for objects internal use only. Clients should not call these methods.
* Str type/class contains useful methods like count, strip(equivalent to trim in java), lower, upper, startswith, endswith, find, format etc
* strings are immutable.
* lists contains methods like insert, append, remove, index, sort, reverse etc. Many of these methods modify the list itelf like insert, reverse, sort, append, remove etc 

# References:
* Learn to code in python3 by Richard L.Halterman