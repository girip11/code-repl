# Writing own ruby methods

* Method definition. Return value of a method is the return value of the last statement executed in that method. Parameters are put in to stack left to right.

~~~ruby
# Omit paranthesis on methods with no parameters
def say_hello_world
  puts "hello world"
end

puts say_hello_world

# recommended to enclose method parameters within paranthesis
def say_hello(name)
  puts "Hello #{name}"
end

# recommended to enclose method arguments with in paranthesis
puts say_hello('John')

~~~

* Since everything in ruby is an object, parameters are variables that are references to the underlying object. If the underlying object is mutable, then that object state can be modified using the references that the parameters hold

~~~ruby
def lower_case(input)
  # inplace case conversion
  input.downcase!
end

str = "Hello"
puts str
lower_case(str)
puts str
~~~


## Default Parameter Value

~~~ruby
def say_hello(first_name, last_name="")
  puts "Hello #{first_name} #{last_name}"
end
~~~

## Aliasing Methods

> * alias creates a new name that refers to an **existing method, operator, global variable, or regular expression backreference** ($&, $`, $', and $+).
> * Local variables, instance variables, class variables, and constants may not be aliased.
> * The parameters to alias may be names or symbols.

* aliased method name refers to the method body at the timeof aliasing. If the method is redefined, alias is not updated to point to the new method definition.

~~~ruby
#  alias new_method_name old_method_name
def say_hello(name)
  puts "Hello #{name}"
end

alias greet say_hello

puts greet("John")
puts say_hello("John")
~~~

## Variable Arguments

~~~ruby
# args is an array
def print(*args)
  args.each do |arg|
    puts arg
  end
end


print
print("Hello", "World")
~~~

* Varargs paramaeter can be placed at any parameter position.

~~~ruby
def var_args(a,*x,b)
  puts a, b
  x.each do |arg |
    puts arg
  end
end

# a= "I"
# Array X = ["new", "to", "ruby"]
# b = "programming"
var_args("I", "new", "to", "ruby", "programming")
~~~

## Bang (!) methods

* Marks the method as dangerous version of the same method without **!**.

* Bang version of methods either

  * modify state of the receiver object inplace. Ex: String `downcase` and `downcase!`
  * raise exception. Ex: Rails activerecord model `save` and `save!`

## Methods ending with **?**

* Methods ending with **?** usually return a boolean value or nil or a valid value(since ruby can evaluate any such value to **true**)

## References

* [Writing own ruby methods](http://rubylearning.com/satishtalim/writing_own_ruby_methods.html)
