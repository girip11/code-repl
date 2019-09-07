# Variables

## Variable declaration
In javascript, a statement is terminated with **;**. Variables can be declared using either **let** or **var** keyword.
```Javascript
//  variables have default value of **undefined**.
let name;
var age;

// variable initialization
name = "John";
age = 25;

// initializing while declaring
let name = "Jane Doe";
```

## Difference between let and var
* `var` supports [**variable hoisting**](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/var#var_hoisting) while `let` **doesnt**.
  ```Javascript
  // Variable hoisting - initialization can come before declaration. This can make code hard to understand
  planetName = "Earth";

  function printPlanet(planet) {
    console.log(planet);
  }

  printPlanet(); 

  var planetName;
  ```

* With `var`, the same variable can be defined multiple times.
  ```Javascript
  var planetName = "Earth";
  var planetName = "Earth";

  // throws error
  let personName = "John Doe";
  let personName = "John Doe";
  ```

**NOTE**: Prefer `let` over `var`. `let` was introduced in later versions of javascript.

## Variable naming
Name variables in **lower camel case**. variable names are case sensitive. Variable names can start with alphabets and underscore and can contain alphabets, numbers and underscore. Javascript reserved words (keywords) cannot be used as variable names.

**NOTE**: Variable names starting with **\_** may imply special meaning. So avoid prefixing variable names with **\_**.

## Variable types
Variable type can be inspected using the operator **`typeof`**.

### Numbers
* `number` - can store integer, float
```Javascript
let num = 100;
typeof(num);
```

### Strings
* `string` - stores string
```Javascript
let str = 'hello';
typeof(str);
```

### Booleans
* `boolean` - can store true or false
```Javascript
console.log(typeof(true));
```

### Arrays
Arrays are also objects.
```Javascript
let arr = [1, 2, 3, 4];
typeof(arr); // object
console.log(arr[0]);
```

### Objects
* `object` - variable of this type stores object
```Javascript
let simpleObject = {
  name: "John",
  age: 25
}
console.log(simpleObject.name);
```

## Special values
```Javascript
typeof(null);  // object
typeof(undefined) // undefined
```

## Constants in javascript
Value cannot change after declaration. Initialization always happens while declaration.
```Javascript
// Error.Cant jsut declare constants without initialization
const name;

// Correct
const name = "John Doe";
// Error: Value of name cannot be changed
name = "Jane Doe"; 
```

---
## References:
* [Javascript variables](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/First_steps/Variables)