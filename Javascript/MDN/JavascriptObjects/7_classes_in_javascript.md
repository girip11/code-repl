# classes
Classes was introduced in ES6. Syntactic sugar over prototypical based inheritance.

## Class declaration
**Classes are special functions, but class declarations are never hoisted unlike function declarations**

```Javascript
class Person {
  constructor(firstName, lastName, age, gender) {
    this.firstName = firstName;
    this.lastName = lastName;
    this.age = age;
    this.gender = gender;
  }
}

// class declarations should come before using them.
let p = new Person('John', 'Doe', 25, 'male');

```

## Class expressions
Class expressions can be either named or unnamed. Same hoisting rules as the class declarations.

```Javascript
// unnamed class expression
let Person = class {
  constructor(firstName, lastName, age, gender) {
    this.firstName = firstName;
    this.lastName = lastName;
    this.age = age;
    this.gender = gender;
  }
};

console.log(Person.name);

// Named class expression
let AnotherPerson = class Person2 {
  constructor(firstName, lastName, age, gender) {
    this.firstName = firstName;
    this.lastName = lastName;
    this.age = age;
    this.gender = gender;
  }
};

console.log(AnotherPerson.name);
```

## Class methods
Class body us executed in **strict mode**.

* Only once method named **constructor** can be used inside a class.

* **super** keyword to call the constructor of the parent class.

* **static** methods cannot be called on class instances.

```Javascript
class Person {
  constructor(firstName, lastName, age, gender) {
    this.firstName = firstName;
    this.lastName = lastName;
    this.age = age;
    this.gender = gender;
  }

  // getter property
  get fullName() {
    return `${this.firstName} ${this.lastName}`;
  }

  // This method is referred to as prototype method
  greeting() {
    return Person.greetingMessage(this.fullName);
  }

  // static methods of class
  static greetingMessage(fullName) {
    return `Hi, I am ${fullName}`;
  }
}

let person = new Person('John', 'Doe', 25, 'male');
console.log(person.fullName);
console.log(person.greeting());
console.log(Person.greetingMessage(person.fullName));

// This statement would throw a type error 
// since class methods cannot be invoked on instances.
// console.log(person.greetingMessage());
```

## Boxing inside prototype and static methods
Code inside classes always execute in strict mode. So autoboxing never happens. When a static or prototype method returns **this**, the value is always **undefined**. In prototype based implementation, **this** will be set to the global object in **non-strict mode**.

```Javascript
//  using classes
class Person {
  constructor(firstName, lastName, age, gender) {
    this.firstName = firstName;
    this.lastName = lastName;
    this.age = age;
    this.gender = gender;
  }

  currentInstance() {
    return this;
  }
}

// prints undefined
console.log(new Person('John', 'Doe', 25, 'male').currentInstance());
```

## Instance properties and class properties
* Instance properties - defined inside class body.
* class level properties - defined outside class body.

```Javascript
class Person {
  constructor(firstName, lastName) {
    // instance level properties.
    this.firstName = firstName;
    this.lastName = lastName;
  }

}

// class level property defined outside class
Person.count = 0;
```

## Convention: Marking the fields as private through underscore
This is just a convention. Still those fields can be accessed outside.

```Javascript
class Person {
  constructor(fullName) {
    // instance level properties.
    this._fullName = fullName;
  }

  // Getter
  get fullName() {
    return this._fullName;
  }

  // setter
  set fullName(fullName) {
    this._fullName = fullName;
  }
}
```

## Public and private field declarations
**NOTE**: Private and public field declarations are an experimental feature as of now. But can be used with transpiling tools like **Babel**.

**NOTE**: Private fields should always be declared upfront 
```Javascript
class Person {
  // private fields
  #firstName = '';
  #lastName = '';

  // public field
  fullName = '';
  constructor(firstName, lastName) {
    // instance level properties.
    this.#firstName = firstName;
    this.#lastName = lastName;
    this.fullName = `${firstName} ${lastName}`;
  }

}
```


---

## References:
* [Javascript classes](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes)