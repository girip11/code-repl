# Bash guide
  Bash - Bourne-Again SHell. It is a command interpreter.

## Chapter-1
### Setting bash as default shell for user
`$SHELL` variable helps to determine the shell we are currently on. To set the default shell for a user, use the below commands
```Bash
# Default shell for a user
usermod -s /bin/bash <username>

# Setting the shell for currently logged in user through .profile
# These changes will be reflected up on current user's next login.
echo "SHELL=/bin/bash exec /bin/bash --login" >> ~/.profile
```

### Shell prompts
**$** - Bourne, Bash, POSIX or Korn shell
**%** - csh or zsh shell
**\#** - executing commands as root user

### Command help within the shell
```Bash
# help on man command
man --help

# man command (short for manual) displays manual pages for the command issued as its argument.
man cat

# help displays man pages for bash builtins and keywords.
help [[

# type commands returns the type of the argument whether its a shell keyword, builtin etc
type for

# whatis gives a short description about teh command passed as argument to it. `man -f <command>` does the same.
whatis bash
man -f bash

# apropos searches short description in man page using passed argument as the keyword. `man -k <keyword/command>` does the same
apropos bash
man -k bash
```

---

## Chapter-2
### Editors
Editors recommended for bash scripting are one of the following
* emacs
* vim
* nano
* gedit

---

## Chapter-3
### Comments
Text following **#** is a comment. We can use this comment statement liberally to describe about a complex logic in the bash script
```Bash
# This is a bash comment. 
# prints hello world to stdout
echo "Hello world"
```

### Commands and arguments
Arguments can be separated by space, tab or newline
```Bash
# ls is a command. 
# commands can have options and arguments
# -l is a option passed to the ls command
# /bin is the argument passed to the ls command
ls -l /bin

# To learn more about ls command options
man ls
```

### Quotes
Quote any string that may contain spaces, tabs, newlines, special characters. Double quotes is commonly used. Escaping is done using backslash. 
```Bash
str1="Hello  world"
echo $str1

# For instance to have double quotes in a string, we have to escape the double quotes in the string.
str2="\"Tennis\" is an awesome sport"
echo $str2
```

### Internal File Separator(IFS)
Default IFS are space(' '), tabs('\t') and newlines('\n').
```Bash
# ceching IFS settings in a shell
printf %q "$IFS"

# setting IFS to custom value
# helps delimit comma separated values.
IFS=,
```

---

## Chapter-4
### Executables and paths
`$PATH` environment variable is used to find binaries to be executed. It is not recommended to add user scripts to `$PATH`. **If absolutely necessary, add the new path to the end of current list of paths.** Env vaiable paths are searched using values in `$PATH` from left to right. Usually binaries are executed in their own subshell.
```Bash
# bash binary is found inside /bin which is part of $PATH variable
bash -c "echo \"Hello world\""
# If some binary is not available on $PATH, we have to specify the absolute path for execution.
/bin/bash -c "echo \"Hello world\""
```

### Builtins
Commands builtin to bash itself. Doesnot require searching in path for execution. Examples are **alias**, **cd**, **echo**, **read**, **type** etc

### Scripts
Series of commands stored in a file and usually executed in a shell non interactively. A bash script begins with `#!/bin/bash` called the **shebang**.

### alias
Aliases help shorten long commands
```Bash
#  List all aliases
alias

# to create a new alias
alias update="sudo apt update"
alias install="sudo apt install"

# Installing VIM using the alias
install vim
```
### Standard streams
* stdin - standard input stream. By default its keyboard. File descriptor is 0.
* stdout - Standard output stream. default is terminal. Fiel descriptor is 1.
* stderr - standard error stream. File descriptor is 2. this need not always be the same as stdout. To make stderr redirect to stdout `2>&1` is used.

---


## Chapter-5
## References:
* [Bash Guide by Joseph Deveau](https://www.amazon.in/BASH-Guide-Joseph-DeVeau-ebook/dp/B01F8AZ1LE/ref=sr_1_4?keywords=bash&qid=1564983319&s=digital-text&sr=1-4)