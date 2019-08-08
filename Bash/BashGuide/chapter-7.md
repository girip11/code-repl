# Chapter-7: Special characters

## Special characters
**$** - variable value fetching

**"** - string 

**\#** - comment

**whitespace** - used for word splitting

**&** - run in background

**;** - statement separator. multiple commands in the same line are separated by **;**

**$$** - expands to the PID of the current shell

```bash
# run editor in background
gedit &

# statement separation
echo "hello world" echo $(pwd) # prints "hello world echo /home/girish"
echo "hello world"; echo $(pwd);
```

## Logical operators
**&&** - logical AND
**||** - logical OR
Commands return exit code **0(zero)** on success.
```Bash
cd scripts_dir || mkdir scripts_dir && cd scripts_dir
```

## directory traversal
* **~** - home directory of currently logged in user
* **.** - current directory
* **..** - parent directory of current directory. parent directory of root directory is itself.
* **/** - filename/path separator

## Quoting
Use string quoting whereever **word splitting using whitespace** can happen.

* **''** - represents a string literal. No character has a special meaning inside single quotes.

* **""** - represents string. parameter expansion, arithmetic expansion, command substitution are carried out. Can be thought of similar to **String interpolation** in programming languages

* **\\** - escape character. 
```Bash
my_planet="Earth"
echo 'The planet that I live in is: ${my_planet}'
echo "The planet that I live in is: ${my_planet}"
echo "The planet that I live in is: \"${my_planet}\""
```

**NOTE**: To avoid any special processing of a string use single quotes, in all other cases use double quotes. 

## Redirection
**>** - redirects standard output (usually we redirect to a file)

**>>** - redirects and appends standard output to the target (usually we redirect to a file)

**<** - redirects standard input. (read contents of a file)

**<<** - Here document. reads string until a delimited is specified.

**<<<** - Here string. reads string that follows immediately

**|** - redirects stdout of a command to stdin of another command.


## Groups
**{} Inline group**  - commands within braces are tread as single command. **Final command must be terminated with semicolon**.
```bash
cd my_dir || {mkdir my_dir; cd my_dir;}
```

**() command group** - commands within are executed in a separate subshell. subshell vairables are not visible to the parent shell. Executing many commands in subshell might slowdown the script execution.
```bash
var1='foo'
var2='bar'
greeting="Hey"
# below statement is executed in a subshell
(greeting="Hello"; echo "$greeting, $var1 and $var2")

# below statement is executed in current shell
# $greeting variable was defined in subshell and not known to the parent shell.
echo "$greeting, $var1 and $var2"
```

**(()) arithmetic expression** - enclosing arithmetic expressions. Bash knows only integer math. Arithmetic expressions when used for condition test **returns 0 on true and 1 on false.**
```bash
x=1;y=2;z=3;
echo $((x + y * z))  # arithmetic expansion
result=$((x + y * z))
echo $((result == 7))
echo $(($result == 7)) # in arithmetic expression parameter dereferencing($) is optional
```

**NOTE**: Commands groups and arithmetic expression can be expanded by preceding them with **$**. This is referred to as **command substitution and arithmetic expansion** respectively

## let built-in
**let** is a built-in command for math operations.
Arithmetic expressions don't enforce strict spacing. 
```Bash
let z=5
let z=$z+1
let z=z+1 # $ is optional

# to have spaces in arithmetic expression when using with let enclose the expression in double quotes.
let "z = z + 1"
echo $z
```

## Floating point and complex arithmetic
We need to use external utility like **bc**


## read builtin
Reads a line of text from standard input. **newline** is considered as the end of line. But it can be changed using **-d** option. After reading the line, read performs word splitting as per IFS (Internal Field Separators). Value read is assigned to the variable used in the command. If no variable is used, the value is stored in the variable called **REPLY**. 
**read** returns non zero exit code(failure) when EOF (Ctrl + D) is encountered
Some of the important options are

* **-a** - store read words in to indexed array
* **-d** - change the delimiter which is **newline** by default
* **-r** - read the input as raw string literal(as if text is enclosed within single quotes)
* **-p prompt** - before starting to read, print the prompt on console
* **-i initial_text** - use this as initial text when reading from console using option **-e**. 
* **-s** - silent. Dont display text typed on screen
* **-t** - timeout in seconds. can be a fraction. if not specified, default value is taken from shell variable **TMOUT** if available. If timeout is 0, read returns success if input was avaiable to read.
* **-u** - read from file desscriptor instead of standard input


```Bash
# reads input type and stores as array in variable words
read -e -a words
echo "${words[@]}"

# read silent and raw string from console
read -ers -a input
echo ${input[@]}

read -e -p "Type here:" -i "Content is:"  content
echo "$content"

echo "hello world" | (read; echo "$REPLY")
```

---

## References:
* [Bash Guide by Joseph Deveau](https://www.amazon.in/BASH-Guide-Joseph-DeVeau-ebook/dp/B01F8AZ1LE/ref=sr_1_4?keywords=bash&qid=1564983319&s=digital-text&sr=1-4)
* [read builtin](https://www.computerhope.com/unix/bash/read.htm)
* [Advanced bash scripting guide](https://www.tldp.org/LDP/abs/html/arithexp.html)