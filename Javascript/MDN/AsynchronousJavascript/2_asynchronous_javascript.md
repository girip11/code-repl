# Introduction to Asynchronous Javascript

## Async callbacks
Register a callback - passing function as parameter. this function will be invoked when the background task is completed or a desired event is triggered.

Ex: listening to events using `addEventListener()`

```Javascript
// Assume we have a button in the webpage with id **submit_button**
let submitButton = document.getElementById("submit_button");

submitButton.addEventListener('click', () => {
  // this is a callback
  console.log("Button clicked");
});

```

## Promises
New style of async code using promises.
`fetch()` accepts url and returns a promise object.

```Javascript
fetch('https://github.com/girip11/code-repl/blob/master/_config.yml').then((response) => {
  console.log(`response: ${typeof(response)}`);
}).catch((err) => {
  console.log(`Exception: ${err}`);
});
```

Promises are placed in **event queue**. They run after the main thread completes its processing.

## Promises advantages over callbacks
* Multiple async operations chained using `.then()`
* called in the order in which they are placed in the event queue.
* Error handling with `.catch()`.
* avoid inversion control

## Inversion control
Function to which we called with callback function is expected to call the callback function. This is referered to as inversion control.

In callbacks, we trust the library function(3rd party library or own library) **to call the callback function exactly once, handle success and failure properly and pass the correct arguments.**

In case of promises, inversion of control does not happen. Promises can be in either of the three states 
* Pending - can transition to either fulfilled or rejected
* Fulfilled - no further state transition. should have a value which shouldnt change
* Rejected - no further state transition. should have a reason which shouldnt change

Promise though resolved multiple times, would ensure the next task execution (`.then()`) exactly once.


---

## References:
* [Introduction to Asynchronous Javascript](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Asynchronous/Introducing)
* [Inversion of control](https://www.youtube.com/watch?v=bAlczbDUXx8)