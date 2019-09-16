# Floats

## Float image within a text
`float` property can be used for making the text flow around the image.

```HTML
  <style>
    img {
      float: left;
      margin: 10px;
    }
  </style>
  <div>
    <img src="https://via.placeholder.com/150">
    <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Esse nesciunt voluptates, deserunt soluta, accusamus
      numquam ipsam deleniti repellat est voluptatibus veritatis. Voluptatum, quas! Temporibus cupiditate voluptatum,
      beatae a laboriosam ipsum!Lorem ipsum dolor sit amet consectetur adipisicing elit. Esse nesciunt voluptates, deserunt soluta, accusamus
      numquam ipsam deleniti repellat est voluptatibus veritatis. Voluptatum, quas! Temporibus cupiditate voluptatum,
      beatae a laboriosam ipsum!</p>
  </div>
```


## clear property
can be set on element to clear the floats around it.
* none - Default. allow floating on either sides
* left - no float allowed on left.
* right - no float allowed on right.
* both - no floating elements allowed on either sides of the element.

```HTML
  <style>
    img {
      float: left;
      margin: 10px;
    }
    .flaot-clear {
      clear: both;
    }
  </style>
  <div>
    <img src="https://via.placeholder.com/150">
    <p class="float-clear">Lorem ipsum dolor sit amet consectetur adipisicing elit. Esse nesciunt voluptates, deserunt soluta, accusamus
      numquam ipsam deleniti repellat est voluptatibus veritatis. Voluptatum, quas! Temporibus cupiditate voluptatum,
      beatae a laboriosam ipsum!Lorem ipsum dolor sit amet consectetur adipisicing elit. Esse nesciunt voluptates, deserunt soluta, accusamus
      numquam ipsam deleniti repellat est voluptatibus veritatis. Voluptatum, quas! Temporibus cupiditate voluptatum,
      beatae a laboriosam ipsum!</p>
  </div>
```

## inline **div** using float property

```HTML
<style>
#div1 {
  width: 50%;
  float: left;
  color: black;
  background-color: blue;
  text-align: left;
}

#div2 {
  width: 50%;
  float: left;
  color: black;
  background-color: green;
  text-align: right;
}
</style>
<body>
  <div id="div1">
    <p>This is a div1</p>
  </div>
  <div id="div2">
    <p>This is a div2</p>
  </div>
</body>
```


## clearfix hack
* Elements after a floating element will flow around it. This hack is used for fixing the issue 
* When the height of the floating elements exceeds the containing element, the content overflows outside the element.

The below style is applied to the element containing the floats.
```CSS
/* using the pseudo element */
.clearfix::after {
  content: "";
  clear: both;
  display: table;
}
```

---

## References:
* [CSS notes for professionals](https://books.goalkicker.com/CSSBook/)
* [Clearfix hack](https://www.w3schools.com/howto/howto_css_clearfix.asp)