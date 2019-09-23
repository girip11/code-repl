# CSS Grid
Grid - intersecting set of horizontal and vertical lines, forming rows and columns.

## Grid features

* fixed track size using pixels and flexible track sizes usnig **fr unit**
* Items can be placed in precise location
* Flexible to add additional rows and columns when needed.
* alignment control
* control of overlapping content.

## Grid container

> We create a grid container by declaring display: grid or display: inline-grid on an element. As soon as we do this, all direct children of that element become grid items.- MDN

```HTML
<style>
.container {
  display: grid;
}
</style>

<div class="container">
  <div>Item1</div>
  <div>Item2</div>
  <div>Item3</div>
  <div>Item4</div>
</div>
```

## Grid tracks
Define rows and columns using `grid-template-rows` and `grid-template-columns` properties.

**Grid track is the space between any two lines on the grid**

```HTML
<style>
.container {
  display: grid;
  grid-template-columns: 200px 200px 200px;
}
</style>

<div class="container">
  <div>Item1</div>
  <div>Item2</div>
  <div>Item3</div>
  <div>Item4</div>
</div>
```

## **fr** Unit
Create flexible grid tracks using **fr**(fraction). This unit represents the fraction of the available space in the grid container.

```HTML
<style>
.container {
  display: grid;
  /* Whole space divided in by 4fractions. First column takes up 50% while the remaining ones take 25% each*/
  grid-template-columns: 2fr 1fr 1fr;
}
</style>

<div class="container">
  <div>Item1</div>
  <div>Item2</div>
  <div>Item3</div>
  <div>Item4</div>
</div>
```

When **fr** is used along with fixed size pixels, (available space - fixed size columns) will be available for fractional units.

## Track listing with `repeat()` notation

`repeat()` - repeat all or a section of track listing

```HTML
<style>
.container {
  display: grid;
  /* four columns with each 1fr unit space */
  grid-template-columns: repeat(4, 1fr);
}
</style>

<div class="container">
  <div>Item1</div>
  <div>Item2</div>
  <div>Item3</div>
  <div>Item4</div>
</div>
```

Applying repeat notation to part of track listing.
```CSS
/* Applying repeat notation to part of track listing */
/* column1 - 50px */
/* column4 - 50px */
/* rest of the space split equally in to two columns */
grid-template-columns: 50px repeat(2, 1fr) 50px;
```

Creating repeating pattern using the **repeat notation**
```CSS
/* consists of 4 columns */
/* first and third column - 1fr */
/* second and fourth column - 2fr */
grid-template-columns: repeat(2, 1fr 2fr);
```
Here the rows are defined on its own making it an **implicit grid**

By default implicit grid takes up the size to fit its contents (auto sized).

## Sizing the implicit grid
Define a set size for tracks created in the implicit grid with the `grid-auto-rows` and `grid-auto-columns` properties.

```HTML
<style>
.container {
  display: grid;
  /* four columns with each 1fr unit space */
  grid-template-columns: repeat(4, 1fr);
  /* each row now will be 100px tall */
  grid-auto-rows: 100px;
}
</style>

<div class="container">
  <div>Item1</div>
  <div>Item2</div>
  <div>Item3</div>
  <div>Item4</div>
</div>
```

`minmax()` function can help define minimum size but also make the track expand when the content is bigger.

```CSS
grid-auto-rows: minmax(100px, auto);
```

```HTML
<style>
.container {
  display: grid;
  /* four columns with each 1fr unit space */
  grid-template-columns: repeat(4, 1fr);
  /* minimum row height is 50px  */
  grid-auto-rows: minmax(50px, auto);
}
</style>

<div class="container">
  <div>Item1 Lorem ipsiomd fhdsk</div>
  <div>Item2</div>
  <div>Item3</div>
  <div>Item4</div>
</div>
```


## Explicit grid
Created by specifying rows and columns using `grid-template-rows` and `grid-template-columns`.


## Positioning items against Grid Lines
> Lines are numbered according to the writing mode of the document. In a left-to-right language, line 1 is on the left-hand side of the grid. In a right-to-left language, it is on the right-hand side of the grid. - MDN

In left to right language, first vertical line on the left is numbered 1. Similarly the first horizontal line from the top is numbered 1.

`grid-column-start` and `grid-column-end` operate on the vertical lines while `grid-row-start` and `grid-row-end` operate on the horizontal lines.

```CSS
/* This item takes up three columns and two rows */
.item1 {
  /* Content occupies columns between the vertical lines numbered from 1 to 4*/
  grid-column-start: 1;
  grid-column-end: 4;

  /* Content occupies rows between the horizontal lines numbered from 1 to 3*/
  grid-row-start: 1;
  grid-row-end: 3
}
```
Example
```HTML
<style>
.container {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  grid-auto-rows: minmax(50px, auto);
}

.item1 {
  grid-column-start: 1;
  grid-column-end: 4;
  grid-row-start: 1;
  grid-row-end: 3;
}

.item2 {
  grid-column-start: 1;
  grid-row-start: 3;
  grid-row-end: 5;
}
</style>
<div class="container">
  <div class="item1"><a href="http://lorempixel.com/150/200">Item1 Lorem ipsiomd fhdsk</a></div>
  <div class="item2"><a href="http://lorempixel.com/150/200">Item2</a></div>
  <div class="item3"><a href="http://lorempixel.com/150/200">Item3</a></div>
  <div class="item4"><a href="http://lorempixel.com/150/200">Item4</a></div>
</div>
```

## Grid Cell
Conceptually similar to a table cell.

## Grid area
Items spanning multiple cells vertically and horizontally create **grid areas**. **Grid areas is always rectangular**

## Gutters
Spacing between the grid cells is achieved using the properties `row-gap` and `column-gap`

`grid-row-gap` and `grid-column-gap` (deprecated properties) are aliases to `row-gap` and `column-gap`.

```HTML
<style>
.container {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  column-gap: 10px;
  row-gap: 10px; 
}
</style>

<div class="container">
  <div class="Item">Item1 Lorem ipsiomd fhdsk</div>
  <div class="Item">Item2</div>
  <div class="Item">Item3</div>
  <div class="Item">Item4</div>
</div>
```

## Nesting grids
When a grid item itself is styled with `display: grid`,a nested grid is created within the grid item.

Nested grid doesnot inherit any property from the parent grid.

```CSS
/* Assume a 3 column grid */
.item1 {
  grid-column-start: 1;
  grid-column-end: 4;
  grid-row-start: 1;
  grid-row-end: 3;

  /* properties for nested grid*/
  display: grid;
  grid-template-columns: repeat(3, 1fr);
}
```

## Layering items with z-index
Using z-index, we can control which grid item should be displayed above the other. Item with higher z-index will be displayed above the item with lower z-index. Helps when the items overlap.

<style>
.container {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  grid-auto-rows: minmax(50px, auto);
}

.item1 {
  grid-column-start: 1;
  grid-column-end: 4;
  grid-row-start: 1;
  grid-row-end: 3;
  z-index: 2;
  background-color: blue;
}

.item2 {
  grid-column-start: 1;
  grid-row-start: 2;
  grid-row-end: 4;
  z-index: 1;
  background-color: green;
}
</style>
<div class="container">
  <div class="item1"><a href="http://lorempixel.com/150/200">Item1 Lorem ipsiomd fhdsk</a></div>
  <div class="item2"><a href="http://lorempixel.com/150/200">Item2</a></div>
  <div class="item3"><a href="http://lorempixel.com/150/200">Item3</a></div>
  <div class="item4"><a href="http://lorempixel.com/150/200">Item4</a></div>
</div>
```


---

## References:
* [CSS Grid layout basics](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Grid_Layout/Basic_Concepts_of_Grid_Layout)
* [CSS Grid layout](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Grid_Layout)
