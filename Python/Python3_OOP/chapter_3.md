# When objects are alike
**NOTE**: These notes will be useful if you have read the book atleast once.

## Basic inheritance
* All python classes - subclass of **object**.
```Python
class SubClass(SuperClass):
  pass
```

## Class variable
```Python
class Fruit:
  # This is a class variable
  fruits_list=[]

  def __init__(self, fruit_name):
    # self.fruits_list.append(fruit_name) also works
    # with self first the object is lookeup for attribute and then its class.
    # NOT RECOMMENDED accessing class variables using self as setting the variable using self creates instance level attribute
    Fruit.fruits_list.append(fruit_name)

fruit = Fruit("apple")
print(Fruit.fruits_list[0])

# also works because once attribute not found in the object, it is looked up in its class
print(fruit.fruits_list[0])
```

## Extending buitlin classes
we can extend builtin classes like list, tuple etc

```Python
class CustomList(list):
  pass

# help(isinstance) for help
mylist = CustomList()
print(isinstance(mylist, list))
```

## Super function
Returns object as instance of its parent class. Can be called **at any point in a method** and can be used **in any method**.

```Python
class SuperClass:
  def __init__(self, param1):
    self.param1  = param1

class SubClass(SuperClass):
  # overridding super class __init__ method
  def __init__(self, param1, param2):
    super().__init__(param1)
    self.param2 = param2

```

## Multiple inheritance and mixin
```Python
class SubClass(SuperClass1, SuperClass2):
  pass
```
Mixin - superclass that is not meant to exist on its own. Multiple inheritance useful in case of mixins, to enrich functionality of existing class.

Inherit from a mixin class just to reuse the functionality provided by it. But the same effect can also be achieved by passing the mixin class instance to the object requiring the functionality.

Prefer Aggregation/Composition(**has a relationship**) over multiple inheritance (**is a relationship**).

## Diamond problem 
```
    A
   / \
  B   C
   \ /
    D
```
Call `__init__` of parents from child using the syntax
* `ParentClass.__init__(self, params...)`

* Using the above explicit invocation causes **A's** method (for instance __init__) to be called twice. 

* `super()` function helps in such cases. this function calls the **next method in the hierarchy** (next method will be based on the inheritance order defined.)

* `mro` attribute used for defining Method Resolution Order.

* `super()` function along with each **__init__** method which can **accept keyword arguments**, can make next method call in the hierarchy smooth.

## Polymorphism
```Python
class DocumentStore:
  def save(content):
    pass

# saves content to markdown file
class MarkdownDocumentStore(DocumentStore):
  def save(content):
    pass

# saves content as HTML file
class HTMLDocumentStore(DocumentStore):
  def save(content):
    pass

# Duck typing example
# no inheritance, but still valid as this has the same behavior required.
class PDFDocumentStore:
  def save(content):
    pass
```
Duck typing -  causes even objects that don't inherit from a parent stiil be valid. this reduces relevance of inheritance, polymorphism.

Duck typing requires to provide implementation to behavior(interface methods accessed) that is required. No need to implement other behaviors(complete interface methods).

## Abstract Base Class(ABC)
* **ABC** - methods and properties required to be considered a type of that class(using inheritance) or a duck-type instance.

* used in python's collection module in the standard library.

```Python
# to list the abstract methods of a class
ClassName.__abstractmethods__

# as long as a subclass implements those abstract methods, **isinstance** and **issubclass** methods will return true, though we have done only duck typing and not actual inheritance.
```

## Creating Abstract base class
module **abc** in python useful to create abstract base classes.
Python decorators used are
* `@abc.abstractmethod`
* `@abc.abstractproperty`
* `@classmethod` - decorator that marks a method as class method

---

## References:
* [Python3 Object oriented programming by Dusty Phillips](https://www.amazon.in/dp/B005O9OFWQ/ref=dp-kindle-redirect?_encoding=UTF8&btkr=1)
