# Exception handling using try/catch

## Syntax

```javascript
// catch more specific exceptions first and then the more generic ones
try {
  // block of code
} catch(exception1) {

} catch(exception2) {

} finally {
  // cleanup code
}
```

Even with return statements inside try and catch clauses, finally block is executed.

Accepted forms of try statement

* try ... finally
* try ... catch
* try ... catch ... finally

## Unconditional exception handling

Below snippet is an example of unconditional catch clause

```javascript
try {
  //block of code
} catch (e) {
  //catches any exception
}
```

## Conditional exception handling

Conditional catch clause that conforms to ECMASCRIPT.

```javascript
try {
  //block of code
} catch (e) {
  if (e instanceof TypeError) {
    // statements to handle TypeError exceptions
  } else if (e instanceof RangeError) {
    // statements to handle RangeError exceptions
  } else if (e instanceof EvalError) {
    // statements to handle EvalError exceptions
  } else {
    // statements to handle any unspecified exceptions
    logMyErrors(e); // pass exception object to error handler
  }
}
```

## Rethrowing the exception

For rethrowing the caught exception inside the **catch** clause or throwing a new exception from **try** clause, use the **throw** statement.

## Return statement inside try block

Return value from return statement inside finally is always the return value of the function.

```javascript
function exceptionHandling() {
  try {
    console.log("Inside try");
    let value = 5/"b";
    console.log(value)

    if(Number.isNaN(value)) {
      throw new Error("Incorrect parameters to divide")
    }

    return value;
  } catch(e) {
    console.log("Inside catch" + e);
    return 0;
  } finally {
    console.log("Inside finally");
    return 100;
  }
}

console.log(exceptionHandling()) // prints 100 as the return value
```

---

## References

* [try..catch](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/try...catch)
