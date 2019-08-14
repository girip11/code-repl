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
  @import url('/csss/styles.css')
</style>
```

```CSS
/* External styling */
@import '/css/style.css'

/* import css from remote location.font files */
@import 'https://fonts.googleapis.com/css?family=Lato'
```
* media queries can be passed as argument to `@import` rule


## Inline styles
Inline style applied using the **style** attribute. Have higher precedence over internal and external styles. 
Makes code less maintainable. not recommended.

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
  list-style-type: circle;
  list-style-image: url(images/logo.png);
  list-style-position: inside;
}
```

---

## References:
* [CSS notes for professionals](https://books.goalkicker.com/CSSBook/)