# Chapter-5

## Variables
Variables hold some value. Based on the value it holds its type can be integer, string or array.
```Bash
# Variable declaration and initialization
# identifier=value. No space allowed between identifier, = and value. Otherwise bash considers identifier as command and = and value are its arguments.

set -xv # enables verbose debugging
declare -i count=1 # variable count holds an integer
echo $count # prints the value of count
name='Girish' # variable holds a value of type string
fruits=['Apple', 'Orange', 'Mango'] # variable holds a value of type array
```

## Strings
Single quote used to take the value as it is(literal value). Double quotes is used when **string interpolation** is required.
```Bash
# execute the below snippet and observe the difference.
# escaping doesnot work within single quotes.
name='Girish Pasupathy'
echo 'My name is $name \"'
echo "My name is \"$name\""
echo ${#name} # prints the string length
``` 

Variable value is inferred using **\$identifier**. Bash replaces value of the variable against the **\$identifier** and the executes the command.

While executing the command, Bash splits the words in to tokens using any whitespace. To pass the value of **\$identifier** unmodified to the command, enclose the **\$identifier** within quotes to make it a string argument to the command.
```Bash
movie_name="Batman           vs           Superman"
echo $movie_name  # observe does not retain spacing in the movie_name
echo "$movie_name" # retains spacing in the movie_name
```
**NOTE**: Always double quote a string which contains any whitespace (space, table or newline).

## Integers
```Bash
# Integer needs to be declared explicitly and erased explicitly.
# Syntax: declare -i variable_name=value
# unset variable_name
declare -i count=1
count+=100
echo $count
unset count

#NOTE: below statement assigns a string of value 100 to the variable. + performs string concat.
count=100
count+=10
echo $count
```

## Read only variables
**Once set, the variable cannot be unset**. Variable lifetime is till end of the shell process.
```Bash
declare -r msg="Hello world"
echo $msg
unset $msg
echo $msg
```

## Commonly used Shell variables
* $BASH
* $BASH_VERSION
* $HOME - current logged in user home directory path
* $HOSTNAME 
* $IFS - Internal Field separators
* $PWD - present working directory
* $OLDPWD - previous working directory
* $PATH - command seach path
* $PIPESTATUS - array that consists of exit codes of all the commmands in the pipe stream
* $PPID - current shell's parent PID
* $RANDOM - pseudo random integer [0 - 2^15]
* $SECONDS - script execution time in seconds.
* $UID - current user ID
```BASH
echo $RANDOM
```

Name script variables lowercase to avoid name collision with shell variables. Shell variables are used only for read only purposes. They are never set/unset. **shell variable are different from environment variables**

---

## References:
* [Bash Guide by Joseph Deveau](https://www.amazon.in/BASH-Guide-Joseph-DeVeau-ebook/dp/B01F8AZ1LE/ref=sr_1_4?keywords=bash&qid=1564983319&s=digital-text&sr=1-4)