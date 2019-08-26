# Classes

## creating and instantiating class
```Python
class Employee:
  def setName(self, name):
    self.name = name.title()

  def getName(self):
    return self.name

  def setAge(self, age):
    self.age = age

  def getAge(self):
    return self.age

  def setDesignation(self, designation):
    self.designation = designation.title()

  def getDesignation(self):
    return self.designation

# instantiating a class
employee1 = Employee()
employee1.setName("John Doe")
employee1.setAge(25)
employee1.setDesignation("Software Engineer")

# accessing attributes directly
print(",".join([employee1.name, str(employee1.age),
employee1.designation]))

# accessing through getters
print(",".join([employee1.getName(), str(employee1.getAge()),
employee1.getDesignation()]))

# names available on that object
dir(employee1)
```

## self
self refers to the object on which the method is operating. `dir(instance)` returns list of names available within that object.

## Object identity
Object assigned an identity when created. `id()` builtin function returns the object id. To compare two objects we can use the **is** operator.
```Python
employee1 = Employee()
employee1.setName("John Doe")
employee1.setAge(25)
employee1.setDesignation("Software Engineer")

employee2 = Employee()
employee2.setName("Jane Doe")
employee2.setAge(25)
employee2.setDesignation("Software Engineer")

print(id(employee1))
print(id(employee2))

print(employee1 is employee2)
```
object id is an integer. Every object has unique id.

## Object type
`type(instance)` builtin returns the typeof the object. 

**NOTE**: **type** and **id** are used only for debugging purposes.

## Namespaces
Each object has its own namespace dictionary. Names are added to object namespace when first assignment to the variable is done or when a module is imported. This is called **name binding**. Scope is the visibility of a name inside a code block
Names defined inside a class definition can be accessed inside its methods only through **self**. Names are looked up in the scope of the current class before proceeding to search in the scope of its base classes. **NameError** raised when the name is not found in any scope.

## Inheritance
```python
# we can refer to this relationship as
# parent class, child class or
# base class, derived class or
# super class , subclass

# Syntax
class Parent:
  # parent class body

class Child(Parent):
  # child class
```

## Magic methods
These methods are part of programming languages. These method names are flanked on both sides by double underscores.

## Constructors
`object.__init__(self, params...)`. Constructor does not return any values.

```Python
class Employee:
  def __init(self, name, gender, designation):
    self.name = name
    self.gender = gender
    self.designation = designation

# object creation
employee1 = Employee("Jane Doe", "Female", "Software Engineer")
```

```Python
# Child class constructor usually calls parent class constructor.
class Parent:
  def __init__(self, param1, param2):
    # constructor code

class Child1(Parent):
  def __init__(self, param1, param2, param2):
    # This is one way of calling parent constructor. Alternate way is calling user super() which is preferred over this way.
    # this syntax is very useful in mutliple inheritance scenarios, where we have to call __init__ of two or more parents of the child class
    Parent.__init__(self, param1, param2)
    self.param3 = param3

class Child2(Parent):
  def __init__(self, param1, param2, param2):
    super().__init__(param1, param2)
    self.param3 = param3
```

## string representation of the object
String representation of an object can be customized using the method `object.__str__(self)`. This methods is used by the builtins `str(object)` and `print(object)`
```Python
# Child class constructor usually calls parent class constructor.
class Parent:
  def __init__(self, param1, param2):
    # constructor code

class Child(Parent):
  def __init__(self, param1, param2, param2):
    super().__init__(param1, param2)
    self.param3 = param3
  
  # used by str() and print() builtins
  # informal string representation
  def __str__(self):
    return """{0}, {1}, {2}""".format(self.param1, self.param2, self.param3)

  # official string representation. used by repr() builtin
  def __repr__(self):
    return """Child({param1!s}, {param2!s}, {param3!s})""".format(**vars(self))

child = Child("arg1", "arg2", "arg3")
print(child)
print(str(child))
print(repr(child))
```

## Other useful magic methods for emulating containers (list, dictionary)
Below tow magic methods help emulate types like list, dictionary.
* `object.__len__(self)`- returns length of the object as integer. used by the builtin `len()` method.
* `object.__getitem__(self, key)`- should return value similar to output of `self[Key]`

Below methods make the collection mutable
* `object.__setitem__(self, key, value)`- should set value when accessed like `self[Key]`
* `object.__delitem__(self, key)`- similar to using with **del** statement.
* `object.__iter__(self)`  iterating purpose
* `object.__reversed__(self)` - invoked by `reversed()` builtin function.
* `object.__contains__(self, item)` - contains operation.

## Properties
`property([fget], [fset], [fdel], [doc])`

All four parameters optional. If none provided, makes the attribute inaccessible. The actual attribute name is **prefixed with double underscores**. Property takes the name of the attribute without the double underscores.

* read_only property - `property(get_function)`
* read/write property - `property(get_function, set_function)`. These methods are invoked on every read or write to the property.
* delete the attribute - third argument. keyword arguments supported, which means we can only specify delete parameter and skip other ones.`property(fdel = del_function)`
* docstring for the property - fourth argument. `property(doc = docstring)`

## Customizing attribute access

* `object.__getattr__(self, name)` - returns attribute value.
* `object.__getattribute__(self, name)` - on accessing via attribute name. Not available in python 2 and below.
* `object.__setattr__(self, name, value)` - on attribute assignment attempt
* `object.__detattr__(self, name)` - on deleting the attribute.

**NOTE**: understand with examples  on usage of attribute, property, magic method(__getattr__).

---

## References:
* [Python3 for absolute beginners](https://www.amazon.in/Python-Absolute-Beginners-Tim-Hall/dp/1430216328)

* [Property vs __getattr__](https://stackoverflow.com/questions/22616559/use-cases-for-property-vs-descriptor-vs-getattribute)