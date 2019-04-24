# comments
* Preferred - prefix with "#". Single line comment
* Obselete - enclose between **=begin** and **=end**. This proves multiline comment feature but not usually used.

# Console output
* `puts` or `print` to write to console. print writes to console without newline at the end.

# Console input
*  `gets` reads the input from terminal with new line as the terminator. But the read value includes the new line character as well. To remove the new line from the input String just use `gets.chomp()`.

# Arrays
* Array.new => new empty array
* Array["a", "b"] initializes new array with two elements.
* Array.length() => length of the array.

# Hashes
* Used to store a collection of key value pairs

```Ruby
states = {
    "key1" => "value1",
    "key2" => "value2"
}

cities = {
    :key1 => "value1",
    :key2 => "value2"
}

# Below two access are equivalent
puts states["Key1"]
puts cities[:Key1]
```
# Methods
* Syntax 
  ```Ruby
    def [MethodName] (param1 = "defaultValue",.... param = "defaultValue")
        Method Body
    end
  ```

* Method returns the result of last expression in the body when "return" keyword is not specified.
* If return keyword is specified, then no statement in the method after the return statement is executed. No error of unreachable code because ruby is interpreted.
* To return multiple values, use "return keyword".  
    `return expression1, expression2`

# Conditional statements
* If Syntax
  ```Ruby
  if condition
    Body
  end
  ```
* If else syntax
```Ruby
if condition
    body
elsif condition
    body
else
    body
end
```
* To combine conditions use logical operators **and**, **or**, **!**(NOT operator)

# Switch Case
Syntax 
```Ruby
    case label
        when "value1"
            body
            .
            .
        when "valueN"
            body
        else    # default case 
            body
    end
```

# While loop
Syntax
```Ruby
while condition
    body
end
```

# for loop
Syntax
```Ruby
# syntax for iterating through array
for itr in array
    body
end

# Iterating through array
array.each do |iterator|
    body
end

# Syntax for looping through range
for itr in start..end 
    body
end

# iterating for n times.
N.times do |index|
    body
end
```

# File operations
* File open
    `File.open("file","mode")`
```Ruby
    File.open("file", "r") do |file|
        puts file.read()
        # Every call to readline method moves the file pointer to the next line in the file
        puts file.readline()

    end
 
    # OR

    file = File.open("file", "r")
    for line in file.readlines()
        puts line
    end
    file.close()
```
* Various file modes. "r"(read only), "r+"(read write), "w"(write-only), "w+"(create or truncate), "a"(append only), "a+"(create or append), "b"(binary)
* 


# Handling Errors
Syntax:
```Ruby
# Catch all syntax
begin
    body
rescue
    body
end

# catch specific error
begin
    body
rescue [ErrorType1]
    body
rescue [ErrorType2]
    body
rescue 
    body
end

# catch error and assign to variable to access error details
begin
    body
rescue [ErrorType1] => ex1
    body
rescue [ErrorType2] => ex2
    body
rescue
    body
end
```

# Class
Syntax
```Ruby
class [ClassName]
    # public visible attributes or variables
    attr_accessor :attr1, :attr2, :attr3

    # constructor equivalent in ruby is initialize method.
    # This is also optional
    def initialize(param1, param2, param3)
        @attr1 = param1
        @attr2 = param2
        @attr3 = param3
    end

    # optional methods
    def method1(param1, param2, param3)

    end
end
```

# Inheritance
Syntax
```Ruby
class Parent
    # attributes

    # methods
    def sayHello
        puts 'Hello'
    end
end

class child < Parent
    # attributes

    # override parent method
    def sayHello
        puts 'Hellloo'
    end
end
```

# Modules
* Helps to group methods with similar functionality. For instance, group all methods that can serialize, deserialize a json under one single module.
Syntax:
```Ruby
module JSONUtil
    # methods
    def serialize(obj)
        # serialization logic
    end
end
```

* Usually the module is defined in one file and used in another ruby file. Syntax for using it is. For using it in the same file as the module file just the **include** keyword and then call the methods directly.
```Ruby
# import the file first
require_relative "ruby_module_filename"

# Include the modules requires in the file.
include JSONUtil

# we can invoke the method directly.
serialize(Array[1,2,3,4,5])
```

# Reference:
* [Youtube ruby tutorial from freecodecamp](https://www.youtube.com/watch?v=t_ispmWmdjY)