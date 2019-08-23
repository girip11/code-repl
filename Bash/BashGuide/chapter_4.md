# Chapter-4

## Executables and paths
`$PATH` environment variable is used to find binaries to be executed. It is not recommended to add user scripts to `$PATH`. **If absolutely necessary, add the new path to the end of current list of paths.** Env variable paths are searched using values in `$PATH` from left to right. Usually binaries are executed in their own subshell.
```Bash
# bash binary is found inside /bin which is part of $PATH variable
bash -c "echo \"Hello world\""
# If some binary is not available on $PATH, we have to specify the absolute path for execution.
/bin/bash -c "echo \"Hello world\""
```

## Builtins
Commands builtin to bash itself. Doesnot require searching in path for execution. Examples are **alias**, **cd**, **echo**, **read**, **type** etc

To know about all the bash builtins use the command `man builtins`

## Scripts
Series of commands stored in a file and usually executed in a shell non interactively. A bash script begins with `#!/bin/bash` called the **shebang**.

## alias
Aliases help shorten long commands. If defined in a script or shell, alias is visible only within the script or shell. To make available to all shell, we have to add the alias settings to file like **.bashrc**

```Bash
#  List all aliases
alias

# to create a new alias
alias update="sudo apt update"
alias install="sudo apt install"

# Installing VIM using the alias
install vim
```

## Standard streams
* stdin - standard input stream. By default its keyboard. File descriptor is 0.
* stdout - Standard output stream. default is terminal. Fiel descriptor is 1.
* stderr - standard error stream. File descriptor is 2. this need not always be the same as stdout. To make stderr redirect to stdout `2>&1` is used.

---

## References:
* [Bash Guide by Joseph Deveau](https://www.amazon.in/BASH-Guide-Joseph-DeVeau-ebook/dp/B01F8AZ1LE/ref=sr_1_4?keywords=bash&qid=1564983319&s=digital-text&sr=1-4)