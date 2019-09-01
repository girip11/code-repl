# Strings and serialization

**NOTE**: These notes will be useful if you have read the book atleast once.

## Str class
Strings in python are immutable. In python3, string is a sequence of unicode charcaters.
```Python
#  lists all the string methods
dir(str)

# help on string methods
help(str.islower)

# below way also works as string concatenation
sample_string = ("help(str.isdigit)" " gives documentation" " on the string class" " isdigit method")
print(sample_string)
```


## String formatting
Custom formatting in object by overridding the __format__ method.
```Python
# arguments applied in order
"{} has scored {} centuries in cricket.".format("Sachin Tendulkar", "100")

# to reuse arguments use indexes.
"{0} has scored {1} centuries in cricket. {0} also holds record for most number of runs scored in international cricket".format("Sachin Tendulkar", "100")

# escaping braces using {{}}
"In {}, {{}} will escape the brace itself".format("python")

# String formatting using keyword argumets
# Mixing unlabeled braces or indexed braces with keyword agruments is allowed. In that case positional arguments should precede keyword arguments
"""Author is {boook_name} is {author_name}""".format(book_name="Python3 Object Oriented Programming", author_name="Dusty Phillips")

# using lists
# consider it writing python code inside {} or []
"""
<ul>
  <li>{items[0]}</li>
  <li>{items[1]}</li>
</ul>
<ol>
  <li>{0[0]}</li>
  <li>{0[1]}</li>
</ol>
""".format(["OItem3", "OItem4"], items = ["Item1", "Item2"])

# using dictionary in string formatting
"<a href='{attr[href]}' title='{attr[title]}'>{content}</a>".format(attr={"href": "example.com", "title": "Example website link"}, content = "Visit example.com")

# using objects
# Assume MyObject has attribute name
class MyObject:
    pass
myObj = MyObject()
myObj.name = "Girish"
"name: {0.name}".format(myObj)

# formatting floats
"{0:0.2f}".format((22/7))

# formatting datetime
import datetime
"{0:%Y-%m-%d}".format(datetime.datetime.now())
```

## Converting bytes to text and vice versa
`dir(bytes)` . **bytes** object is immutable.
* `str.encode(encoding_scheme)` and `bytes.decode(encoding_scheme)`. In the absence of encoding scheme, uses `sys.getdefaultencoding()`

## Mutable bytes
`bytearray` - holds bytes

## regular expressions
`import re` - to import regex module
`dir(re)` - gives methods on regex module

Useful methods
* `re.match(pattern, search_string)` 
* `re.search`
* `re.findall`

* **^** - matches start of the string
* **$** - end of the string
* **.** -matches a single character
* **?** - matches zero or one time of the preceding expression
* **\*** - matches zero or more times of the preceding expression
* **+** - matches one or more times of the preceding expression.
* **\[ \]** - range
* **()** - group expressions
* **{n}** - applies n repetitions of the preceding pattern/expression.

```Python
import re as regex
regex_pattern = "^[A-Z]([a-z]*_)+$"
regex.match(regex_pattern, "String")
match = regex.match(regex_pattern, "Matchingstring_")

```
Using the compiled regex, saves computation when using regex. `re.compile` is used for this.


## Serialization
pickling -serialization
unpickling -deserialization

`import pickle`
Useful methods
* `dump()` and `dumps()`
* `load()` and `loads()`

uses `__get_state__()` and `__set_state__`() method which inturn used `__dict__` for storing the objects state.

## serialization of objects
JSON, CSV, YAML, XML etc. JSON widely used in web.

`import json`

---

## References:
* [Python3 Object oriented programming by Dusty Phillips](https://www.amazon.in/dp/B005O9OFWQ/ref=dp-kindle-redirect?_encoding=UTF8&btkr=1)
