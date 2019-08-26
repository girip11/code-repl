# Chapter-1
  Bash - Bourne-Again SHell. It is a command interpreter.

## Setting bash as default shell for user
`$SHELL` variable helps to determine the shell we are currently on. To set the default shell for a user, use the below commands
```Bash
# Default shell for a user
usermod -s /bin/bash <username>

# Setting the shell for currently logged in user through .profile
# These changes will be reflected up on current user's next login.
echo "SHELL=/bin/bash exec /bin/bash --login" >> ~/.profile
```

## Verbose debugging mode
```Bash
#!/bin/bash

# add the below line to any bash script to
# enable the verbose debugging mode.
set -xv
```

## Shell prompts
**$** - Bourne, Bash, POSIX or Korn shell
**%** - csh or zsh shell
**\#** - executing commands as root user

## Command help within the shell
```Bash
# help on man command
man --help

# man command (short for manual) displays manual pages for the command issued as its argument.
man cat

# help displays man pages for **bash builtins and keywords.**
help [[

# type commands returns the type of the argument whether its a shell keyword, builtin etc
type for

# whatis gives a short description about the command passed as argument to it. `man -f <command>` does the same.
whatis bash
man -f bash

# apropos searches short description in man page using passed argument as the keyword. `man -k <keyword/command>` does the same
apropos bash
man -k bash
```

---

## References:
* [Bash Guide by Joseph Deveau](https://www.amazon.in/BASH-Guide-Joseph-DeVeau-ebook/dp/B01F8AZ1LE/ref=sr_1_4?keywords=bash&qid=1564983319&s=digital-text&sr=1-4)