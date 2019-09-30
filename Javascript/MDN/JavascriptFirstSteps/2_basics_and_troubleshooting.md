# Javascript Basics

## Variables creation

Variable creation using **let** or **var** keyword. Constants are created using the **const** keyword

```Javascript
const planet_name = "Earth";
let name = "John Doe";
var gender = "male";
```

## Functions

```Javascript
// This is a named function
function function_name(param1,param2, ...) {

}

// below is a named function expression
const helloWorld = function helloWorld() {
  console.log("Hello World");
}

// This is an example for anonymous function expression
const helloWorld = function () {
  console.log("Hello World");
}
```

## Operators

+, -, *, /
operator precedence - **PEDMAS**
Paranthesis, Exponent, Division, Multiplication, Addition, Subtraction.

## Relational operators

* **===** : strict equality operator. Value and type must be same
* **!==** : value and type are not same.
* <, >, <=, >=

## Conditional blocks

```Javascript
if (condition1) {

} else if (condition2) {

} else {

}
```

## Loops

```Javascript
for (let i =1; i < 10; i++) {
  console.log(i);
}
```

## DOM functions

* form elements have focus method.
* input elements have value property
* paragraph element has the text stored in textContent property
* All HTML elements have style property, which can be used to set the styling for that object.

```Javascript
document.querySelector('[CSS SELECTOR]')
```

## Troubleshooting

* Use browser console and take a look at the error messages,
* Syntax errors, logical errors

---

## References

* [JS Basics](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/First_steps/A_first_splash)
* [Troubleshooting](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/First_steps/What_went_wrong)
