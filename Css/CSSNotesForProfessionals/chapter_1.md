# Getting started with CSS

## External stylesheet
* External stylesheet using the link element.
```HTML
<!-- type attribute is optional in HTML5 -->
<!-- link tag is placed in head tag -->
<link rel="stylesheet" href="external_stylesheet.css" type="text/css">
```

* order of CSS files inclusion matters.
* Browsers cache external CSS files.

## Internal styling
* Using the **&lt;style&gt;** tag placed in **head** tag. Style applied to a partcular HTML document only.

## @import rule
import style rules from another style sheet.
```HTML
<!--  @import with internal styling -->
<style>
  @import url('/css/styles.css');
</style>
```

```CSS
/* External styling */
@import '/css/style.css';

/* Import css from remote location.font files */
@import 'https://fonts.googleapis.com/css?family=Lato';
```
* media queries can be passed as argument to `@import` rule. Using media queries, conditional import is possible.


## Inline styles
Inline style applied using the **style** attribute. Have higher precedence over internal and external styles. 
Makes code less maintainable.**Not recommended.**

## CSS with javascript
HTML element's **style** property. Style properties named in **lower camel case**.
```javascript
var html_element = document.getElementById('element')
// CSS font-family becomes fontFamily (lower camel case or simple camelCase)
html_element.style.fontfamily = "sans-serif"

// using jquery
('#element').css('fontFamily', 'sans-serif')
```

## Styling lists
```CSS
/* Three properties */
/* list-style-type - refer https://www.w3schools.com/cssref/ */
/* list-style-image - none or url*/
/* list-style-position - inside or outside*/
/* list-style: <type> <image> <position>*/
li {
  /* some of the values for list-style-type are disc(default), circle, square, lower-alpha, upper-alpha, lower-roman, upper-roman, decimal, none */
  list-style-type: circle;

  /* Using this property we can set images as list item markers instead of standard bullet markers. Images with appropriate size should be provided. resizing of images does not happen. */
  list-style-image: url(images/logo.png);
  /* inside - bullet point will be part of the list item. 
    outside - bullet point will be outside the list item. Can be understood better with border applied to list item.
  Default value is outside*/
  list-style-position: inside;
}
```

**NOTE**: Recommended way to apply list styling is to add the styling only to the list type elements(`<ol>` `<ul>`) and using inheritance, the styling would propagate to the `<li>` elements in the list. If a particular list item requires unique styling then we can override the list level settings for that list item only.

---

## References:
* [CSS notes for professionals](https://books.goalkicker.com/CSSBook/)
* [list-style-position](https://www.w3schools.com/cssref/pr_list-style-position.asp)