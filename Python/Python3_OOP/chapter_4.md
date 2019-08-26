# Expecting the unexpected

**NOTE**: These notes will be useful if you have read the book atleast once.

## Raising exception
```Python
#  Syntax
# raise <ExceptionClass>("Optional Exception message") 
raise ValueError("Message")
```

## Handling exception
**except, finally, else** can all be omitted. If **except** is used, the order is always **try**, **except**, **else** and **finally**. **try** clause can also be followed by just **finally** clause. **else** clause cannot be usd with just **try** clause

While handling exceptions with multiple except clauses, the first matching clause is always the one that gets executed. This could happen due to inheritance(is a relation, Subclass is a SuperClass). So the rule is handle more specific exception first followed by more general exception.

`ExceptionInstance.args` access arguments passed to the constructor.

Code inside **finally** clause gets executed even if we **return** from **try** or **except** clause.

```Python
# Syntax
try:
  # statements
except:
  # simply except clause catches all exceptions.
  # exception handling statement.

# ===========================================
#  Syntax to handle specific exceptions
try:
  # statements
except (Exception1, Exception2):
  # exception handling statement.

# Or

try:
  # statements
except Exception1 as ex1:
  # exception handling statement.
  print(ex1)
except Exception2 as ex2:
  # exception handling statement.
  # we can also use reference to the exception object
  print(ex2.args)

# ==================================================
# Syntax with else and finally
try:
  # statements
except:
  # exception handling
else:
  # code to execute on non exception scenario
finally:
  # code to execute irrespective of exception was thrown or not.
```

## Exception hierarchy
All exceptions must inherit from either **BaseException** or one of its subclasses.

`Exception`, `SystemExit` and `KeyboardInterrupt` all derive from `BaseException`

SystemExit - raised on invoking sys.exit. handling it can be used to perform actions before exiting the program.

**except** clause without any exceptions mentioned explicitly will catch all exceptions that are subclasses of **BaseException**.
```Python
#  This can handle all exceptions which are subclassses of Exception.
try:
  # statements
except Exception:
  # exception handling
```

## Defining our own exceptions
**Exception** can accept any object in its initialization and store it as a tuple, which can then be accessed using `args` attribute

```Python
import random

class InvalidGreetingException(Exception):
  pass

def main():
  greeting_messages = ["Hello", "Welcome", "Hey", "Hi"]
  choices = greeting_messages + ["Bye", "Thanks", "GoodBye"]

  greeting_choice = random.choice(choices)
  print("Selected choice: {0!s}".format(greeting_choice))

  if (greeting_choice not in greeting_messages):
    raise InvalidGreetingException("Not a valid word for greeting", greeting_choice)

if __name__ == "__main__":
  try:
    main()
  except InvalidGreetingException as e:
    for arg in e.args:
      print(arg)
```

**Ask forgiveness ratehr than permission**
Exception object can be used to pass information.

---

## References:
* [Python3 Object oriented programming by Dusty Phillips](https://www.amazon.in/dp/B005O9OFWQ/ref=dp-kindle-redirect?_encoding=UTF8&btkr=1)
