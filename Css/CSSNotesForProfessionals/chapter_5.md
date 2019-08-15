# Background
* can set background color, gradient and image.
* adjust size, positioning, repetition

## Background color
`background-color` property. Applied to all elements.
Possible values
* color value, hex color codes. Ex: red, blue etc
* transparent -transparent background
* inherit - inherit this property from parent
* initial - sets to default value

### Hex color code
`#000000` - every two hex characters represent a color. Order of color is RGB. Notation is case insensitive
* \#ff0000 - Red only
* \#00ff00 - Green only
* \#00f - blue only (short notation)
* \#ffffff - can be shortened to #fff

### RGB or RGBa method
RGB - Red Blue Green. Each values between 0 and 255
RGBA - the fouth parameter is between 0 and 1 called **alpha parameter** that defines the **opacity**

```CSS
section {
  /* black */
  background-color: rgb(0, 0, 0); 
}

/* black with 50% opacity */
header, footer {
  background-color: rgba(0, 0, 0, 0.5)
}
```

### HSL method
HSL - Hue Saturation Lightness
HSLa - alpha parameter to define opacity
* Hue - degree on color wheel ranging from 0 to 360
* Saturation - 0 to 100%
* Lightness - 0 to 100%
```CSS
section {
  /* green */
  background-color: hsl(120, 100%, 50%);
}
```

## Background gradients
Gradients - new image type. introduced in CSS3
Gradient functions
* linear - repeating and nonrepeating variants
* radial -repeating and nonrepeating variants

## Background image
covers entire element excluding margin
Possible values
* url()
* none - no background image
* inherit - inherit from parent
* initial - default value

```CSS
header {
  background-image:url('images/body_background.png');
}

/* short notation */
footer {
  background: red url('images/footer.png');
}

/* multiple background images using comma separated */
/* images will get arranged according to declared order */
section {
  background-image: url('images/bg1.png'),
  url('images/bg2.png');
}
```

## More properties for background image
* background-size: xpx ypx or x% y%
* backgroud-position: center center, left top, right bottom, left offset(px/%), right offset(px/%)
* background-repeat - no-repeat, repeat. repeat-x, repeat-y
* background-clip - relative to content-box, border-bo or padding-box

## Background shorthand
Order of the values **doesnot** matter.
```CSS
/*  Shorthand notation
background: [<background-image>] [<background-color>] [<background-position>]/[<background-size>]
[<background-repeat>] [<background-origin>] [<background-clip>] [<background-attachment>]
[<initial|inherit>];
 */
```
**NOTE:** Use of the shorthand background property resets all previously set background property values,
even if a value is not given. If you wish only to modify a background property value previously set, use a longhand property instead.


---

## References:
* [CSS notes for professionals](https://books.goalkicker.com/CSSBook/)