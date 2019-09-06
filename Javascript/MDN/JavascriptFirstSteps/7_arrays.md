# Arrays

## Creation
Array can contain collection of items of any type.

```Javascript
let cricketTeams = ["India", "Australia", "England", "NewZealand", "WestIndies", "SriLanka", "Pakistan", "SouthAfrica" "Bangladesh", "Zimbabwe"]

console.log(cricketTeams[0]);

// Update entry in the array
cricketTeams[9] = 'Afganistan';

// length of the array
cricketTeams.length

// string to array using split() method
let rankingColumns = "Country,Rank".split(",");

// array to string
cricketTeams.toString();

// join using custom delimiter
cricketTeams.join("_");

// adding and removing array elements to and from end
rankingColumns.push("Population");

let rankColumn = rankingColumns.pop("Rank")

// shift and unshift insert and remove from the beginning of the array.
// remove from the beginning
cricketTeams.shift();

// insert at beginning
cricketTeams.unshift("India")
```

## Multidimensional Array
```Javascript
let multiDimArray = [[1,2,3], [4,5,6]]
console.log(multiDimArray[0][0]);
```

---

## References:
* [Arrays in javascript](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/First_steps/Arrays)