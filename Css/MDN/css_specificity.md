# CSS Specificity

Specificity - means by which browsers apply the CSS rules on elements.

## Specificity calculation
Specificity - weightage based on number of selector types in a **CSS declaration**. Specificity applied to resolve conflict when multiple CSS declarations target the same element.

```CSS
div {
  /* The below line is a CSS declaration */
  color: white;
}
```
<br>

Multiple CSS declarations with same specifity - last declaration is applied.

## Selector types and specificity
Ascending order of specificity
* Type selectors and pseudo elements (least specific)
* class selectors, pseudo classes, attribute selectors
* ID selectors (most specific)

```HTML
<style>
/* selector with lowest specificity */
div {
  background-color: black;
  color: white;
}

/* this selector has higher specificity than the previous one and has lower specificity than the next one*/
.container {
  background-color: blue;
}

/* This selector has the highest specificity among the three */
div.container{
  background-color: red;
}
</style>

<body>
  <!-- div element will have the background color as red-->
  <div class="container">
    <p> Hello world! </p>
  </div>
</body>
```

**NOTE**: 
* Universal selector, combinators and negation pseudo class have no effect on specificity.
* CSS declarations inside the **style attribute** of the HTML element has the highest specificity.


## `!important` exception
CSS declaration with `!important` overrides other declarations. **Bad practice to use `!important`**. Two same CSS property declarations with `!important` will be resolved usign their **specificity**.

> Some rules of thumb:
> * Always look for a way to use specificity before even considering `!important`
> * Only use `!important` on page-specific CSS that overrides foreign CSS (from external libraries, like Bootstrap or normalize.css).
> * Never use `!important` when you're writing a plugin/mashup.
> * Never use `!important` on site-wide CSS.

## `!important` uses
* Override inline styles
* Override high specificity

## Overriding `!important`
Define CSS selector with **higher specificity** or with **same specificity at a later point** containing the CSS declaration with `!important`.

## `:is()` and `:not()` exceptions
> The matches-any pseudo-class `:is()` and the negation pseudo-class `:not()` **are not considered a pseudo-class in the specificity calculation**. But selectors placed into the pseudo-class count as normal selectors when determining the count of selector types.


## DOM element proximity ignorance
```CSS
/* Both the CSS rules below have the same specificity. so the last one declared is applied. */
  body h1 {
    color: green;
  }

  html h1 {
  /* This is the last one declared. so this CSS declaration will be applied to <h1> elements*/
  color: purple;
  }
```

## Directly targeted styles vs inherited styles
Directly targeted styles take precedence over the inherited ones.

```HTML
<style>
  ul {
    color: blue;
  }

  li {
    color: green;
  }

  li.red{
    color: red;
  }
</style>
<ul>
  <!-- colored green-->
  <li>Item1</li>
  <!-- colored green-->
  <li>Item2</li>
  <!-- colored red-->
  <li class="red">Item3</li>
</ul>
```

## Online specificity calculator tool
[CSS specificity calculator](https://specificity.keegan.st/)

---

## References:
* [](https://developer.mozilla.org/en-US/docs/Web/CSS/Specificity)