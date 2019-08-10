# Working with text

## String operations
```Python
# default string split character is whitespace
text = "This is a sample text"
text.split()

# performs only 3 splits
text.split(' ', 3)

text.rsplit(' ', 2)

# string.partition("separator") returns a tuple (head, separator, tail)
text.partititon("a")
text.partition("no") # returns entire string in head, empty strings for separator and tail 

# partition in reverse direction
text.rpartititon("a")
```

## Joining strings without concatentation
use `separator.join(string_list)` compared to **+** operator.
```Python
first_name = "foo"
last_name = "bar"
name = " ".join([first_name, last_name])
```

## Changing case
```Python
# capitalize method capitalizes first character of the string and converts the rest to lowercase
text = "exAMple text"
print(text.captialize())

# title method capitalizes first letter of every word in the string. every letter following a space or punctuation gets capitalized
print(text.title())

# convert al characters in string to upper case
print(text.upper())

# converting to lowercase
print(text.lower())

# swapcase. converts upper case to lowercase and vice versa 
text.swapcase()
```

## Simple text formatting
```Python
text = "example text"

# width and the fill character
text.center(50, '*')

# left and right  justify
text.ljust(50, "+")
text.rjust(50, "+")

# fill zeroes to left
text.zfill(50) # output string length will be 50

# converting tab to whitespace
tab_text = "hello\tworld"
tab_text.expandtabs(4) # default tab size is 8 spaces

```

## advanced formatting
`string.format(*args, **kwargs)`
```Python
# both field numbers and keyword arguments can be used
format_string = "{0} wants to convey the message {message}"
format_string.format("John", message = "Hello world")

# using conversion fields
# !s - str()
# !r - repr() 
# repr() =  returns a string that contains printable representation of the object 
format_string = "{0!s} INR equals {1!r} USD: {message!s}"
format_string.format(68, '1', message = "INR to USD conversion")
```

## Format specification

## Integer formatting

## Floating point formatting

## Editing strings
```Python
# remove leading and trailing characters
text = " Hello World "
print(text.strip()) # by default strips whitespace characters
print(text.strip("world"))

# strip from left and right
text.lstrip("H")
text.rstrip("ld")

# replace - string.replace(old_str, new_str, replacement_count)
text.replace("world", "reader", 1)
```

## Finding strings
```Python
text = "This is a sample text"
# in operator
print("This" in text)

# string.find(substr, start_index, end_index)
# returns index of the substr in string if found else -1
text.find("text")

# string.rfind
text.rfind("sample")

# string.index(sub, start_index, end_index)
text.index("sample")

# string.rindex. Starts searching from the end
text.rindex("sample")

# string.count
text.count("is")
```

## Pattern matching using regex
available from **re** module. 

* **.** - matches any single character except newline
* **?** - matches zero or one  occurrence of preceding expression.
* **\*** - matches zero or more occurrences of preceding expression.
* **+** - matches one or more occurrences of preceding expression.
* **^** - match the start of the string
* **$** - match the end of the string


## Escaping regular expression pattern
`re.escape(pattern_string)` escapes all the non alphanumeric character in the **pattern_string**

## Regular Expression Object
Create aregex pattern object using `re.compile(patterns, [flags])`. This helps improve code readability and performance, because the pattern is compiled once and can be used many times without compiling again. Also since the pattern itself is stored in object, if named appropriately makes the code more readable.

## Manipulating string using regular expressions
```Python
# re.sub(pattern, replacement_string, input_string, [match_count_to_replace])

# re.subn(pattern, replacement_string, input_string, [match_count_to_replace]) returns (new_string, replacement_count)

# re.findall(pattern, input_string, [flags]) returns nonoverlapping matching array
```

## Files

### Opening Files
Syntax: `open(filename, [mode], [buffering])`

**mode** and **buffering** are optional parameters. Default mode is **read only** and the file is assumed as **text file**. File modes are
* **r** - read
* **w** - write
* **a** - append only. useful for log files
* **b** - binary
* **+** - read/write

**buffering** when used with write or append mode can either be **0** or **1**. 0 means buffering is disabled, (i.e) data written to disk directly. 1 enables buffering which delays writing the data to disk until `file.flush()` or `file.close()` is called explicitly.
```Python
# open a text file in read only mode
open("text_file.txt")

# open image, audio files using binary mode
open("earth_pic.png", "rb")
```

### Reading from files
`file.read([size])` - without size or size as negative value, reads the complete file content as string object. if size is mentioned, reads min(size, file_length_bytes) amount of bytes from the file and returns a string object.

`file.readline([size])` - without size, reads a line and returns as string object. returns empty string when end of file if encountered. With size option, size number of bytes are read in a line.

`file.readlines([sizehint])` - reads lines of file in to a list. when **sizehint** is specified, reads lines that **approximately** sum up to **sizehint** bytes. Each item in the returned list is always a complete line in a file. So the amount of bytes read is not exactly the same as **sizehint**.

```Python
# "hello_world.txt" file content as below.
# ========================================
# Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 
# Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. 
# Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. 
# Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
#=========================================

# on read method calls, file pointer moves forward. If you are trying out these samples on python3 repl, you either have to open and close files or seek to get the file pointer to the beginning of the file.

# read
file = open("hello_world.txt", "r")

# read the entire file contents
print(file.read())
print(file.read(100)) # only 100 bytes

file.seek(0, 0)

# reads an entire line howmuch ever its length be
print(file.readline())
file.seek(0, 0)

# read a line of size n
# if a line is 150 characters in length and if the size mentioned is 100, first call to readline returns 100 characters string and a second call returns the remaining 50 characters as string.
print(file.readline(100))
print(file.readline(100))
file.seek(0, 0)

# iterate through all lines in a file
# file itself acts as iterator returning same result as file.readline()
# exits when file.readline() returns empty string
for line in file:
  print(line)
file.seek(0, 0)

# read all the file lines to a list
lines = file.readlines()
print(str(lines))
file.seek(0, 0)

# read lines and limit for 200 characters
lines = file.readlines(200)
print(str(lines))
print(len(str(lines)))
```

## Writing to files
```Python
content = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.\nUt enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.\nDuis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur\n.Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."

# write to file in write mode
file = open("loren_ipsum.txt", "w")
file.write(content)
file.close()

# write in buffering mode
file = open("loren_ipsum.txt", "w", 1)
file.write(content)
file.flush()
file.close()

# write to file in append mode
file = open("loren_ipsum.txt", "a")
file.write(content)
file.close()

# writing a list of strings
# writelines() does not add line separators, so you’ll have to remember to put in the extra \n characters yourself.
file = open("loren_ipsum.txt", "w")
lines = content.split("\n")
file.writelines(lines)
file.close()
```

### Navigating in a file
`file.tell()` - returns file's current position.
`file.seek(offset, [whence])` - moves the file pointer to the seek position based on whence. Valid values for **whence** are 0, 1 and 2. 0 denotes starting of the file, 1 denotes current file position and 2 denotes end of the file. **For whence values 1 and 2, offset must be 0.**

**NOTE** - seek cant be performed on all file objects.

### closing files
`file.close()`. explicit closing is recommended. calling `close()` more than once is allowed.

---

## References:

* [Python3 for absolute beginners](https://www.amazon.in/Python-Absolute-Beginners-Tim-Hall/dp/1430216328)