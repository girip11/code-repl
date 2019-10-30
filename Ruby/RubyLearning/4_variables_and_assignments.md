# Variables and Assignments

* Variable is created when the interpreter sees an assignment statement.

> Whenever Ruby sees a bareword, it interprets it as one of three things:
>
> 1. If there's an equal sign (=) to the right of the bareword, it's a local variable undergoing an assignment.
> 2. Ruby has an internal list of keywords and a bareword could be a keyword.
> 3. If the bareword is not (1) or (2) above, the bareword is assumed to be a method call. If no method by that name exists, Ruby raises a NameError.

## Method calls as messages

* Method call in ruby can be interpreted as message sent to the object(name preceding the dot operator). If the object has a method that matches the name specified in the message, then the object responds by executing that method.

~~~ruby
value_s = '2000'
# value_s object is a receiver of the message to_i
value = value_s.to_i
~~~

## References

* [Variables and Assignments](http://rubylearning.com/satishtalim/variables_and_assignment.html)
