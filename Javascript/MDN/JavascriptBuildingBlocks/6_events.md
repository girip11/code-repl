# Introduction to events

Event handler/Event listeners can be registered to handle events when fired.

Different mechanisms to handle events are listed below.

## 1. Using event handler properties
```Javascript
const btn = document.querySelector(".submit-btn");

// onclick is an event handler property.
btn.onclick = function() {
  // statements for button click handling
}

function newButtonClickHandler() {
  // button click handler
}

// this will overwrite the previous button click handler
btn.onclick = newButtonClickHandler;

```
Commonly used event handling properties on `<button>`  element are
* onfocus
* onblur
* ondblclick
* onmouseover
* onmouseout

Keyboard key press related event handler properties
* window.onkeypress
* window.onkeydown
* window.onkeyup

## 2. Inline events handlers
Event handlers used as attribute on the HTML elements. **This approach is NOT Recommended** since it mixes up HTML and javascript. Keeping javascript all at one place is recommended.

```HTML
<script>
function onButtonClick() {
  console.log("Button clicked");
}
</script>
<button onclick="onButtonClick()"> Hello</button>
```

## 3. Using `addEventListener()` and `removeEventListener()`
Has a way to cleanup unused event handlers using the `removeEventListener()` method. Multiple event handler for the same event can be added.

```Javascript
// onclick is an event handler property.
function onButtonClick() {
  // statements for button click handling
}

function newButtonClickHandler() {
  // statements for button click handling
}

const btn = document.querySelector(".submit-btn");

// first parameter is the event to handle and the next parameter is the event handler itself.
btn.addEventListener('click', onButtonClick);

// On evenry button click , these two event handlers will be invoked.
btn.addEventListener('click', newButtonClickHandler);
```

## Event Objects
Object that contain information about the event fired is passed as parameter to the event handlers.

```Javascript
function onButtonClick(e) {
  // statements for button click handling
  console.log(e.target);
}

const btn = document.querySelector(".submit-btn");

// first parameter is the event to handle and the next parameter is the event handler itself.
btn.addEventListener('click', onButtonClick);

```

* `target` property - reference to the element on which the event occurred.

## Preventing default behavior
Example in form, when clicked on its **submit** button, event handler can be set to handle the **onsubmit** event. Inside the event handler, on the event object invoking **preventDefault()** method prevents the form from being submitted. Helps in cases where form fields don't pass the custom validation logic.


## Event bubbling and capture
Behavior when two event handlers of same event activated on single element.

Event fired on element that has parent elements, browsers can run two different phases

* **capturing phase** (top down) - Event handling starts from target element's(element on which the event occurred) outer most ancestor element and moves down to the target element. **Event handlers are invoked only on those elements registered for that event in the hierarchy.**

* **bubbling phase** (bottom up)-
Event handling start from the target element(on which the event occurred) and moves up the hierarchy of ancestors till the root element.


**NOTE**: Modern browsers use **bubbling phase** for event handling.

In bubble up phase, the event handler propagation can be stopped using the **stopPropagation()** method on the **event object passed to the event handler**.

To set the event handlers in **capturing phase**, third parameter to the **addEventListener()** method should be set to **true**.

## [Event Delegation](https://davidwalsh.name/event-delegate)
Event handlers set on parent will be invoked when those events occur on child elements even though child elements dont have event handler registered for that event due to bubbling up.

**Ex**: List with large number of items, event handling can just be done on the parent instead of registering the event handler on each of the list item (children)

---

## References:
* [Introduction to events](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Building_blocks/Events)
