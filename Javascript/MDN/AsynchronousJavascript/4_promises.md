# Asynchronous Programming With Promises

Promise - intermediate state of operation which would be completed(success or failure) in the future.


## Callback hell
```Javascript
chooseToppings(function(toppings) {
  placeOrder(toppings, function(order) {
    collectOrder(order, function(pizza) {
      eatPizza(pizza);
    }, failureCallback);
  }, failureCallback);
}, failureCallback);
```

## Promises offer readability
```Javascript
chooseToppings()
.then(toppings => placeOrder(toppings))
.then(order => collectOrder(order))
.then(pizza => eatPizza(pizza))
.catch(failureCallback);
```

* Promise will succeed(Fulfilled state) or fail(Rejected state) exactly once.
* Callback can be added later for events that completed earlier and still have the callbacks invoked.

## Promise Example
```Javascript
fetch('https://httpstat.us/200', {
  headers: {
    accept: 'application/json'
  }
})
.then(response => response.text())
.then(str => console.log(str))
.catch(err => console.log(`Exception: ${err.message}`));
```

**NOTE**: The value returned by a fulfilled promise becomes the parameter passed to the next .then() block's executor function.

## Running code after fulfilling multiple promises

`Promise.all()` takes a list of promises and returns a promise that will fulfill only when all the promises are fulfilled.

```Javascript
// syntax
// Logical AND of all promises. even if one promise in the list fails, the entire promise is marked rejected
let a = fetch(url1);
let b = fetch(url2);
let c = fetch(url3);
Promise.all([a, b, c]).then(values => {
  // statements
});
```

## Running promise completion code using finally

Async equivalent of `try/catch/finally`.

```Javascript
// Syntax
myPromise
.then(response => {
  doSomething(response);
})
.catch(e => {
  returnError(e);
})
.finally(() => {
  runFinalCode();
});
```

## Building custom promises

```Javascript
let createPromise = (resolve, reject) => {
// generate a value between 0 and 100
let randomValue = Math.floor(Math.random() * 100) + 1;

console.log(`Generated value: ${randomValue}`)

// max 5 seconds
let waitTimeToComplete = Math.floor(Math.random() * 5000);

console.log(`waitTime: ${waitTimeToComplete}`);

// promise if fulfilled only when the randomValue is even number otherwise rejected.
// on fulfilling returns the random value
setTimeout((randomValue) => {
  if(randomValue % 2 == 0) {
    resolve(randomValue);
  } else {
    // pass the reason to reject
    reject('Generated number was odd');
  }
}, waitTimeToComplete, randomValue);

};

let customPromise = new Promise(createPromise);
customPromise.then((value) => {
  console.log(`Generated Even number: ${value}`);
}).catch(e => {
  console.log(`Exception: ${e}`);
});
```

Real world example is creating a promise that encapsulates XHR call to a webserver and returns the response.

```Javascript
function getXhrRequest(responseCode) {
  let xhrRequest = new XMLHttpRequest();
  xhrRequest.open('GET', 'https://httpstat.us/' + responseCode, true);
  xhrRequest.setRequestHeader('accept', 'application/json');
  return xhrRequest;
};

function promisifyRequest(responseCode) {
  return new Promise((resolve, reject) => {
    let httpRequest = getXhrRequest(responseCode);
    httpRequest.onload = () => {
      if(httpRequest.status == 200) {
        resolve(httpRequest.responseText);
      } else {
        reject(httpRequest.responseText);
      }
    };

    httpRequest.onerror = () => {
      reject(httpRequest.responseText || "Unknown error occurred");
    };

    httpRequest.send();
  });
}

promisifyRequest(200).then(response => {
  console.log(`Response: ${response}`);
}).catch(err => {
  console.log(`Exception: ${err}`);
});
```


---

## References:
* [Async programming with promises](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Asynchronous/Promises)
* [Using `fetch()`](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API/Using_Fetch)
* [Using Promises](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Using_promises)
* [We have a problem with promises](https://pouchdb.com/2015/05/18/we-have-a-problem-with-promises.html)