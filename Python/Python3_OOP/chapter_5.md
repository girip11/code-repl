# When to Use Object Oriented Programming

**NOTE**: These notes will be useful if you have read the book atleast once.

## Property
Property in python - makes method look like attributes

```Python
class Phone:
  def __init__(self, name, color):
    self._name = name
    self._color = color

  #  name not changeable once set
  def _get_name(self):
    return self._name

  # color of phone changeable
  def _set_color(self, color):
    self._color = color

  def _get_color(self):
    return self._color
  
  #  define properties
  name = property(_get_name)
  color = property(_get_color, _set_color)

phone = Phone("Motorola onepower", "black")
print("Name: {0!s}, Color: {1!s}".format(phone.name, phone.color))

phone.color = "red"
print("Name: {0!s}, Color: {1!s}".format(phone.name, phone.color))
```

`property()` - creates a proxy object for the attribute access.
`property(getter, setter, delete, docstring)` - getter and setter are frequently used. delete rarely used. docstring is optional. **If docstring is not provided, default value is picked from getter function.**

## Property creation using decorators
getter, setter methods generally share the same name as the name of the attribute
```Python
class Phone:
  def __init__(self, name, color):
    self._name = name
    self._color = color

  # name not changeable once set
  @property
  def name(self):
    return self._name

  @property
  def color(self):
    """
      Color of the phone
    """
    return self._color

  @color.setter
  def color(self, color):
    self._color = color

phone = Phone("Motorola onepower", "black")
print("Name: {0!s}, Color: {1!s}".format(phone.name, phone.color))

phone.color = "red"
print("Name: {0!s}, Color: {1!s}".format(phone.name, phone.color))
```

## Deciding when to use properties
* In python data, properties, methods are all attributes on a class.
* Functions and methods are object themselves.
* Action on an object is achieved using methods. Method names are usually verbs.
* Use attribute unless the get, set of the attribute needs special checks. Attribute name is **noun**
* Properties can be used to cache values with custom getters, while custom setters can be used for validation.

## Remove duplicate code
* Duplicate code affects readability and maintainability. **Dont Repeat Yourself (DRY)** principle

---

## References:
* [Python3 Object oriented programming by Dusty Phillips](https://www.amazon.in/dp/B005O9OFWQ/ref=dp-kindle-redirect?_encoding=UTF8&btkr=1)