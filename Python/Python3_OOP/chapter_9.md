# The iterator pattern

## Iterator Object
Iterator - object which contains `next()` and `done()` methods.

## Iterators in Python
* the object implements the special method `__next__()`

* `next(iterator)` is usd to get the next object in the sequence.

## Iterator Protocol
* Iterator abstract base class in module `collections.abc` defines the iterator protocol.

* Class with `__iter__` is iterable and returns an Iterator instance (Iterable interface).

* `iter(iterable)` usually returns the iterator object.

* Iterable - object with items that can be looped over, iterator - specific location on the iterable.

* When the items are completed, iterator raises `StopIteration()`

```Python
# iterating on an iterable using for loop

# for first uses the iter() to get the iterable and invokes next() to continue further iterations.

# iterable on iter() returns an iterator
# iterator on iter() returns itself. 
for item in iterable:
  print(item)
```

## itertools
This module contains helpful functions for operating on iterables.

```Python
import itertools

# lists all useful methods for working with iterables.
dir(itertools)

def squareValue(value, power):
  return value ** power

gen = itertools.starmap(squareValue, [(1,2), (2,2), (3,3)])

for value in gen:
  print(value)
```

## Comprehensions
Comprehensions - concise, highly optimized for creating list, set or dict from a sequence. can perform map, filter operations.

### List comprehensions
 List comprehensions faster compared to looping over the list.

```Python
# map a list of strings to list of integers containing their length
input = ['hello', 'this', 'foo', 'bar']
output = [len(entry) for entry in input]

# filter operation
# take only strings with length of atleast 4 characters
words = [entry for entry in input if len(entry) >= 4]
```

### Set and Dictionary comprehensions
* Enclose the expression inside `{}`.

```Python
input = [1, 2, 5, 3, 3, 8, 2, 3]

# set comprehension
unique_values = {n for n in input}

# dictionary comprehension
input = ['hello', 'this', 'foo', 'bar']
output = {entry: len(entry) for entry in input}
```

## Generator expressions
> Generators are iterators that you can iterate over only once. Generators donot store all the values in memory and generate the values on the fly. -[Stackoverflow Yield usage](https://stackoverflow.com/questions/231767/what-does-the-yield-keyword-do)

Same syntax as comprehension, but `()` are unsed instead of `[]` or `{}`. In generator expressions, the final container is not created. Memory efficient.

Generators returned by generator expressions can be iterated over only once.

```Python
input = [1, 2, 4, 5, 6, 2, 9]

# the computation is yet to take place
gen_exp = (e for e in input if e >= 5)
print(type(gen_exp))

# this gen_exp can be iterated over only once.
for item in gen_exp:
  print(item)
```

## Generator and yield keyword
Function with yield keyword is converted to generator object. On encountering the yield statement, function returns the value to the caller, but when `next()` is called on that function, function execution resumes from the line of code **after the yield statement**.

> When the function with yield statement is called, the function doesnot run, instead returns a generator object -[Stackoverflow Yield usage](https://stackoverflow.com/questions/231767/what-does-the-yield-keyword-do)

Wherever in Python, iterable is expected, generators work (duck typing).

```Python
def filter_values(input):
  for n in input:
    if n >=5:
      yield n

input = [1, 2, 5, 3, 3, 8]
generator = filter_values(input)
print(type(generator))   # prints 'generator'

# observe ths class generator has __iter__ and __next__ implemented.
dir(generator)

for value in filter_values(input):
  print(value)
```
Function execution pauses at the yield statement. Whenever `__next__` is called, generator function runs code placed following the yield statement till the **next yield statement**.

A generator function can have multiple yield calls.

## Yield items from another iterable

```Python
# read lines from a file
def processLog(file):
  with open(file) as input_file:
      yield from (log_line for log_line in input_file)
```

`yield from` used with generator expressions, generators(another generator or recursive one)

## Coroutines
Similar to generators, while generators cant have data passed to it, **using coroutines data can be passed to the generators.** (generators produce data, coroutines can consume data)

> The thing that is really confusing for many people is the order in which this happens:
> * yield occurs and the generator pauses
> * send() occurs from outside the function and the generator wakes up
> * The value sent in is assigned to the left side of the yield statement
> * The generator continues processing until it encounters another
yield statement
> -From the book Python3 Object Oriented Programming

`send()` method does the following
* pass value from outside generators
* performs function of `next()` (i.e) returns the value obtained from the next yield statement and pauses the execution.

```Python
# coroutine_example
def counter():
  count = 0
  while True:
    step = yield count
    if(step == None or (not isinstance(step, int))):
      break
    count += step

coroutine = counter()
print(type(coroutine))

# prints 0 and pauses
print(next(coroutine))

for n in range(1, 20):
  print(coroutine.send(i))

coroutine.send(None)
```

## Closing coroutines and throwing exceptions
Generator exits by raising `StopIteration`, that propogates through chained iterators and then to the for loop using the generator.

In case of coroutines, caller knows to proceed to next iteration using `send()` method. Hence coroutines are usually closed by calling `close()` method on the coroutine instance.

`close()` call raises `GeneratorExit` exception. Good practice to wrap yield statement inside try .. finally

---

## References:
* [Python3 Object oriented programming by Dusty Phillips](https://www.amazon.in/dp/B005O9OFWQ/ref=dp-kindle-redirect?_encoding=UTF8&btkr=1)
* [Understanding Python's for statement](http://effbot.org/zone/python-for-statement.htm)