# Bash scripting good practices

* Script should return zero on success and non-zero on failure.

## Good practices on functions

* Function documentation example

```Bash
function hello_world() {
  # @description This function prints the message
  # @description hello world on to the terminal
  echo "Hello world"

}
```

* Functions are like scripts they return only integers. Use global variables **RESULT**, **EXCEPTION** and **EXCEPTION_MSG** to store the result, error code and error message respectively.

## Variables

* use **local** keyword to define local variables, else the variables become globally available within the script after the function has been executed atleast once. Use readonly variables whenever possible. Use the **readonly** shell builtin. `help readonly` to knwo about the usage of this shell builtin.

* Assign meaningful names to the function parameters since functions receive parameters as special variables like $1, $2 etc.

* Raise error on accessing unset variable access using the command `set -o nounset`.

## Traps

```Bash
function Main__interruptHandler() {
    # @description signal handler for SIGINT
    echo "SIGINT caught"
    exit
}
function Main__terminationHandler() {
    # @description signal handler for SIGTERM
    echo "SIGTERM caught"
    exit
}
function Main__exitHandler() {
    # @description signal handler for end of the program (clean or unclean).
    # probably redundant call, we already call the cleanup in main.
    exit
}

trap Main__interruptHandler INT
trap Main__terminationHandler TERM
trap Main__exitHandler EXIT

function Main__main() {
    # body
}

# catch signals and exit
trap exit INT TERM EXIT

Main__main "$@"
```

## References

* [Stackoverflow: Best practices for shell scripts](https://stackoverflow.com/questions/78497/design-patterns-or-best-practices-for-shell-scripts)

* [Shell script common mistakes](http://www.pixelbeat.org/programming/shell_script_mistakes.html)
