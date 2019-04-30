# Notes
* Chapterwise notes from the book **Learn to code in python3**

## Chapter 1

* Python is interpreted language. Statement by statement interpreted.
* Group of statements form a block. Method/function comprises of blocks.
* Indentation very important for interpreter to identify tokens.
* No tab or whitespace before the beginning of a statement.

## Chapter 2

Identifier naming rules
* Identifier names case sensitive
* Start with either alphabets(lower and upper case) or underscore
* remaining characters can contain only alphabets, digits or underscore
* reserved words cannot be used as identifiers.
* `print` for console output and `input` for console input.
* `print('messsage', end='')` prints the message to console and ends with empty string. By default print method ends the string with new line.
* All reserved keywords are small case except the keywords **True** and **False**.
* Type conversions
  ```Python
    # Converts to int
    int('1')

    float('1.234')

    # eval converts input to appropriate type
    # if we pass a string to eval and if the value is 4
    # type is returned as int, if the value is 4.3 then the
    # type of the returned variable is float.
    x = '1'
    # prints int
    print(type(eval(x))

    x = '1.0'
    # prints float
    print(type(eval(x))

    x = '12xf
    # Error
    print(type(eval(x)))
  ```

## Chapter 3
* The operators are 
    - '+' addition
    - '-' subtraction
    - '*' multiplication
    - '/' floating point division. Returns the quotient of the division as a floating point
    - '//' Integer division. returns quotient of the division as integer.
    - '%' Modulus - returns the remainder of division
    - '\*\*' exponent operator __a \*\* b__ is interpreted as 'b' times 'a' or 'a' to the power of 'b'
    - unary '+' and '-'
* unary operators have higher precedence than binary operators and unary operators are right associative.
* Operator precednce - PEDMAS
    `P(paranthesis)E(Exponent)D(/, // and %)M(multiplication)A(addition)S(subtraction)`
* Division and multiplication same precedence and addition and subtraction in same precedence.
* All the binary operators are left associative except the assignment operator which is right associative.
* Chained assignment 
```Python
# Right most expression executed first
a = b = c = d
```
* Arithmetic shorthand operators
  ```Python
    x *= 5 # same as x = x * 5 
  ```

# References:
* Learn to code in python3 by Richard L.Halterman