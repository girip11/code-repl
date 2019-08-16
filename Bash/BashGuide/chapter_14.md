# Functions

```Bash
# function syntax
function function_name() {
  # commands
}

# alternate syntax
function_name() {
  #commands
}

# example
function simple_function() {
  echo "Hello world"
}

# calling the function
simple_function
```
Function definition must precede its call. Call to empty function also results in error. Function must have atleast 1 command.

Function call is equivalent to a command. Nesting of functions is possible.

Functions can access and modify global variables. local variables inside a function are not visible outside. local variables are defined using the `local` keyword.

Inside a function, local variable hides the global variables with the same name.
```Bash
function print_message(){
  local msg="Hello world"
  echo "$msg"
}
```

## Parameter to functions
Function parameters are accessed as positional parameters starting from $1 similar to a script.

```Bash
function say_hello() {
  echo "Hey, $1"
}

say_hello "Roger Federer"
```

Functions do not have access to the script parameters directly unless passed as parameters in the function call.

Functions in bash does not return any value. returns just the exit code.

```Bash
function get_value() {
  return 10
}
get_value
echo $? # this way we can return values.
```

---

## References:
* [Bash Guide by Joseph Deveau](https://www.amazon.in/BASH-Guide-Joseph-DeVeau-ebook/dp/B01F8AZ1LE/ref=sr_1_4?keywords=bash&qid=1564983319&s=digital-text&sr=1-4)
