# Calculating specificity

For specificity basics refer [MDN notes on specificity](../MDN/css_specificity.md)

| Group | selector                                           |
| ----- | -------------------------------------------------- |
| A     | Id selector                                        |
| B     | Class selector, attribute selector, pseudo classes |
| C     | type selectors, and pseudo elements                |

Group A is most specific while group C is least specific.

Universal selector and combinators have no specificity.

```CSS
/* A=2, B=0,C=0 */
#foo #bar{

}

/* A=1, B=1, C=0 */
#foo.bar {

}

/* A=0, B=0, C=1 */
div {

}

/* A=0, B=0, C=1 */
div::before {

}
```

## Easy specificity calculation
* Assign 1000 points to each selector declared in **inline** styles.
* Assign 100 points to each selector that belongs to Group A
* Assign 10 points to each selector that belongs to Group B
* Assign 1 point to each selector that belongs to Group C


## Resolving styles with selectors of same specificity
```CSS
.foo {
  color: blue;
}

.bar {
  color: red;
}
```
An element with both the `foo` and `bar` classes will be displayed after resolving conflict over the `color` property. Given both the selectors have the same specificity, cascading nature of CSS helps resolving this conflict. **The last one declared will be applied.**

## Manipulating specificity
Dulpicating selectors to increase the specificity.

```CSS
/* A=0, B=1, C=0 */
.bar {

}

/* A=0, B=2, C=0 */
.bar.bar{

}

/* (0, 1, 0) < (0, 2, 0)*/
```

## `!important` and inline styling
* `!important` - usage is discouraged. Override through higher specificity rather than using this flag. Usage of this flag affects **maintainability**

* inlie styling - heavily discouraged. Use it only for debugging purposes.

**NOTE**: Always start with selectors that have least specificity, which implies having more generic selectors. Increase the specificity gradually as and when required.

## Online specificity calculator tool
[CSS specificity calculator](https://specificity.keegan.st/)


## CSS Loading order
* Browser styles
* Style customized on the browser by the user
* External stylesheet on the webpage
* Within the <style> element of the HTML document
* Inline styles applied using the **style** attribute on the HTML element.

With CSS rules(aka CSS declarations) having same specificity, cascading rules are applied to resolve the conflict.

---

## References:
* [CSS notes for professionals](https://books.goalkicker.com/CSSBook/)