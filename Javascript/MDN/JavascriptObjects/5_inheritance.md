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
```

## Inheritance
ES6 class can have only one superclass. Multiple inheritance not possible.

```Javascript
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

## Subclassing with extends
Classes can extend from traditional function based (constructor function) classes.

```Javascript
function Person(name, age, gender) {
  this.name = name;
  this.age = age;
  this.gender = gender;
}

Person.prototype.greeting = function() {
  return `Hi, I am ${this.name}`;
}

class Teacher extends Person {
  constructor(name, age, gender, subject) {
    super(name, age, gender);
    this.subject = subject;
  }

  greeting() {
    return `Hi, I am ${this.name}. I teach ${this.subject}`;
  }
}
```

Classes cannot extend regular objects. To make the class extend from regular objects, we need to set the child class's prototype to the object using `Object.setPrototypeOf`.

```Javascript
const Person = {
  greeting: function() {
    return `Hi I am ${this.name}`;
  }
};

class Teacher {
  constructor(name, age, gender, subject) {
    this.name = name;
    this.age = age;
    this.gender = gender;
    this.subject = subject;
  }

}

Object.setPrototypeOf(Teacher.prototype, Person);

let t = new Teacher('John', 30, 'Male', 'Science');
console.log(t.greeting());
```

## super keyword
**`super`** keyword can be used to call methods on the parent/super class.

```Javascript
const Person = {
  greeting: function() {
    return `Hi I am ${this.name}`;
  }
};

class Teacher {
  constructor(name, age, gender, subject) {
    this.name = name;
    this.age = age;
    this.gender = gender;
    this.subject = subject;
  }

  greeting() {
    return super.greeting() + `I teach ${this.subject}`;
  }
}

Object.setPrototypeOf(Teacher.prototype, Person);

let t = new Teacher('John', 30, 'Male', 'Science');
console.log(t.greeting());
```

## Mixins (Abstract subclass)
Since javascript class doesnot support multiple superclasses, mixins can be used to solve multiple inheritance problem. **Mixins can be implemented with the help of functions that accept the super class as input parameter and return the subclass as output.**

```Javascript
let calculatorMixin = Base => class extends Base {
  calc() { }
};

let randomizerMixin = Base => class extends Base {
  randomize() { }
};

class Foo { }
class Bar extends calculatorMixin(randomizerMixin(Foo)) { }
```


## Species
`Symbol.species` property allows subclasses to override the default constructor for objects.

```Javascript
class MyArray extends Array {
  // Overwrite species to the parent Array constructor
  static get [Symbol.species]() { return Array; }
}
var a = new MyArray(1,2,3);
var mapped = a.map(x => x * x);

console.log(mapped instanceof MyArray); // false
console.log(mapped instanceof Array);   // true
```

---

## References:
* [Inheritance](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Objects/Inheritance)
* [Javascript classes](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes)
* [`Object.create()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/create#Examples)
* [`Function.prototype.call()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function/call)