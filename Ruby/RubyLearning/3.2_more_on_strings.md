# More on Strings

In single quoted strings, ruby does very little additional processing.

> In single-quoted strings, a backslash is not special if the character that follows it is anything other than a single quote or a backslash

In double quoted strings, following computations happen

* Substitute escaped characters with binary value. Ex '\n'
* Look for expression interpolation

**NOTE:**. New String object created on every string literal  used in assignment or as parameter.

## Commonly used `String` methods

* `length`
* `upcase`. Inplace version `upcase!`
* `downcase`. Inplace version `downcase!`
* `reverse`. Inplace version `reverse!`
* `swapcase`. Inplace version `swapcase!`
* `capitalize`. Inplace version `capitalize!`
* `slice` - substring

~~~ruby
# for String documentation
ri String

# Specific String method reference
ri String.slice

# list all class methods String including the ones inherited
puts String.methods.sort

# String class methods exclusive only to String
puts String.methods(false).sort

# Listing all String instance methods
puts String.instance_methods.sort

# Only instance methods from that String. Excludes methods inherited from ancestors
puts String.instance_methods(false).sort
~~~

Executing ruby command from bash and looking up its documentation.

~~~bash
ruby -e 'puts String.methods.sort' | grep convert
ri String::try_convert

ruby -e 'puts String.instance_methods(false).sort' | grep strip
ri String.slice
~~~

## Comparing string equality

* `==` - checks if two String are same by comparing the contents
* `String.eql?` - same as `==`
* `String.equal?` - Checks if two Strig instances are the same objects. Compares the reference values and not the contents.

~~~ruby
str1 = "Hello"
str2 = "Hello"

puts str1 == str2 # true
puts str1.eql?(str2) # true

str3 = str1

puts str1.equal?(str2) # false
puts str1.equal?(str3) # true
~~~

## Using %

When using **%** notation, any delimiter will work as long as the delimiters match.
`puts %(Hello)`, `puts %{Hello}`, `puts %!Hello!`, `puts %-Hello-` will all work.

~~~ruby
# same as 'Hello' similar to single quoted but no \' \\ processing
str = %q(Hello)

puts 'a\'b' # prints a'b
puts %q(a\'b) # prints a\'b

# same as "Hello" (double quotes)
# processes interpolation and backslashes
name = 'John'
puts %Q(Hello #{name})
# Using just % same as %Q
puts %(Hello #{name})

# command interpretation within backticks supports inetrpolation and character escaping
`echo #{name}` # prints "John\n"

# same as enclosing within backticks.
puts %x(echo #{name}) # prints John

# Array shorthand
words_arr = ['hello', 'world']

# Using %w creates same array as above but with less typing
puts %w[hello world]
puts %w(hello world)
puts %w{hello world}
puts %w-hello world-
~~~

## More on HereDocs

* `<<identifier`   - interpolated, goes until `identifier`
* `<<"identifier"` - same thing
* `<<'identifier'` - no interpolation
* `<<-identifier`  - you can indent the identifier by using "-" in front
* `<<~identifier`  - Automatically dedents to shortest leading whitespace line.

## Character sets

Character sets are like lookup tables where each character is assigned a unique magic number(code point).

* ASCII
* Universal Character Set(UCS)

## Character Encoding

* ASCII encoding
* UTF-8 encoding. 0-127 stored in one byte and characters with code point(magic)128 are stored in multiple bytes.

## Ruby `Encoding` class

`Encoding.list` lists built-in encodings.

Use magic comment `# coding` or `# encoding` to specify the character encoding per ruby file. Default encoding is US-ASCII.

~~~ruby
# coding: utf-8
# coding: UTF-8
# encoding: utf-8
# encoding: UTF-8
~~~

---

## References

* [More on Strings](http://rubylearning.com/satishtalim/more_on_strings.html)
* [zenspider.com: String quickRef](http://www.zenspider.com/ruby/quickref.html#types)
* [exec vs system vs `` vs %x](https://stackoverflow.com/questions/6338908/ruby-difference-between-exec-system-and-x-or-backticks)
