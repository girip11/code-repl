# What is Javascript

Create dynamic content, manage controls, handling events etc

## Browser APIs

* DOM(Document Object Model) API - HTML and CSS manipulation
* Geolocation API
* Canvas and WebGL APIs - create animated 2D and 3D graphics.
* Audio and Video APIs ex: WebRTC

## Third party APIs

Ex: open street maps API

## Web page rendering

HTML and CSS first is assembled  and then javascript code is executed by browser's javascript engine.

Browser tab - execution environment provides isolation between code running on each website.

## Javascript running order

Browser runs javascript run from top to bottom
Javascript - interpreted language(just in time compiled to improve performance). Javascript present as part of webpage is the client side javascript.

Dynamic content on website can be created using both server side and client side code.

## Adding javascript code to the webpage

**`<script>`** tag can be added inside `<head>` or `body`.

```HTML
<!-- Inline javascript -->
<script>
  console.log("Hello");
</script>

<!-- adding external javascript file -->
<!-- defer attribute eliminates render blocking javascript -->
<script src="/js/app.js" type="text/javascript" defer></script>
```

## Inline javascript handlers

Usage of this technique is discouraged in practice, as it mixes javascript handler inside HTML elements. Recommended approach is using the `addEventListener()` in javascript.

```HTML
<script>
function createContent() {
  let p = document.createElement('p');
  p.textContent = "Hello World";
  document.body.appendChild(p);
}
</script>

<button onclick="createContent()">Click to create content</button>
```

## Handling events using EventListener

```HTML
<script>
function createContent() {
  let p = document.createElement('p');
  p.textContent = "Hello World";
  document.body.appendChild(p);
}

let btn = document.querySelectorAll('button');
if(btn && btn.length >= 1) {
  btn[0].addEventListener("click", createContent);
}
</script>

<button>Click to create content</button>
```

## Script loading strategies

Making javascript execute after complete HTML loading and parsing. This is useful when JS code manipulates HTML and requires all of HTML to be loaded before starting the JS code execution.

```HTML
<!-- defering internal JS script execution -->
<script>
document.addEventListener('DOMContentLoaded', function() {
  // Internal JS code
})
</script>

<!-- delaying external JS code execution. **defer** attribute works only for external javascript-->
<script src="/js/app.js" defer></script>
```

## async vs defer

* scripts **independent** of each other and don't need to wait for parsing can use **async**.
* scripts that are dependent on other scripts requires preserving order of loading(same as order with which they are mentioned), such scripts can be loaded using **defer**.

## Comments

```Javascript
// single line comment
/*
  Multiline comment
*/
```

---

## References

* [What is javascript](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/First_steps/What_is_JavaScript)
