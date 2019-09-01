# Python object oriented shortcuts

**NOTE**: These notes will be useful if you have read the book atleast once.

## `len()` function
`len()` function - objects should implement `__len__()` method. `len()` function more efficient and maintainable.
```Python
# obj = MyObject()
# len() method calls MyObject.__len__(obj)
len(obj)
```

## `reversed()` function
input is a sequence and returns a copy of the sequence in reverse order. Looks for `__reversed__` method on the class of the sequence object, if not found `__len__` and `__get_item__` methods are used to construct the new reversed sequence.
```Python
# sample class for this example
class MySequence(list):
  def __reversed__(self):
    pass

# seq = MySequence()
# reversed() method calls MySequence.__reversed__(seq)
reversed(seq)
```

## Enumerate 
provides a tuple of **index along with value** when looping through a container.
```Python
# assume a tennis list ranking
ranking_list = ["Djokovic", "Nadal", "Federer"]
for i, player in enumerate(ranking_list):
  print("Rank: {}, Player:{}".format(i+1, player))
```

Use `dir(__builtins__)`. Commonly used builtin functions
* `all()`, `any()`
* `eval()`, `exec()`, `compile()`
* `hasattr`, `getattr`, `setattr`, `delattr`
* `zip()` - two sequence in to a sequence of tuple 

## File I/O
use `help(function_name)`
Useful methods
* `open(filename, mode, buffer)` - returns file object
* `read()`, `readline()`, `readlines()`
* `write()`, `writelines()`
* `close()`

File object returned by open() is iterable directly using **for** loop going through one line at a time. 

Binary files - read content in chunks using `read()`


## Pythonic way to handle files
**with** statement - startup, cleanup code execution.
Can work with any object having **__enter__** and **__exit__** methods.

```Python
# using "with" statement, __enter__ and __exit__ methods on file object are called.
# __exit__ ensures file closing even on exception scenarios.
with open('readme.md') as readme_file:
  for line in readme_file:
    print(line)
```

## Alternative to method overloading.

## Default arguments

Python - cant have multiple methods with same name
* Can use default argument - positional arguments(mandatory), keyword arguments(optional with default values supplied) 
* Dynamically generate default values not possible. Value computed when first loaded by interpreter.
* Beware of using empty list as default value (refer book).

* Recommended value for default argument is **None**.

## Variable arguments
```Python
# args is a tuple
def my_func(*args):
  print(type(args))
  for arg in args:
    print(arg)

# kwargs is a dict
def my_func2(**kwargs):
  print(type(kwargs))
  for k, v in kwargs.items():
    print(arg)
```

## Unpacking arguments
prefix a list/tuple with **\*** to unpack. prefix a dictionary with **\*\*** to unpack.

```Python
def func(a, b, c):
  print(a, b, c)

func(*[1,2,3])
func(*(1,2,3))
# unpacking causes call to behave like invoking with keyword arguments.
func(**{"a": 1, "b": 2, "c": 3})
```

## Functions are objects
* possible to set attributes on functions.
* functions have attributes. `function_name.__name__`, `function_name.__class__`, `type(function_name)`
* dir(function_name) - lists attributes of function.
* functions can be passed as arguments - helps in callback scenarios.


## Function as attributes
useful in **monkey patching**. useful in fixing bug in 3rd party library functions(hacky).

```Python
class Sample:
  def print_message(self, message):
    print("Inside: print_message, message:{}".format(message))

def fake_print_message(message):
  print("Inside: fake_print_message, message:{}".format(message))

sample = Sample()
sample.print_message("Hello")
print(sample.__dict__)

# think of this like replacing the __dict__ of the object with key "print_message", updating its value to point to a different function object.
sample.print_message = fake_print_message
sample.print_message("Hello")
print(sample.__dict__)
```

* can replace methods on an object
* can replace method on a class. this will reflect on all instances of the object

## Callable objects
object made callable - implement `__call__` method with required arguments

```Python
class CallableObject:
    def __call__(self, message):
        print("message: {}".format(message))

obj = CallableObject()
obj("This is a callable object behaving like a function")

# instantiate and then call
CallableObject()("Hello")

```


---

## References:
* [Python3 Object oriented programming by Dusty Phillips](https://www.amazon.in/dp/B005O9OFWQ/ref=dp-kindle-redirect?_encoding=UTF8&btkr=1)