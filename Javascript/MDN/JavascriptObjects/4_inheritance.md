# Inheritance

## Inheriting properties from another object
`call()` method on the function object is used to call constructor function on the parent object.

```Javascript
function Person(first, last, age, gender) {
  this.name = {
    first: first,
    last: last
  };
  this.age =age;
  this.gender = gender;
}

Person.prototype.greeting = function() {
  return "Hi, I am " + this.name.first + " " + this.name.last + ".";
}

function Teacher(first, last, age, gender, subject) {
  // if the constructor doesnt take any arguments, only this needs to be passed.
  Person.call(this, first, last, age, gender);

  this.subject = subject;
}
```

## Setting prototype and constructor reference on inherited objects

```Javascript
console.log(Person.prototype);
console.log(Teacher.prototype);

Object.getOwnPropertyNames(Teacher.prototype);

Object.getOwnPropertyNames(Person.prototype);

// Make the Person's prototype as Teacher's prototype
Teacher.prototype = Object.create(Person.prototype);

// Would have the value as Person
// since Person.prototype was copied to Teacher.prototype.
console.log(Teacher.prototype.constructor);

Object.defineProperty(Teacher.prototype, 'constructor', {
  value: Teacher,
  enumerable: fasle,
  writable: true
});

// override greeting method in Teacher
Teacher.prototype.greeting = function() {
  return `Hi, I am ${this.name.first} ${this.name.last}. I teach ${this.subject}`
}
```

## Class in javascript(ECMA2015 or ES2015 or ES6)
Supported in all modern browsers. Its actually converted to the prototypal inheritance model under the hood.

```Javascript
class Person {
  constructor(first, last, age, gender) {
    this.name = {
      first: first,
      last: last
    };

    this.age = age;
    this.gender = gender;
  }

  // returns greeting message
  greeting() {
    // Template literals - helps achieve string interpolation
    return `Hi, I am ${this.name.first} ${this.name.last}.`;
  }
}

const p = new Person('John', 'Doe', 25, 'male');
console.log(p.greeting());

// Inheritance
class Teacher extends Person {
  constructor(first, last, age, gender, subject) {
    super(first, last, age, gender);
    this.subject =subject;
  }
}
```

## Getters and Setters
```Javascript
//  rewriting Teacher class using getter and setter
// Inheritance
class Teacher extends Person {
  constructor(first, last, age, gender, subject) {
    super(first, last, age, gender);
    this._subject =subject;
  }

  get subject() {
    return this._subject;
  }

  set subject(subject) {
    this._subject = subject;
  }
}

const t1 = new Teacher('John', 'Doe', 25, 'male', 'Maths');
console.log(t1.subject);
t1.subject = 'English'
```

## References:
* [Inheritance](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Objects/Inheritance)
* [`Object.create()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/create#Examples)
* [`Function.prototype.call()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function/call)