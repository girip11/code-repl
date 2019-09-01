## Python data structures

**NOTE**: These notes will be useful if you have read the book atleast once.

Python disables arbitrary attributes on **object** and other builtins, to be memory efficient.

* restrict arbitrary properties on custom classes, use **slots**

## Storing attributes with empty objects
```Python
class MyObject:
    pass

myObj = MyObject()
myObj.name = "Foo"
myObj.age = 20
```

## Tuples
immutable. stores data.usually stores data of different types. but they affect **code readability** (difficult to interpret what each value in a tuple stands for)

```Python
# defining tuples
empty_tuple = ()
test_tuple = (1, "Foo", 100.25)

# tuple unpacking in a function
def tuple_unpack_example(test_tuple):
  # exception raised on tuple length and variable count mismatch
  count, name, value = test_tuple

  # tuple elements can be accessed via []
  for tuple_value in range(len(test_tuple)):
    print(test_tuple[tuple_value])

  return

tuple_unpack_example(test_tuple)
```

## Named tuples
offers readability. immutable. groups read only data together.

```Python
from collections import namedtuple

# namedtuple syntax
# namedtuple("TupleIdentifier", "Space separated attribute names")
Employee = namedtuple("Employee", "name experience")
employee = Employee("John Doe", experience=5)

print("Name: {0!s}, Experience: {1!s}". format(employee.name, employee.experience))
```

## Dictionaries
string, numbers, tuple, objects can all be used as keys. lists, dictionaries being mutable cannot be used as key in the dictionary
```Python
#  commonly used syntax to define an empty dictionary
empty_dict = {}

# alternatively
empty_dict = dict()

fruits_count_dict = {"apple": 1, "oranges": 10}

print(fruits_count_dict["apple"])

# dict.get(key, default_value)
print(fruits_count_dict.get("mango", 0))

# setdefault(key, value_to_set)
print(fruits_count_dict.setdefault("mango", 5)))

#  add/update using [] index syntax
fruits_count_dict["apple"] = 7

#  keys(), values(), items()
print("keys: {0!s}".format(",".join(fruits_count_dict.keys())))

print("values: {0!s}".format(",".join(fruits_count_dict.values())))

for k,v in fruits_count_dict.items():
  print("K:{}, V:{}".format(k,v))
```

## Dictionary uses
* collection of key value pairs as in fruits example, where each entry in the collection is of similar nature.

* To represent a table like structure, where each key value represents a column in the table. Advantage over named tuple in this case is that dictionary is mutable.

## defaultdict
function is invoked whenever a key accessed is not in teh dictionary.
```Python
from collections import defaultdict
# usinf defaultdict(function) we can assign default values to keys not in the dictionary
fruits = defaultdict(int)
# int() return 0
print(int())

fruits["apple"] = 1
fruits["mango"] = 10

print(fruits["apple"])

# prints 0 returned by int()
# also adds entry for orange to the dictionary
print(fruits["orange"])

```

## Counter
stores occurence of each key as its value in a collection.

```Python
from collections import Counter
favorite_sports = ["cricket", "tennis", "cricket", "football", "tennis", "cricket"]
counter = Counter(favorite_sports)

# most_common(n). top n 
print(counter.most_common(2)[0])
```

## lists
mutable. used for storing homogeneous entities. Some useful methods on lists are
* `append()` - add item to list
* `extend()` - concat another list inplace
* `insert(index, element)`
* `index(element)` - exception when list doesnt contain element
* `find(element)` - returns -1 when list doesnt contain element
* `count(element)` - counts occurrence of element in the list
* `sort()` - inplace sorting
* `reverse()` - inplace reversing


## Sorting
* Custom sort logic requires only **`__lt__`** (less than) method defined on the class. This method returns **True** if current instance is less than passed instance else **False**.

* **__lt__** and **__eq__** along with **@total_ordering** class decorator, we get other method __gt__(&gt;), __ge__(&gt;=), __le__(&lt;=), __ne__(!=) implementations.

```Python
# case insensitive sort
#  sort(key)
mylist = ["Hello", "bar", "Foo"]

# assign key with a function object
#  str.lower is a function accepting a string object
mylist.sort(key = str.lower)

# sorting a tuple
from operator import itemgetter
# by default sort happens based on tuple's first item
my_tuple = [(1, "a"), (2, "c")]

#  to use an item other than the first item(index 0) use itemgetter(index)
my_tuple.sort(key =  itemgetter(1))

```

## Sets
Objects in a set are unique, **unordered**. Set can store any **hashable** object.

```Python
empty_set = set()
empty_set.add("item1")

set_with_items = {"item1", "item2"}
for item in set_with_items:
  print(item)
```
Commonly used methods.
* `set1.union(set2)` or `set1 | set2`
* `set1.intersection(set2)` or `set1 & set2`
* `set1.difference(set2)` or `set1 - set2`
* `set1.symmetric_difference(set2)` - (set1 - set2) intersection (set2- set1)
* `set1.issubset(set2)` - returns bool
* `set1.issuperset(set2)` - returns bool

**union, intersection and difference** methods can take multiple sets in the argument

* checking membership(contains operation) using sets is efficient compared to list


## Extending builtin containers
we can use composition or inheritance to add functionality to existing builtin collections.

Composition is recommended. inheritance preferred when existing container behavior needs to be overridden.

## Queues
### FIFO queues
**First In First Out** . useful in producer, consumer scenarios helps in buffering.
```Python
from queue import Queue

my_queue = Queue(maxsize=5)
#  get on empty queue without blocking
# raises Empty exception
my_queue.get(block=False)
print(my_queue.empty())

my_queue.put("item1") # adds to last
my_queue.put("item2", block=False)
my_queue.put("item2", timeout=1)
print(my_queue.get()) # gets from first
print(my_queue.full())
```

### LIFO queues or Stack
**list** is efficient compared to LifoQueue. use standard lists **`append()`** and **`pop()`** operations.

* LifoQueue provides  **concurrent access**
* enforces **strictly stack interface**

```Python
from queue import LifoQueue

stack =LifoQueue(maxsize = 3)
if(stack.empty()):
  stack.put("item1") # adds last
  stack.put("item2", block=False)
  stack.put("item3", timeout = 1)

print(stack.full())

if not stack.empty()):
  print(stack.get(block = False)) # takes from last
```

### Priority Queues
tuples stored in this queue. First element in tuple is the priority and the second is the data. implemented using **heap** data structure (heapq module).

* `get()` - blocks if queue is empty
* `put()` - blocks if queue is full

---

## References:
* [Python3 Object oriented programming by Dusty Phillips](https://www.amazon.in/dp/B005O9OFWQ/ref=dp-kindle-redirect?_encoding=UTF8&btkr=1)