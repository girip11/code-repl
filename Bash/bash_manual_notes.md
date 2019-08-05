# Bash shell programming
Bash shell programming syntax and constructs.

## Introduction
Bash - **B**ourne **A**gain **SH**ell. Default shell of GNU operating system. Bourne shell is the unix shell (sh). Largely compatible with **sh**. Portable to other OS.

## Basic shell features
### Quoting
Bash supports single quotes and double quotes. 
* Within **single quotes**, all characters hold their literal meaning. Escaping, string interpolation doesnot work within single quotes.
* Within **double quotes** string interpolation and escaping works. 
```Bash
# String interpolation and escaping
name="Girish"
echo "Hello \"$name\""
```

### Shell options
Bash shell options can be accessed using command `shopt`. 

### Shell commands
* Shell command returns zero on success and **128 + n** on failure where **n** is the exit code on failure.

### Pipelines
* Pipeline is a sequence commands separate by '|' or '\&'
  ```Bash
  # pipeline format
  # preceeding exclamation negates the exit status of the command
  [!] command1 [| or |& command2]
  ```
* In piping, output of the first command is redirected to the input of the second command.'|&' redirects standard error and standard output of command1 to the standard input of command2.
* `command1 2>&1 | command2` is written succinctly as `command1 |& command2`
* Each command in the pipeline is run in its own subshell. Exit status of the pipeline is the esit status of the last command in the pipeline.
* If **pipefail** shell option is enabled then, the exit status of the pipeline is the exit code of last command to return with non-zero exit code(pipe exits with the first command to fail in the pipeline). 

### List of commands
* A list is a sequence of one or more pipelines separated by one of the operators ‘;’, ‘&’,
‘&&’, or ‘||’, and optionally terminated by one of ‘;’, ‘&’, or a newline.
* &&, || have equal precedence and are **left associative**.
  ```Bash
  # logical and
  cmd1 && cmd2

  # logical
  cmd1 || cmd2
  ```
* **;, &** have equal precedence. 
* Commands delimited with **&** cause the command to execute in the background by the shell executing the command.
* Commands ending with **;** executed synchronously. 

## Reference:
[Bash Manual]() 
