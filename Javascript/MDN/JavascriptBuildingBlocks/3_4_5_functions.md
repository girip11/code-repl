# Functions in javascript

## Defining functions
parameters are comma separated
```Javascript
function functionName(param1, param2, ..) {
  // statements
}

//  function call/invocation
functionName();
```

## Anonymous functions
**Commonly used with event handlers**. Hence function itslef can be passed as parameters to other functions.
```Javascript
function () {
  // function body
}

let submitBtn = document.querySelector(".submit-button");

submitBtn.addEventHanlder('click', function() {
  console.log("Button clicked !!");
});

// assign function to a variable
var say_hello =  function() {
  console.log("hello");
}

say_hello();
```

## Function scope
Scope outside all the functions - **global scope**. accessible anywhere in the code. Variables declared inside a function are visible only within that function - **local scope**


Functions can call other functions. Split large functions in to smaller functions and have the large function call these smaller functions to get the functionality done.

## Function return values
Use **`return`** keyword to return values from functions.

---

## References
* [Functions in javascript](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Building_blocks/Functions)
* [Building own functions](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Building_blocks/Build_your_own_function)