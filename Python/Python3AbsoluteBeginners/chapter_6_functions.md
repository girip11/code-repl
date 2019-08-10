# Chapter-6: Functions
functions follow **snake_case** as the naming convention. Function names are usually verbs while the variable names tend to be nouns.

## Function syntax
```Python
# function syntax
# ================
# def function_name(param1, param2..):
#   """
#   This is a doc string. This can be #   used to describe about the 
#   function. doc string should be 
#   the first thing in a function.
#   """
#   function_body
#   return None # you could choose to return a value. default return value is None

def print_hello_world():
  """
    prints message "Hello world" to the console
  """
  print("Hello world")

def print_message(msg):
  print(msg)

def get_string_length(input_string):
  """
  returns the length of input_string
  """
  return len(input_string) if (input_string != None  and type(input_string) == str) else 0

# function call
print_hello_world()
print_message("Hello world")
# below arguments are referred to as positional arguments
print(get_string_length("Palindrome"))
```

## Default parameters and keyword arguments
```Python
# function with default parameters
import random
def get_random_number(min= 0 , max = 100):
  """
    returns random number from min to max
  """
  return random.randint(min, max)

# function call with default parameters
random_number = get_random_number()

# calling a method with keyword arguments. note that the order of arguments doesnt matter in this case
random_number = get_random_number( max = 1000, min = 10)
```

## Passing variable arguments to the function
```Python
# convention is to call the * parameter as args
def print_values(*args):
  print(args) # argsis a tuple here. verify using type(args)

print_values("Apple", "Mango", "Orange", 1, 10.5)

# convention is to call the ** parameter as kwargs
def print_key_value_pairs(**kwargs):
  print(kwargs) # kwargs is a dict.

print_key_value_pairs(one = 1, two = 2, three = 3)
```

**NOTE**: positional arguments comes before keyword arguments. Convention is to place parameters followed by parameters with default values, *args and then **kwargs.

**\*** and **\*\*** can be used in function calls. First these parameters are expanded as tuple and dict respectively and then passed to the function.

## Docstring convention
* First line - short description of the function
* function parameters description
* longer description of the function explaining algorithm used if anu
* return value description
* example function call with optional arguments, keyword arguments.
* information on side-effects, exceptions

## Variable Scope
* symbol table to track names used in the program. `vars()` built-in can help dump the values as dictionary.
* variables created in main program's symbol table known as **global variables**. `globals()` builtin to view them.
* variables created inside function stored in symbol table specific to that function.`locals()` builtin to view them.

* all functions can access global variables. if local variables have same name as global variables, then the global variables cannot be used inside the function. known as **shadowed globals**

## global statement
If a function uses global variables, then we use **global** statement to declare the usage of those global variables.

Using **global** statement new global variables can be defined from inside a function.

```Python
planet1 = "mercury"
planet2 = "venus"
planet3 = "earth"

def capitalize():
  global planet1, planet2, planet3
  planet1 = planet1.upper()
  planet2 = planet2.upper()
  planet3 = planet3.upper()
  planets = ",".join([planet1, planet2, planet3])
  print(planets)
  print(vars())
```

## passing lists and dictionaries to functions
Integers, floats are passed by value to functions.
String, tuple are immutable themselves. so when passed to function as arguments, those values remain unchanged.
In case of mutable structures like lists, set and dictionaries, only the reference is passed. It is possible to modify these sequences from inside the function and cause side effects.

---

## References:
* [Python3 for absolute beginners](https://www.amazon.in/Python-Absolute-Beginners-Tim-Hall/dp/1430216328)