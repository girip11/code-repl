# Prototypes

## Protoype object
* Object can have prototype object from which it can inherit the methods and properties.

* Prototype chain - Prototype object itself can have another prototype object.

Every object be default has **Object** as its prototype.

## Prototype chain
When a method is invoked on an object, first it is checked in that object for that method. If the method id not found, search continues in the object's prototype chain. 

> personObj -> Person(constructor) -> Object

## Prototype property
**Object** has a property call **prototype** which itself is an object. All those members inside this **prototype** object are inherited by objects in the prototype chain. Direct members of **Object** are not inherited.

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

// Person constructor's prototype is empty
console.log(Person.prototype);

console.log(Object.prototype);

console.log(String.prototype);
console.log(Number.prototype);
console.log(Date.prototype);
console.log(Array.prototype);
```

## Objects created using `create()`
```Javascript
// Assume p1 is an instance of Person
const p2 = Object.create(p1);

// p2 object is created with p1 as its prototype object
console.log(p2.__proto__); // return p1
```

## **constructor** property
```Javascript
//  Refer to the Person constructor function above
const p1 = new Person('John', 'Doe');

// constructor property - constructor function
console.log(p1.constructor);

const p2 = new p1.constructor('Jane', 'Doe');

// constructor function name
console.log(p1.constructor.name);
```

## Modifying prototypes
Adding members to constructor prototype dynamically and automatically becomes available to objects **derived from** that constructor.

```Javascript
// prototype object be default contains constructor property, which points to the constructor upon which this property is invoked.
console.log(Person.prototype);

Person.prototype.goodBye = function() {
  return 'Bye, ' + this.name.first + " " + this.name.last + ".";
}

console.log(p1.goodBye());
```

Rarely properties are defined on prototype object. **Constant properties** can be defined on prototype.

Common practice is to defined properties on constructor and methods on the prototype.
---

## References:
* [Javascript Prototypes](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Objects/Object_prototypes)