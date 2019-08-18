# Parameters
Variables are parameters that can be named.

## Positional parameters
commandline arguments to the bash script are positional parameters. Positional parameters start from index 0.

* **$0** - name of the script
* **$1, $2** - positional parameters from 0 to 9
* **${10}** - from 10th parameter onwards, the number needs to be enclosed within** inline group {}**

## Special parameters
These parameetrs can only be referenced but not modified. Contains metadata relating to exit status, process id, shell options etc.

* **$#** - number of positional parameters passed to the script
* **$\*** - all the positional parameters. If double quoted, results in a single string.
* **$@** - all the positional parameters. If double quoted, results in a list of those parameters.
* **$?** - exit code of most recently completed foreground command
* **$!** - PID of the last completed background command
* **$$** - process ID of the current shell
* **$_** - last argument of the last completed foreground command after expansion.
* **$-** - shell options that are set

## Parameter expansion
* **${parameter}** - allows characters to be appended to the **parameter** value after expansion.
* **${#parameter}** - string length
* **${parameter^}** - converts first character to uppercase. similar to **capitalize** method in python.
* **${parameter^^}** - converts the string to upper case
* **${parameter,}** - converts first character to lowercase.
* **${parameter,,}** - converts the string to lowercase
* **${parameter~}** - reverses the case of the first character.
* **${parameter~~}** - reverses the case of all the characters.

## Assigning values
**:** in the below assignment of defaults is useful when the parameter is declared but set to null.

* **\${parameter:=value}** or **\${parameter=value}**- sets default value if the parameter is not set.
* **\${parameter:+value}** or **\${parameter+value}** - substitute value for parameter if parameter is set otherwise substitute nothing.
* **\${parameter:-value}** or **\${parameter-value}** - substitute value when parameter is not set.

## Substring removal
pattern can be made of simple globs or extended globs

* **${parameter:offset:length}** - substring from offset till length number of characters.
* **${parameter#pattern}** - find the first occurrence of the pattern from start to end and remove the pattern.
* **${parameter##pattern}** - finds all the occurrence of the pattern from start to end and removes the pattern.
* **${parameter%pattern}** -find the first occurrence of the pattern from end to start and remove the pattern.
* **${parameter%%pattern}** - finds all the occurrence of the pattern from end to start and removes the pattern.

## search and replace
pattern can be made of simple globs or extended globs
* **${parameter/pattern/value}**  - replace first occurence of pattern with value 
* **${parameter//pattern/value}** - replace all occurrences of pattern with value 
* **${parameter/pattern}** - replace first occurrence of pattern with null string. 
* **${parameter//pattern}** - replace all occurrences of pattern with null string.


---

## References:
* [Bash Guide by Joseph Deveau](https://www.amazon.in/BASH-Guide-Joseph-DeVeau-ebook/dp/B01F8AZ1LE/ref=sr_1_4?keywords=bash&qid=1564983319&s=digital-text&sr=1-4)

* [Parameter substitution](https://www.tldp.org/LDP/abs/html/parameter-substitution.html)
* [Bash special parameters](https://www.gnu.org/software/bash/manual/bash.html#Special-Parameters)
* [$! usage](https://unix.stackexchange.com/questions/85021/in-bash-scripting-whats-the-meaning-of)