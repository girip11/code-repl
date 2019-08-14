# CSS Selectors

## Basic selectors

* **\*** - universal selector
* **div** - tag selector or html element selector. all **div** elements
* **.blue** - class selector
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


---

## References:
* [CSS notes for professionals](https://books.goalkicker.com/CSSBook/)