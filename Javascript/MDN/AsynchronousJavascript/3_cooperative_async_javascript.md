# Cooperative Asynchronous Javascript

`setTimeout()`, `setInterval()` and `requestAnimationFrame()` - callbacks run by the main thread.

## `setTimeout()`
 executes a block of code once after the specified time has elapsed.

Since main thread has to execute the callback on time elapse, the callback is not always guaranteed to be executed exactly after the time interval mentioned.

```Javascript
/* syntax
setTimeout(function_to_execute, time_interval_milliseconds, parameters_to_function)

returns an identifier using which we can manage the timeout like cancelling the run using **clearTimeout()**
*/

function sayHello(user) {
  console.log(`Hello, ${user}`);
}

// trigger after 5seconds
let greeting = setTimeout(sayHello, 5000, 'John Doe');

// Stops this function from executing before 5 seconds elapse, 
clearTimeout(greeting);
```

**NOTE**: Setting timeout to 0, causes immediate timeout and runs the function immediately(as soon as the main thread becomes available)

## `setInterval()`
Function passed to this function is executed repeatedly, with each execution separated by the time interval provided.

```Javascript
/* Syntax
  setInterval(function_to_execute, periodic_interval, parameters_to_function)
*/

function executePeriodically(startTime) {
  let timeElapsed = new Date().getTime() - startTime;
  console.log(`Time elapsed: ${timeElapsed}`);
}

let periodicExecution = setInterval(executePeriodically, 2000, new Date().getTime());

clearInterval(periodicExecution);
```

**Note:** `setInterval()` can be implemented using `setTimeout()` by calling it recursively in the callback function. 
* This way we can achieve constant time interval between executions.
* Different interval between execution is possible.


## `requestAnimationFrame()`
TODO

---

## References:
* [Cooperative Asynchronous Javascript](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Asynchronous/Timeouts_and_intervals)