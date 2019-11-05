# Simple Constructs

## if else end

In ruby, only `nil` and `false` evaluate to false. 0 evaluates to true.

```ruby
val = 0

if val
  puts "0 evaluates to true"
else
  puts "This will never be executed for val = 0"
end
```

## `unless .. end` statement

Opposite of `if`. Executes when the condition evaluates to `false` or `nil`.

## Ternary operator

```ruby
puts "enter an integer between 0 - 100"
val = gets.chomp.to_i
puts ((val >= 0 && val <=100) ? "in range": "out of range")
```

## Statement modifiers

```ruby
val = 5
puts "Value of val is 5" if val == 5

puts "Value of variable 'val' is not 10" unless val == 10
```

## Case statement

Equivalent to series of if else statements.

```ruby
# case with range
val = 5
message = case val
when 0..10
  "Within 0 - 10"
# then required when the expression is in the same line as "when"
when 11..100 then "Within 11 - 100"
else
  "Out of range"
end

puts message
```

```ruby
# case with regex
puts "Enter car model"
car_model = gets.chomp

case car_model
when /dx/
  "Diesel"
when /px/
  "petrol"
when /ex/
  "electric"
else
  "Unknown"
end

```

**NOTE:** For label to exact value match in case of strings, `Hash` is preferred over case statement.

## `nil`

In ruby `nil` is also an object. Methods can be accessed on nil as well as methods can be added like any other object.

```ruby
nil.public_methods(false).sort

puts nil.to_s
puts nil.to_i
puts nil.nil?
```

## `nil` and `false`

`nil` and `false` are two different objects in ruby.

```ruby
puts nil.object_id
puts nil.class

# NIL is a synonym for nil
puts NIL.class
puts NIL.object_id

# similarly FALSE is a synonym for false.
puts false.object_id
```

## Loops

```ruby
i = 0
while i < 10
  puts i
  i+= 1
end
```

---

## References

* [Simple Constructs](http://rubylearning.com/satishtalim/simple_constructs.html)
* [Ruby case statement](https://www.rubyguides.com/2015/10/ruby-case/)
