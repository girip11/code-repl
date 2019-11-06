# Names in Ruby

* Names in ruby - start with underscore or alphabet (lower and uppercase) followed by alphabets, digits or underscores.

* Variables hold references to objects. A variable can hold any type of object. Ruby does automatic garbage collection.

## Variables

* Local variable start with underscore or alphabet (lower and uppercase) followed by alphabets, digits or underscores.

* Instance variables start with @ followed by alphabets, digits or underscores.

* Class variables start with @@ followed by alphabets, digits or underscores.

* Global variables start with $ followed by alphabets, digits or underscores.

## Constants

Constant name starts with uppercase. Constants also follow snake_case naming convention with all the letters capitalized. Interpreter **issues warning** when constants are reassigned. Constants should follow this naming convention for the interpreter to recognize the name as constant.

* Example `RUBY_VERSION`

## Methods

Method name starts with lowercase and follow **snake_case** naming convention. Methods can have **?** **!** or **=** as its suffix.

## Classes and Modules

Class and module names follow **Pascal case** naming convention.

## Ruby basic types

The basic types in Ruby are Numeric (subtypes include Fixnum, Integer, and Float), String, Array, Hash, Object, Symbol, Range, and RegExp.

Class **Object** provides `class` method that returns the class of the object.

~~~ruby
puts 6.class

# Listing instance methods on a class
puts String.instance_methods.sort
~~~

We can find out which object context we are currently in using the special variable **self**.

~~~ruby
# Interpreter irb prints main
# main is a special object
puts self
puts self.class

# If you add a method in the interpreter
# that method is added to the Object class
def say_hello(name)
  puts "Hello #{name}"
end

# You can find the method say_hello in the list
puts Object.public_methods.sort
~~~

## References

* [Names in Ruby](http://rubylearning.com/satishtalim/ruby_names.html)
* [More on Ruby Methods](http://rubylearning.com/satishtalim/more_on_ruby_methods.html)
