# Fun with strings

* In ruby, strings are mutable.

* `puts` invokes to_s on the non string object passed to it to get its string representation.

~~~ruby
# single and double quotes can be used
str = 'Hello World'
puts str

# string concatenation
puts "Hello " + "World"

# string append using <<
str << "Welcome
to planet Earth"

# HERE document
commands = <<END_STR
ls / | grep -i etc
pidof irb
END_STR

# This way we can execute a shell script
system(commands)
~~~

## Executing Shell commands from ruby

* In ruby, shell commands can be executed by enclosing the command within **backticks**.

  ~~~Ruby
  # output of the command displayed by puts
  puts `ls`
  ~~~

* Shell commands can also be executed using **system** method from kernel module. This spawns a separate process to execute the command. This function returns

  * `true` when command executed successfully
  * `false` when command exited with nonzero exit code.
  * `nil` when failed to execute the command

  ~~~Ruby
  system("bash -version")
  ~~~

## String interpolation

Placing `#{ruby_expression}` within double quotes evaluates the ruby expression and replaces the `#{}` with the expression value.

~~~ruby
name = gets.chomp
puts "Hello #{name}"

def get_square(n)
  n*n
end

puts "Value of 2 * 2 is #{get_square(2)}"
~~~

## References

* [Fun with strings](http://rubylearning.com/satishtalim/fun_with_strings.html)
