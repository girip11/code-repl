# Arrays

## Creation

Array can contain collection of items of any type.

```javascript
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

```javascript
let multiDimArray = [[1,2,3], [4,5,6]]
console.log(multiDimArray[0][0]);
```

## Iterating through arrays

```javascript
let arr = [1, 2, 3, 4];

for(let i = 0; i < arr.length; i++) {
  console.log(i);
}

//  arrays have lot of methods like filter, flatMap, map that can be used  as in functional programming
arr.forEach(function(arrItem) {
  console.log(arrItem);
})
```

---

## References

* [Arrays in javascript](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/First_steps/Arrays)
