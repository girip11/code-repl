# Structure and formatting of CSS rule

## CSS Rule Syntax
```CSS
/* Comment statement */
/* rule syntax - selector and a declaration block*/
selector {
  /* this {} is called as declaration block */
}
```

## Property list
Some CSS properties can take multiple values. Ex: **text-shadow**

```CSS
/* property list syntax*/
propert-name: value1, value2;

/* above can also be formatted as */
property-name:
  value1,
  value2
```

## Multiple selectors
Group multiple selectors to apply same style by comma separation. Applies to all types of selectors
```CSS
div, p {
  color: blue;
}

/*  below rule applies to
* all <p> elements
* all elements with class blue
* all span elements taht are direct child of div*/
p, .blue, div > span {
  color: blue;
}
```

---

## References:
* [CSS notes for professionals](https://books.goalkicker.com/CSSBook/)