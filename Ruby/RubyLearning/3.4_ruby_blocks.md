# Ruby blocks

Ruby block - a way of grouping statements. Can be placed adjacent to the function/method call, as the last parameter to the function/method.

## Syntax

```ruby
# Convention is to use {} for single line blocks
# and do .. end for multiline blocks.
[1, 2, 3].each { |n| puts n }


[1, 2, 3].each do |n|
  square = n*n
  puts "square of #{n} is #{square}"
end
```

**NOTE**: Always enclose the method/function parameters within paranthesis when using block.

## Calling a block

A method can invoke a block using `yield` statement. Ruby block passed to the method is executed each time `yield` statement is executed.

If no block is passed to the method, then executing **yield** raises **LocalJumpError**.

```ruby
def greeting
  yield
end

# Raises excepion when called without block
greeting
```

## Passing parameters to block

```ruby
def greeting(first_name, last_name)
  # pass parameters to the block
  yield(first_name, last_name)
end

greeting("John", "Doe") {|first, last| puts "Hello #{first} #{last}"}
```

## Returning value from a block

Block returns the result of last statement/expression in that block. This value whill be returned by the **yield** statement inside the method.

```ruby
def greeting(first_name, last_name)
  # pass parameters to the block
  message = yield(first_name, last_name)
  puts message
end

# Here the block returns a custom greeting message.
greeting("John", "Doe") {|first, last| "Hello #{first} #{last}"}
```

## `block_given?`

```ruby
def greeting(first_name, last_name)
  # pass parameters to the block
  message = "Greetings, #{first_name} #{last_name}"

  if block_given?
    message = yield(first_name, last_name)
  end

  puts message
end

greeting("Jane", "Doe")
greeting("John", "Doe") {|first, last| "Hello #{first} #{last}"}
```

## Block variables

Parameters passed to the block hava a block scope. If these parameters share the same name as that of the variables present outside the block, those outer variables can never be accessed inside that block (block local variable shadows the outer vairable).

```ruby
x = 5

10.times do |i|
  x = i
  puts "Inside block x: #{x}"
end

puts "Outside block x: #{x}"
```

Explicitly declaring block local variables apart from the block parameters. This can help updating variables outside the block scope and avoid causing undesirable side effects.

```ruby
x = 10

# note block local variables separated from block parameters by semicolon
5.times do |i; x|
  # x is a block local variable.
  x = i*i
  puts "square of #{i} is #{x}"
end

puts "value of x: #{x}"
```

---

## References

* [Ruby Blocks](http://rubylearning.com/satishtalim/ruby_blocks.html)
