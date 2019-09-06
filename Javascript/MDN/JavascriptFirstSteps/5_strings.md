# Strings

## Single and double quoted strings
```Javascript
let str = "Hello world"
let anotherStr = 'foo bar'
```

To have single quotes inside the single quoted string, escape the inner single quotes with **\**.

## String concatenation
```Javascript
let str = "Hello world"
let anotherStr = 'foo bar'

// concat strings using the + operator.
console.log(str + anotherStr)

// numbers are converted to string when using + and the other operand is a string
let addedResult = "50" + 100;
console.log(addedResult);
typeof(addedResult);

// to convert object to string, call its toString ,method
let numberStr = 100.toString();
typeof(numberStr);

// string to number conversion
addedResult = Number("50") + 100;
console.log(addedResult);
typeof(addedResult);
```

---

## References:
* [MDN: Strings In Javascript](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/First_steps/Strings)