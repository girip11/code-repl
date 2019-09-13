# Working with JSON

JSON - JavaScript Object Notation. data format, contains only properties. Only double quotes can be used. Unlike javascript object, property names should be quoted.


## JSON structure
```JSON
{
  "member1_string": "value",
  "member2_number": 2019,
  "member3_boolean": true,
  "members_array": [
    {
      "name": "John Doe",
      "age" : 30,
      "gender" : "male"
    },
    {
      "name": "Jane Doe",
      "age" : 28,
      "gender" : "female"
    }
  ]
}
```
 
Arrays form a valid JSON.

## JSON Serialization and desrialization
Use `JSON` object.

* `parse()` - json text to JS object
* `stringify()` - JS object to json string.

```Javascript
const PersonJson = '{"name": "John Doe", "age": 25, "gender": "male"}'
let person = JSON.parse(PersonJson);
console.log(person.name);

console.log(JSON.stringify(person));
```


---

## References:
* [Working with JSON](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Objects/JSON)