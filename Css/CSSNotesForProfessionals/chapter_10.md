# Border

## Border radius
helps to change shape of the box model. Ex: set border radius to half of the length of the square element to yield a circle.

```CSS
.circle {
  width: 200px;
  height: 200px;
  border-radius: 100px;
}

.circle {
  width: 200px;
  height: 200px;
  border-radius: 50%; /* easier rather than computing manually*/
}
```

## Border style
`border-style` property. Accepted values
* dotted
* solid
* double
* dashed
* none
* hidden

```CSS
/* all sides dotted */
border-style: dotted;

/* one style each side */
border-style: dotted solid double dashed;
```

## Multiple borders
Apply multiple borders using outline, box-shadow or pseudo-element

## Border shorthand
`border: <width> <style> <color>` is a shorthand for 3 properties.
* border-width
* border-style
* border-color
This shorthand is available for `border-top`, `border-right`, `border-bottom` and `border-left`.

## Border collapse
applies only to table elements or elements with `display: table;` or `display: inline-table;`

```CSS
table {
  border-collapse: separate;
  border-spacing: 2px
}
```

## Border Image
set image as border instead of styles.
* `border-image` - url to image
* `border-image-slice` - offset to fivide image in to 9 regions (4 corners, 4 edges, middle)
* `border-image-repeat` - scaling of image on middle and border
```CSS
border-image: url("images/border_image.png")  30 stretch;
```
Possible to create multi colored border using gradients. `border-image` won't respect `border-radius`

## Border on specific side
* `border-top`
* `border-right`
* `border-bottom`
* `border-left`
All above follow same syntax as **border shorthand**

---

## References:
* [CSS notes for professionals](https://books.goalkicker.com/CSSBook/)