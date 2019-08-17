# Input and output

**Input** - positional parameters, special parameters, files, streams, pipes, shell and environment variables.
**Output** - files, streams, pipes, shell and environment variables.

## Positional and special parameters
* **\$1** - positional
* **\$?** - special parameters.

## Shell variables
shell variables are local to shell while environment variables are system wide.

## Environment variables
commonly used ones are listed below. For exhaustive list refer the book.
| Variable | Description                          |
| -------- | ------------------------------------ |
| HOME     | current user's home directory        |
| HOSTNAME | system's name                        |
| PATH     | search path for commands             |
| PWD      | current working directory            |
| SHELL    | path to current user's shell program |
| USER     | currently logged in user             |

* Full listing of the environment variable is obtained using the `printenv` command.
* `export` - add or change environment variable.
* `unset` - remove the environment variable.

```Bash
# complete list of environment variables
printenv

# get the currently set value of the environment variable
printenv USER

# add my_dir to PATH
export PATH="$HOME/my_dir:$PATH"

# unset SHELL and add bash as the new value
unset SHELL
export SHELL="/bin/bash"
```

Environment variables of running programs cannot be changed. Changes made in current shell will reflect in any of its child processes only.

Changes made to environment variables are valid only during the lifetime of the shell program unless persisted in one of the below files.
* ~/.pam_environment
* ~/.bashrc
* ~/.profile
* /etc/environment

Current user login and logout to reflect changes in evnironment variable.

* In scripts use **source** or **exec** to reread/refresh environment changes.
```Bash
source <path to script containing environment variables>

# or

exec bash
```

## Standard streams
* stdin
* stdout
* stderr

## File descriptors (FD)
FD - access file, stream ,pipe, socket, device, network interface etc.

* abstraction between the hardware device and the device file created by kernel(/dev directory).

| stream | Default  | FD  |
| ------ | -------- | --- |
| stdin  | keyboard | 0   |
| stdout | console  | 1   |
| stderr | console  | 2   |

## Reading using custom file descriptors
```Bash
# open a file for reading using custom file descriptors
exec 3< file

# once a shell is opened using this file descriptor
# input can be read from this file by specifying the file descriptor
# for example
read -u 3 line # read a line from the file
echo $line
```

Redirect a custom file descriptor to stdin of a command
```Bash
# redirects FD3 to stdin of grep
grep -i "foo" <&3
```

Closing the file using file descriptor.
```Bash
# By redirecting 3 to **-**, bash closes the file with FD 3
exec 3>&-
```

## Writing to file using custom file descriptors
```Bash
# open a file for writing
exec 4>file

# redirecting stdout
echo "hello world" >&4

# closing the file using the file descriptor
exec 4>&-
```

Opening a file for reading and writing using file descriptor is done using the **<>** diamond operator.
```Bash
exec 3<>file
# writing
echo "hello world" >file

# reading from file
read -u 2 line

# closing the file
exec 5>&-
```

## File redirection
Output redirection carried out using **>** or **>>**. Ex: redirect output of a program from console(default) to a file.

* Redirection to file using **>** - creates non existent file and overwrites the existing file.

* Redirection to file using **>>** - creates non existent file and appends to the existing file.

* Just **>& or &>** redirects stderr to stdout, for instance `command >&file`

```Bash
# output written to file and not on console.
echo "Hello world" > output.txt
```

Input redirection is done using **<**.
```Bash
# reads the content of file output.txt
cat output.txt

# or using input redirection. contents of file available to as stdin. Here stdin points a file rather than to input frmo keyboard(default)
cat < output.txt
```

## Redirection using file descriptors
[Article on bash redirection](https://catonmat.net/bash-one-liners-explained-part-three)

```Bash
# redirect stdout to file
echo "This text gets stored in the file" > output.txt

# redirect stdout to file using file descriptor
echo "This text gets stored in the file" 1> output.txt

# file to stdin
cat < output.txt

# input redirection using file descriptor
cat 0< output.txt 
```

**/dev/null** - null device (discards anything written to it). When output and error are to be ignored, redirect stdout and stderr to this.

Redirect stderr to stdout using **FD1>&FD2**. File descriptors are read from **left to right**

```Bash
# common use case. ignore stdout and stderr
./my_script.sh 2>&1 > /dev/null

# shorthand notation for above command
./my_script.sh &>/dev/null

# common use case. redirect both stdout and stderr to a file. this is the **correct** version
# 1. redirect FD1 to file
# 2. duplicate FD1 and place it in place of FD2
./my_script.sh > my_script.log 2>&1

# below version is **not correct**
# 1. duplicate FD1 and place it in place of FD2
# 2. redirect FD1 to file
# because duplication happened before redirection, FD2 never gets redirected to FD1
# in this case only stdout is captured in the file.
# stderr is still directed to the console(default)
./my_script.sh 2>&1 > my_script.log 
```

## Here document
used for embedding text(multiline string) into script. **EOF** is a commonly used delimiter. **supports parameter substitution**. By default preserves tabs and spacing.

```Bash
# Syntax
# data between the DELIMITER redirected to the stdin
command <<DELIMITER
data string
DELIMITER

# Example
name="Batman"
cat <<EOF
  Character name is $name
EOF

# prevent parameter substitution by quoting the starting DELIMITER
cat <<"EOF"
  Character name is $name
EOF

# ignore spacing by prefixing the starting delimiter with **-**
cat <<- EOF
  Character  name is $name
EOF
```

## Here string
places single line of string to the stdin of the command. Supports **parameter substitution** within **double quoted strings**.
```Bash
# Syntax
command <<< "Input string"

# example.
# for this to work, the command should read its input from the **stdin**
cat <<< "Print this to console"
```

## FIFO(named pipe)
**F**irst **I**n **F**irst **O**ut. Create FIFO using `mkfifo` command. No contents stored on teh file system. Kernel passes the data internally.

* FIFO blocked by read operation, until a write operation it remains blocked and vice versa.

* FIFO file have user permissions.

## Pipe
Connects stdout of one command to stdin of another. Each command following a pipe is executed in its subshell.

```Bash
# stdout of first command to stdin of second command
cat planets.txt | grep -i "earth"

# to redirect both stdout and strerr to stdin use |&
cat planets.txt |& grep -i "earth"

# or
cat planets.txt 2>&1 | grep -i "earth"

echo "${PIPESTATUS[@]}"
```

`PIPESTATUS` array saves the exit codes of all the commands in the pipe stream.

## Process substitution
Allows to pipe stdout of multiple commands to another command. 
```Bash
# syntax
command <(list)
command >(list)

# example
# comm is a command to compare two sorted files
# comm --help
# finding unique lines to each file
comm -3 <(sort file1 | uniq) <(sort file2 | uniq)
```

Bash replaces <() or >() with a file descriptor of a named pipe that it created. command will be writing to the named pipe while the **list** inside () will be connected to the same named pipe awaiting any input available for read.

In process substitution, bash handles the FIFO files.
* Input substitution - **<()**
* Output substitution - **>()**

```Bash
# in the output, observe the file descriptor created and used by bash to execute this command.
wc -l < (cat planets.txt)

wc -l < (grep -i "ar" planets.txt)
```

Redirecting stdout to one command while redirecting stderr to another command using process substitution is possible
```Bash
# bash replaces >() with a file descriptor.
# command inside >() listens to the file descriptor(blocked till someone writes)
# when the command executes, the output and error gets redirected to respective files and those commands get unblocked.
command > >(stdout_cmd) 2> >(stderr_cmd)

# after FD replacement above command looks as
# command 1> fifo_file1 2> fifo_file2
```

## tee utility
tee takes an input stream and duplicates it to a file and stdout.

```Bash
# command -> tee -> stdout
#             |
#           file
command | tee file
```

## **read** built-in construct
* read data from stdin, file or file descriptors into a variable. Refer [Chapter_7](./chapter_7.md)


## swap stdout and stderr
```Bash
# duplicate FD3 to stdout
# duplicate FD1 to stderr
# duplicate FD2 to stdout
# close the FD3
command 3>&1 1>&2 2>&1 3>&-
```

---

## References:
* [Bash Guide by Joseph Deveau](https://www.amazon.in/BASH-Guide-Joseph-DeVeau-ebook/dp/B01F8AZ1LE/ref=sr_1_4?keywords=bash&qid=1564983319&s=digital-text&sr=1-4)
* [Bash redirection](https://catonmat.net/bash-one-liners-explained-part-three)
* [Process substitution - linuxjournal](https://www.linuxjournal.com/content/shell-process-redirection)
* [Process substitution - tldp](https://www.tldp.org/LDP/abs/html/process-sub.html)
