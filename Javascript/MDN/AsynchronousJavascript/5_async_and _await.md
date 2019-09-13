# Using Async and Await
Introduced as part of ECMAScript 2017. For older browser support, use BabelJS to transpile.

## Async keyword

Async - turns a function to return promise. When async function returns a value, the promise is resolved with the return value.When exception is thrown inside the async function, promise is rejected with the thrown value.

```Javascript
function sayHello() {
  return "Hello";
}

console.log(typeof(sayHello));
sayHello();

// Returns a promise
async function sayHelloAsync(){
  return "Hello";
}

console.log(typeof(sayHelloAsync));
sayHelloAsync().then(value => console.log(value));

// arrow function can also be used
let hello = async  () => {
  return "Hello"; 
}

hello().then(console.log)
```

## `await` keyword
**used and works only inside any async function**. pauses the code execution on that line until the promise is fulfilled.

```Javascript
async function sayHello() {
 let greeting = await Promise.resolve("Hello");

  return greeting;
}

sayHello().then(console.log);
```


## Example
``` Javascript
// remember async function always returns a promise

async function fetchResponseText(responseCode) {
try{
  // code pauses here till promise returned by fetch is complete
  let httpResponse = await fetch('https://httpstat.us/' + responseCode);

  // code pauses till promise returned by text() is complete 
    return await httpResponse.text();
  } finally {
    // This statement gets executed just after `httpResponse.text()` promise is completed by await
    console.log("Completed fetching the response text");
  }

}

// fewer then() blocks
fetchResponseText(200).then(console.log);
```


## Error Handling
`try..catch` can be used inside async functions or `catch()` block can be used along with the `then()` blocks.

## Awaiting `Promise.all()`
Waits till all the promises complete and return the values in an array.

```Javascript
let values = await Promise.all([promise1, promise1]);

values.forEach( value => console.log(value));
```
 
## Async and await to not slow down code execution

```Javascript
async function slowExecution() {
  // Executes one promise after another 
  await fetch(url1);
  await fetch(url2);
  await fetch(url3);

  // custom processing

}

async function fastExecution() {
  // promises start to process simulataenously
  // till the first await
  let p1 = fetch(url1);
  let p2 = fetch(url2);
  let p3 = fetch(url3);

  // custom processing

  await p1;
  await p2;
  await p3;

  // or
  // await Promise.all([p1, p2, p3])
  // depending on the need
}
```

## Async and await class methods
```Javascript
class Person {
  constructor(firstName, lastName, age, gender) {
    this.name = {
      first: firstName,
      last: lastName
    };

    this.age = age;
    this.gender = gender;
  }

  async greeting() {
    return await Promise.resolve(`Hi I am, ${this.name.first} ${this.name.last}`);
  }
}

let p = new Person("John", "Doe", 25, "male");
p.greeting().then(greetingMessage => console.log(greetingMessage));
```


---


## References:
* [Using Async and Await](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Asynchronous/Async_await)