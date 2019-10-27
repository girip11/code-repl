# Conditional blocks

0 is true, any other value is false.

## Exit codes

* value between 0 - 255
* 0 is success, 1 default value for failure
* `true` and `false` are two commands that do nothing, but return exit codes 0 and 1 respectively.
* **$?** to get the previous foreground command exit status.
* **exit** built-in. return exit code from script.

```Bash
true
echo $?

false
echo $?
```

## Standard exit codes

| Exit code | description                   |
| --------- | ----------------------------- |
| 0         | success                       |
| 1         | failure                       |
| 2         | shell builtin incorrect usage |
| 126       | command cannot execute        |
| 127       | commadn not found             |
| 128       | incorrect exit code argument  |
| 128 + num | fatal error signal "num"      |
| 130       | script killed with Ctrl + C   |
| 255*      | Exit code out of range        |

## If

`if-elif-else` statements can be nested

```Bash
# if syntax
# statements are executed if the expression evaluates to true which is 0
if expression
then
  # statements to be executed when expression returns true
else
  # statements to be executed when expression returns false
fi

# example
if true
then
  echo "hello"
fi

# multiple conditions syntax
if expression_1
then
  # statements
elif expression_2
then
  # statements
else
  # statements
fi
```

## Case statement

searches in order, executes first matching pattern. **globs**(wildcards and extended globs set using shell option) can be used in **pattern matching**.

```Bash
# Syntax
case variable in
pattern1)
  # statements
  ;;
pattern2|pattern3)
  # statements
  ;;
*)
  # statements
  ;;
esac
```

## Select

Uses `PS3` variable to print its prompt. Prompts user to make decision.User enters a number starting from 1 till the number of items in the values to be selected. Executes in loop till break keyword.

```Bash
# Syntax
# PS3="Prompt title here"
# select variable in value1, value2.... valueN
# do
#   # statements
#   break
# done

PS3="Select the fruit you like: "
fruits=("apple" "mango" "pineapple" "orange" "exit")
select fruit in "${fruits[@]}"
do
  if [[ $fruit == "exit" ]]
  then
    echo "Exiting..."
    break
  fi
  echo "Favorite fruit is : $fruit"
done
```

## Conditionals

| condition | descriptions                                                                                                                                  |
| --------- | --------------------------------------------------------------------------------------------------------------------------------------------- |
| !         | Negates a test or exit status                                                                                                                 |
| \[ \]     | tests expression in brackets and returns true or false. shell builtin. consider it obselete. same as the **test** builtin. Offers portability |
| \[\[\]\]  | tests expression in brackets and returns true or false. more flexibility than above tes. Affects portability since POSIX doesnot support this |

## Differences between \[ \] and \[\[ \]\]

* within \[ \], variables should be quoted.
* values should be escaped within \[ \]
* \[ \] uses **-a** for logical and and **-r** for logical or while \[\[ \]\] can use && and ||
* \[\[ \]\] can perform pattern matching using **=** operator and regular expression matching using **=~** operator.

**NOTE**: \[ \] is a sh test. it is obsolete. Always use \[\[ \]\] in bash scripting.
`help test` gives notes on various tests available

## Arithmetic tests

Comparison operators

* **-eq** - equals
* **-ne** - not equals
* **-lt** - less than
* **-le** - less than or equal to
* **-gt** - greater than
* **-ge** - greater than or equal to

## String tests

* **-z** - true if string is empty
* **-n** - true if string is not empty
* **string1 = string2** - equals
* **string1 == string2** - equals
* **string1 != string2** - not equals
* **string1 < string2** - lexicographic comparison
* **string1 > string2** - lexicographic comparison
Bash specific regex string comparison
* **string1 =~ string_regex** - regex equals

  ```Bash
  msg="hello"

  # ! negate the test espression result
  if [[ ! -z $msg ]]
  then
    echo "message is not empty"
  fi

  # () group expressions, causing change in precedence.
  if [[ ( cond1 && cond2 ) || cond3 ]]
  then
    # statements
  fi
  ````

## File tests

Commonly used file tests are listed below. For more tests turn to the reference book.

* **-e FILE** - true if file exists
* **-f FILE** - true if exists and regular file
* **-d FILE** - true if FILE exists and is a directory
* **-p FILE** - true if FILE exists and named pipe file
* **-S FILE** - true if FILE exists and socket file
* **-h FILE** - true is FILE exists and is symbolic link
* **-O FILE** - true FILE exists and owned by currently logged in user (user whose context the BASH is executing)
* **-G FILE** - true if exists and owned by group of bash user
* **-r FILE** - true exists and readable by bash user
* **-w FILE** - true if exists and writable
* **-x FILE** - true if exists and executable
* **-s FILE** - true if exists and nonempty
* **FILE2 -nt FILE2** - newer than
* **FILE1 -ot FILE2** - older than

## Logical tests

Only supported inside `[[]]`

* **expr1 && expr2** - logical AND
* **expr1 || expr2** - logical OR

## Pattern tests

Only supported by `[[]]`

* **string = pattern** or **string == pattern**- true if string matches pattern
* **string =~ pattern** - true if string matches **pattern regex**.

### Character classes for pattern matching

| class  | description               |
| ------ | ------------------------- |
| alnum  | alpha and digit           |
| alpha  | lower and upper           |
| ascii  | ASCII characters          |
| blank  | space and tab             |
| cntrl  | control characters        |
| digit  | [0-9]                     |
| graph  | alnum and punct           |
| lower  | lowercase characers [a-z] |
| print  | alnum + punct + space     |
| punct  | punctuation characters    |
| space  | ' ', \t, \n, \r           |
| upper  | [A-Z]                     |
| word   | alnum + "_"               |
| xdigit | hexadecimal digits        |

```Bash
# Syntax
# [[:class:]]
msg="Hello"

# check if every characters in the message is alphabet
for ((i=0; i<=${#msg}; i++))
do
  if [[ ${msg:$i:1} == [[:alpha:]] ]]
  then
    echo "Current character is a alphabet"
  fi
done
```

## Miscellaneous

* **-o OPT** - true if shell option is set (option that was set using the **set builtin** and not using **shopt builtin**).

* **-v VAR** - true if shell variable is set.

```Bash
# Other options that can be set using set buitlin
# `help set` for more information on options that can be set using the **set** shell buitlin.
if [[ -o braceexpand ]]
then
  echo "braceexpand option is set"
fi

if [[ -v BASH_VERSION ]]
then
  echo "$BASH_VERSION"
fi
```

---

## References

* [Bash Guide by Joseph Deveau](https://www.amazon.in/BASH-Guide-Joseph-DeVeau-ebook/dp/B01F8AZ1LE/ref=sr_1_4?keywords=bash&qid=1564983319&s=digital-text&sr=1-4)
* [Arithmetic expressions with if](https://stackoverflow.com/questions/8304005/how-do-i-do-if-statement-arithmetic-in-bash)
* [Difference between \[ \] and \[\[ \]\]](https://stackoverflow.com/questions/3427872/whats-the-difference-between-and-in-bash)
* [Character classes and bracket expressions](https://www.gnu.org/software/grep/manual/html_node/Character-Classes-and-Bracket-Expressions.html)
