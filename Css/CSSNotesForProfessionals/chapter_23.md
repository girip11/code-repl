# Layout control

`display` property can change the layout of the element.


## Inline styling
Occupies width as much as necessary. Inline elements are spaced horizontally.
<br>

> Inline elements behavior 
> * respect left & right margins and padding, but not top & bottom
> * cannot have a width and height set
> * allow other elements to sit to their left and right.
> [Inline elements](https://hacks.mozilla.org/2015/03/understanding-inline-box-model/)

```HTML
<style>
.container {
  border: 1px solid black;
}

.inline {
  display: inline;
  padding: 1px;
  border: 1px solid red;
}
</style>

<!-- div is a block element, but formatting can be set to be inline formatting -->
<div class="container">
  <div class="inline"> Hello</div>
  <div class="inline"> World</div>
</div>
```

## Block styling
Occupies 100% width of its parent element. Line 
breaks before and after the element.

> Block elements behavior:
> * respect all of margin and padding in all 4 sides
> * force a line break after the block element
> * acquires full-width if width not explicitly defined
> [Block element behavior](https://stackoverflow.com/questions/9189810/css-display-inline-vs-inline-block)


```HTML
<style>
.container {
  border: 1px solid black;
}

a {
  display: block;
  padding: 1px;
  border: 1px solid red;
}
</style>

<!-- anchor tag is an inline element by default -->
<div class="container">
  <a href="http://lorempixel.com/150/200" >Image1</a>
  <a href="http://lorempixel.com/150/200">Image2</a>
</div>
```

## Inline block

> Inline-block elements behavior:
> * elements placed inline (left and right)
> * respect top & bottom margins and padding
> * respect height and width
> [Inline block elements Stackoverflow](https://stackoverflow.com/questions/9189810/css-display-inline-vs-inline-block)

```HTML
<style>
.nav {
  background-color: black;
  color: white;
  list-style-type: none;
  text-align: center;
}

.nav-item {
  text-align: center;
  display: inline-block;
  font-size: 20px;
  padding: 10px 20px;
}
</style>
<ul class="nav">
  <li class="nav-item">Home</li>
  <li class="nav-item">Blog</li>
  <li class="nav-item">About</li>
  <li class="nav-item">Contact</li>
</ul>
```

## None display
Elements with `display:none` are not displayed. Browser ignores every other layout property for that element.
<br>
`none` display property is often used with javascript to show or hide an element.

**Note**: `Visibility: hidden` hides the element from being displayed, but the element still takes up the space.


```HTML
<style>
li {
  list-style-type: none;
  list-style-position: inside;
  border: 1px solid red;
}

.hide {
  visibility: hidden;
}

.display {
  display: block;
}

.no-display {
  display: none;
}

</style>

<ul class="container">
  <li class="hide">
    <a href="http://lorempixel.com/150/200"> Image1</a>
  </li>
  <li>
    <a href="http://lorempixel.com/150/200">Image2</a>
  </li>
  <li class="no-display">
    <a href="http://lorempixel.com/150/200">Image3</a>
  </li>
  <li>
    <a href="http://lorempixel.com/150/200">Image4</a>
  </li>
</ul>
```

## Table Layout

```HTML
<style>
  .table-div {
    display: table;
  }
  .table-row-div {
    display: table-row;
  }
  .table-cell-div {
    display: table-cell;
  }
</style>

<div class="table-div">
  <div class="table-row-div">
    <div class="table-cell-div">
      I behave like a table now
    </div>
  </div>
</div>
```

## [Grid layout](./chapter_24.md)
* Refer to [MDN notes on grid layout](../MDN/GridLayout/1_grid.md).

## [Flex layout](./chapter_16.md)
* Refer to [MDN notes on grid layout](../MDN/FlexboxLayout/1_flexbox_basics.md).

## Other types of display

* `table`, `table-cell`, `table-row`, `table-column` make the layout behave similar to that of `<table>`, `<td>`, `<tr>`, `<col>` elements respectively. It is easier to create **responsive tables** using this CSS `<table>` layout.
* `list-item` - behave similar to `<li>`
* `inline-table` - inline level table container
* `inline-flex` - inline level flex container
* `inline-grid` - inline level grid container



---

## References:
* [CSS notes for professionals](https://books.goalkicker.com/CSSBook/)