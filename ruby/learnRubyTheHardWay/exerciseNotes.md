# Setting up Ruby environment

* For installation of ruby in linux, follow the [document](../install-ruby-ubuntu.md)

* irb - interactive ruby or the ruby shell. Typing `irb` in the terminal opens the ruby shell (Ruby REPL).
* To exit from the ruby shell type `quit`.
* ruby works with file extension **.rb**

# String and Text
* String is enclosed between either " or '

* But #{} has meaning only in Strings within "".

* Strings enclosed between '' renders a string literal. No expression between #{} is evaluated, instead the content within the single quotes is taken as is.
```Ruby
name = "Girish"
msg = "Hello #{name}"
puts "Message: #{msg}"
puts 'Message: #{msg}'
```

* Above snippet produces the below output.
```bash
Message: Hello Girish
Message #{msg}
```
    
# References:
* [The Setup](https://learnrubythehardway.org/book)