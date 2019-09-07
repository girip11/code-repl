# Box model

| Value       | Description                                                |
| ----------- | ---------------------------------------------------------- |
| content-box | width and height of content area                           |
| padding-box | width and height that includes content and padding         |
| border-box  | width and height that includes content, padding and border |
| initial     | default state                                              |
| inherit     | inherits box model of the parent element                   |


## Properties 
* padding - can be defined for all 4 sides
* border - can be defined for all 4 sides. Border can also have color and style
* margin - can be defined for all 4 sides
```CSS
div {
  border: 5px red solid;
  padding: 20px;
  margin: 50px;
}
```

## Box-sizing
* default box model is the **content-box**. 

```CSS
/* total width of the element will be 100% + 20px */
/* In content-box, the width and height are associated with the content only. padding and border alter the total width and height of the element */
div {
  width: 100%;
  box-sizing: content-box;
  padding: 20px;
}
```

In **padding-box**, the total width of the element would be defined width + border size.

In **border-box**, the total width equals to the allocated width. For a given width, padding and border take up internal space, shrinking the size of the content box. **This is the most commonly used box model.**

```CSS
/* apply the box model to textarea element only */
textarea {
  width: 100%;
  padding: 10px;
  box-sizing: border-box;
}

/* to apply border box to all elements in the page */
html {
  box-sizing: border-box;
}

/* Below assignment targets all HTML elements with *, all pseudo elements created before and after with *::before and *:: after. */
*, *::before, *::after {
  box-sizing: inherit;
}
```

---

## References:
* [CSS notes for professionals](https://books.goalkicker.com/CSSBook/)
* [Box sizing including pseudo elements](https://stackoverflow.com/questions/31317238/why-use-selector-in-combination-with-before-and-after)
* [Before pseudo element](https://developer.mozilla.org/en-US/docs/Web/CSS/::before)
* [After pseudo element](https://developer.mozilla.org/en-US/docs/Web/CSS/::after)