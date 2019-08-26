# Exceptions

## Exception handling
```Python
try:
  # code block
except SomeSpecificError as e:
  # exception handling for SomeSpecificError
except:
  # catch all other exceptions
```

## Classes of Exceptions 

### Finding the class hierarchy
`object.__class__` returns the class information of the object.
```Python
try:
  1/0
except ZeroDivisionError as ex:
  ex_class = ex.__class__
  print(ex_class.__name__)
  while ex_class.__bases__:
    base = ex_class.__bases__[0]
    print("""base class of {0!s} is {1!s}""".format(ex_class.__name__, base.__name__))
    ex_class = base
```

### Exception classes hierarchy
object
  BaseException - This is the base class of all Exception classes
    Exception
      ArithmeticException
        ZeroDivisionError

## Raising exceptions
```Python
# raise keyword followed by the exception class
raise ZeroDivisionError

# raise keyword followed by the exception instance
raise ZeroDivisionError("cannot divide by zero")

# raise keyword inside except raises the caught error
try:
  1/0
except ZeroDivisionError as e:
  print(e)
  raise
```

## Creating custom exceptions
```Python
# Custom exceptions are created as subclass of Exception class
class InvalidValueException(Exception):
  """This exception is raised when the program encounters invalid value for a integer variable"""
  pass  # rest of the implementation can be skipped 
```

## Properties of exception
Assume `ex` variable contains the exception.
* `ex.__class__.__name__` - name of the class of the exception object.
* `str(ex)` or simply `ex` - returns the exception message or string representation.
* `ex.args` - stores arguments passed to the `Exception()` constructor. This is a **tuple**.

## Catching exceptions
Except handles first matching clause. So the most specific clause comes first followed by themost generic ones.
```Python
try:
  {}["Hello"]
except Exception as e:
  print("""Exception : {0}""".format(e.__class__.__name__))
except KeyError as ex:
  print("""KeyError: {0}""".format(ex.__class__.__name__))

# output 
# Exception : KeyError
# handled by first clause because KeyError is a subclass of Exception
```

## Using finally clause
Whether an exception inside try is caught or unhandled, finally clause is always executed.
```Python
# in the below syntax, except is optional.
try:
  # code
[except SomException as ex:
  # exception handling ]
finally:
  # cleanup code
```

## Else clause for no exception scenario
**This clause is executed after the try clause but before the finally clause only when no exception is raised**
```Python
try:
  # code
except Exception as e:
  # exception handling code
else:
  # no exception scenario code
finally:
  # cleanup 
```

## Exception chaining
```Python
# explicit raising
try:
  1/0
except Exception as e:
  # raised exception's __cause__ contains the caught exception
  raise Exception("Cannot divide by zero") from e

# implicit raising
try:
  1/0
except Exception as e:
  # raised exception's __context__ contains the caught exception
  print(e.name) # this raises attribute error

# in the AttributeError object raised, the __context__ would point to the ZeroDivisionError.
```

## Pythonic exception handling
**Easy to ask forgiveness than permission**
Encourages more exception handling.

---

## References:
* [Python3 for absolute beginners](https://www.amazon.in/Python-Absolute-Beginners-Tim-Hall/dp/1430216328)