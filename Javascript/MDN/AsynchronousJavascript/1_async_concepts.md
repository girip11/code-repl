
# Asynchronous programming concepts

## Blocking code
Javascript generally is single threaded. Expensive operations make browser frozen. Causes bad user experience.

## Threads 

Web worker - can be used for expensive operations carried out in the background. But they cant access the DOM.

Promises - allow running a task and making it wait until the results of its dependant tasks are returned.

---

## References:
* [General Asynchronous programming concepts](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Asynchronous/Concepts)