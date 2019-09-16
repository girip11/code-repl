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
for item in iterable:
  print(item)
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

---

## References:
* [Python3 Object oriented programming by Dusty Phillips](https://www.amazon.in/dp/B005O9OFWQ/ref=dp-kindle-redirect?_encoding=UTF8&btkr=1)
