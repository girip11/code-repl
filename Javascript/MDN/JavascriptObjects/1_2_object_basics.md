# Object basics

## Creating objects
Object consists of members each of which are name value pairs. Members are comma separated, while name and value are separated by colon.

Objects members can be either a property or a method.

```Javascript
// syntax
// this is example of an object literal
const object = {
  // below members are properties
  member1_name: member1_value, 
  member2_name: member2_value, 
  // below defined are methods
  member3_name: function() {

  },
  member4_name: function() {
  }
};

const sampleObject = {
  name: {
    first: 'John',
    last: 'Doe'
  },
  age: 30,
  gender: 'male',
  interests: ['skiing', 'music'],
  greeting: function() {
    return "Hi, I am " + this.name.first + " " + this.name.last; 
  }
};

// access object properties and methods using **dot** notation
console.log(sampleObject.name.first);
console.log(sampleObject.greeting());

// accessing members using **bracket notation**
// consider object as an associative array
console.log(sampleObject['name']['first']);
console.log(sampleObject['greeting']());

// updating/setting object members
sampleObject.age = 28;

// dynamic member names can be set only using bracket notation
let uniqueIdName = 'UniqueID';
let uniqueIdValue = 'ABCD-EFGH';
sampleObject[uniqueIdName] = uniqueIdValue;
```

## **this** keyword
**this** refers to the current object

Objects communication as **message passing**.

## Constructor function
constructor function is Javascript version of class. This function name follows Pascal case(CamelCase).

```Javascript
function Person(first, last) {
  this.name = {
    first: first,
    last: last
  };
  this.greeting = function() {
    return 'Hi, I am ' + this.name.first + ' ' + this.name.last + '.';
  };
}
const person1 = new Person('John');
const person2 = new Person('Jane');
```

## Other ways to create object instances
```Javascript
// creates empty object
const p1 = new Object();
p1.name = 'John';
p1.greeting = function() {
    return 'Hi, I am ' + this.name + '.';
};

// passing object literal to the Object constructor
const p2 = new Object({
  name: 'John',
  greeting: function() {
    return "Hi, I am " + this.name.first; 
  }
});

// Creating new object based on existing object
const p3 = Object.create(p2);
```

---

## References:
* [Javascript object basics](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Objects/Basics)