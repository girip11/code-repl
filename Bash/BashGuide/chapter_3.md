# Chapter-3

## Comments
Text following **#** is a comment. We can use this comment statement liberally to describe about a complex logic in the bash script
```Bash
# This is a bash comment. 
# prints hello world to stdout
echo "Hello world"
```

## Commands and arguments
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

## Quotes
Quote any string that may contain spaces, tabs, newlines, special characters. Double quotes is commonly used. Escaping is done using backslash. 
```Bash
str1="Hello  world"
echo $str1

# For instance to have double quotes in a string, we have to escape the double quotes in the string.
str2="\"Tennis\" is an awesome sport"
echo $str2
```

## Internal Field Separator(IFS)
Default IFS are space(' '), tabs('\t') and newlines('\n').
```Bash
# ceching IFS settings in a shell
printf %q "$IFS"

# setting IFS to custom value
# helps delimit comma separated values.
IFS=,
```

---

## References:
* [Bash Guide by Joseph Deveau](https://www.amazon.in/BASH-Guide-Joseph-DeVeau-ebook/dp/B01F8AZ1LE/ref=sr_1_4?keywords=bash&qid=1564983319&s=digital-text&sr=1-4)