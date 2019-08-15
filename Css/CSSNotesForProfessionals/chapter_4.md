# CSS Selectors

## Basic selectors

* **\*** - universal selector
* **div** - tag selector or html element selector. all **div** elements
* **.blue** - class selector
* **.blue.red** - element with classes **.blue** and **.red** (compound selector)
* **#headline** - ID selector
* **:pseudo-class** - applies to html elements with pseudo-class
* **::pseudo-element** - element that matches the pseudo-element
* **:lang(en)** - element that matches the **lang** declaration (elements containing the lang attribute).
* **div > p** - child selector

## Attribute selectors
attribute value can be enclosed in either single or double quotes.
| selector       | description                                      |
| -------------- | ------------------------------------------------ |
| [attr]         | element with attribuet **attr**                  |
| [attr='val']   | attribute value matches "val"                    |
| [attr='val'i]  | value equals ignorecase                          |
| [attr~='val']  | "val" contained in values list                   |
| [attr^='val']  | attribute starts with "val"                      |
| [attr$='val']  | attribute ends with "val"                        |
| [attr*='val']  | value string contains "val"                      |
| [attr\|='val'] | value equals or startswith "val" followed by "-" |

```CSS
/*  applies to all div elements with data-color attribute */
div[data-color] {
  /* CSS properties */
}
```

## Combinators
| selector   | description                                                |
| ---------- | ---------------------------------------------------------- |
| div span   | descendant selelctor(not direct child)                     |
| div > span | child selector                                             |
| a ~ span   | general sibling selector (span sibling after a)            |
| a + span   | Adjacent sibling selector (span immediate sibling after a) |

## pseudo classes
Example style based on html element state(checkbox checked, button hover etc)
```CSS
/* syntax */
selector:pseudo-class {
  /* CSS properties */
}
```

## Child pseudo class
`nth-child(an+b)` matches element with `a*n+b -1` siblings before it.
```CSS
/* match first child */
:first-child

 /* Match the third child  */
:nth-child(3)

/* match child located at positions that are multiple of 3. "n" value starts from 0 and children index starts from 1*/
:nth-child(3n)

/* even numbered children */
:nth-child(even)

/* odd numbered children */
:nth-child(odd)

/* last child */
:last-child

/* nth last child */
:nth-last-child(3)
```

## Class name selectors
Selects all elements based on **class name**. To select elements with match on multiple classes, the class names should not be space separated in the selectors.

```CSS
/* selects elements with both classes. order agnostic*/
.important.warning{
  /* style */
}

/* matches parent with .important and child with .warning */
.important .warning {
  /* style */
}
```

## Selecting using ID attribute
```CSS
/* this method has high specificity */
#element-id {

}

/* this method has low specificity */
[id='element-id']{

}
```

## :only-child selector
selects the any element which is the only child of its parent.

```CSS
/* only one <p> element under each parent will match this rule*/
p:only-child{
  /* style */
}
```

## :last-of-type selector
selects the last child of a particular element type of its parent.

```CSS
/* last paragraph element under each parent */
p:last-of-child{
  /* style */
}
```

## :in-range pseudo class
Associated with **input** html element where the **type** is for instance **number**
```CSS
/*  matches element when its value is inside specified range */
input:in-range {
  /* style */
}
/* HTML element looks like below */
/* <input type="number" id="choc_count" name="choc_count" value="40" min="10" max="100" step="1"> */
```

## :not pseudo class
```CSS
/* Syntax */
/* Supports comma separated selectors within ()*/
tag_selector:not([attr], .class_name,...) {

}
/* or */
/* element which contains doesnot contain attribute and doesnot have the class "class_name" */
selector:not([attr]):not(.class_name){

}

/* Example */
/* applies to all input elements that are not disabled and doesnot contain the class "important" */
input.:not([disabled]):not(.important) {
/* style */
}
```

## :focus-within pseudo class
**:focus-within** matches elements that themselves match **:focus** or that have descendants that match with **:focus**
```CSS
/* HTML */
/* <div>
    <input type="text">
  </div> */

/* div contains input that matches with :focus */
div:focus-within {
  background-color: blue;
}
```

## :checked with general sibling combinator
```CSS
/* HTML
  <label for="dark-theme">DarkTheme</label>
  <input type="checkbox" id="dark-theme"  hidden>
  <div id="container">
  </div>
  */

/* Those  elements that are sibling to the element with ID "dark-theme" and placed after it, have their background color changed to black  */
#dark-theme:checked ~ #container{
  background-color: black;
}
```

## Style range input
```CSS
/* this is an example */
input[type="range"]:focus {
  /* style */
}
```

---

## References:
* [CSS notes for professionals](https://books.goalkicker.com/CSSBook/)