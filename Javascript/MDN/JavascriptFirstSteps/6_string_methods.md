# Useful String Methods

```javascript
let companyName = "Motorola";

// length of the string.
console.log(companyName.length);

//  accessing individual characters in the string
for (let i = 0; i < companyName.length; i++) {
  console.log(companyName[i]);
}

// indexOf a substring
companyName.indexOf("ola");

// extracting a substring using slice(startIndex, endIndex)
companyName.slice(0, 5);

// changing case
companyName.toLowerCase();
companyName.toUpperCase();

// replace
companyName.replace("Motor", "");
```

---

## References

* [Useful String Methods in javascript](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/First_steps/Useful_string_methods)
