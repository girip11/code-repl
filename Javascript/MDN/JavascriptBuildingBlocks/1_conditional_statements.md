# Making decisions in javascript

## if .. else statements
```javascript
// syntax
if (condition) {
  // statements
} else if (condition) {
  // statements
} else{

}
```
Values **false, undefined, null, 0, NaN, empty string** evaluate to false.

## Logical operators
* `&&` - Logical AND
* `||` - Logical OR
* `!` - Logical NOT


## switch statements
```javascript
// syntax
switch(condition) {
  case 'choice1': 
    // statements
    break;
  
  default:
    // this section is optional
    // statements
}
```

## Ternary operator
```Javascript
// syntax
(condition) ? expression1: expression2;
```

---

## References:
* [Making decisions](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Building_blocks/conditionals)