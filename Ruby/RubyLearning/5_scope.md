# Variable scopes

* Global variables have global scope. Available to entire program. Global variables start with **$**

* Builtin global variables
  * `$0` - name of ruby file under execution
  * `$:` - Directories that make up search path for loading external file
  * `$$` - pid of the ruby process

* local scope - visible within a method, class, module. Even if the variable is defined outside all the definition blocks it will still be part of the **main object scope**.

## References

* [Variable scopes](http://rubylearning.com/satishtalim/scope.html)
