# Flexbox

Flex operates one dimension (either along the row or column), while **grid** operates on two dimensions.

Consists of two axes
* main axis
* cross axis - perpendicular to main axis

## The main axis
Defined by `flex-direction`. Possible values are
* row - Default value.
* row-reverse
* column
* column-reverse

`row` or `row-reverse` - main axis runs along the row in the inline direction, while `column` or `column-reverse` makes main axis run from top to bottom in the **block direction**.

## The cross axis
Runs perpendicular to the main axis.

## The start and end lines
For English, start is at left, end is right, while for Arabic, start is right and end is left.

## The flex container
Immediate children of the flex container become flex items. Flex layout defined as below.

```CSS
.flex-container {
  display: flex;
}
/* or */
.inline-flex-container {
  display: inline-flex;
}
```

## Flex item behavior
* Flex items take enough space to fill the content.
* Flex items start from start edge of the main axis defined by `flex-direction` property
* Flex items don't expand along the main axis, but expand along the cross axis.
* `flex-basis` by default is **auto** and `flex-wrap` is by default set to **nowrap**.

```HTML
<style>
  ul {
    display: flex;
    list-style-type: none;
    border: 1px solid black;
  }
</style>

<ul>
  <li>
    <img src="http://lorempixel.com/150/150" alt="">
  </li>
  <li>
    <img src="http://lorempixel.com/150/150" alt="">
  </li>
  <li>
    <img src="http://lorempixel.com/150/150" alt="">
  </li>
  <li>
    <img src="http://lorempixel.com/150/150" alt="">
  </li>
  <li>
    <img src="http://lorempixel.com/150/150" alt="">
  </li>
  <li>
    <img src="http://lorempixel.com/150/150" alt="">
  </li>
</ul>
```

Since `flex-wrap` is set ot **nowrap** by default, the flex items overflow the flex container.

## Changing the flex direction
* `flex-direction: row-reverse;` - reverses the start and end.
* `flex-direction: column;` -the main axis switches and our items now display in a column. 
* `flex-direction: column-reverse` the start and end linesalong the columns again switched.

## `flex-wrap`
Default is **nowrap**. Flex items shrink to fit to the flex container. If the flex item is not shrinkable, overflow occurs.

By setting the value of `flex-wrap` to **wrap** elements are placed in the next line.

```HTML
<style>
  ul {
    display: flex;
    flex-direction: row;
/* without this rule, the contents would overflow the flex container */
    flex-wrap: wrap;
    list-style-type: none;
    border: 1px solid black;
  }
</style>

<ul>
  <li>
    <img src="http://lorempixel.com/150/150" alt="">
  </li>
  <li>
    <img src="http://lorempixel.com/150/150" alt="">
  </li>
  <li>
    <img src="http://lorempixel.com/150/150" alt="">
  </li>
  <li>
    <img src="http://lorempixel.com/150/150" alt="">
  </li>
  <li>
    <img src="http://lorempixel.com/150/150" alt="">
  </li>
  <li>
    <img src="http://lorempixel.com/150/150" alt="">
  </li>
</ul>
```

## `flex-flow` shorthand

```CSS
/* order doesnot matter */
.flex-container{
  flex-flow: <flex-direction> <flex-wrap>;
}
```

## Properties applied to the flex items

Available space = (total flex container width) - (sum of width of individual flex items)

### `flex-basis`
This property defines the size of the flex item. Default value is **auto**. Default behavior is as follows.

* If flex item has size specified, then that item hold that much space.
* If the flex item does not have size specified, occupies the space as much as requried by the content.

### `flex-grow`
Setting this property to a positive integer makes the items stretch to fill up the available space or proportion of the available space.
<br>
This property can be set to all the flex items or set to individual flex items. This property can be used to distribute the available space in proportion.

```CSS
.flex {
  display: flex;
}

.flex-item {
  /* Default all the elements should fill the flex available space equally */
  flex-grow: 1;
}

.flex-item.first {
  /* first item takes up twice space as that of any other flex item */
  flex-grow: 2;
}
```

### `flex-shrink`
When set to positive integer, this property will make the flex item shrink than the `flex-basis`. Minimum size of the item will be considered before shrinking the items.

### `flex` shorthand
`flex: [flex-grow] [flex-shrink] [flex-basis];`

Flex shorthand values

* `flex: initial` - same as `flex: 0 1 auto`
* `flex: auto` - same as `flex: 1 1 auto`
* `flex: none` - same as `flex: 0 0 auto`. Items cannot shrink or grow. Laid out only on `flow-basis`.
* `flex: 1` - same as `flex: 1 1 0`

```HTML
<style>
.box {
  display: flex;
}

.box > div {
  flex: 1 1 auto;
}

.box > .one {
  flex: 2 1 auto;
}

</style>
<div class="box">
  <div class="one">One</div>
  <div class="two">Two</div>
  <div class="three">Three</div>
</div>
```


## Alignment and justification

### `align-items`
This property aligns the flex items **along the cross axis.**. Values are

* stretch - default. All flex items stretch to the height of the tallest one in the main axis to fill the flex container.
* flex-start - align items to the start line fo the cross axis
* flex-end - align items to the end line of the cross axis
* center - align items to the center of the cross axis

```HTML
<style>
ul {
  display: flex;
  width: 500px;
  height: 400px;
  flex-flow: wrap row;
  list-style-type: none;
  border: 1px solid black;
  align-items: flex-end; /* stretch, flex-start and center*/
}

li {
  border: 1px solid black;
}
</style>

<ul>
  <li>
    <p>Lorem kjdsfh</p>
  </li>
  <li>
    <p>fhkjdf aksgfe hello</p>
  </li>
  <li>
    <p>AMakxinf skjheianb</p>
  </li>
</ul>
```

### `justify-content`
Align flex items along the **main axis.** Possible values are

* flex-start - Default. Align items at the start edge of the container.
* flex-end - Align items at the start edge of the container.
* center - Align items to the center along the main axis
* space-around - equal amount of space on either sides of the flex item, with half size space on either edges.
* space-between - Share the spare space evenly between the items.
* space-evenly - equal amount of space on either sides of the flex item including the edges.

```HTML
<style>
ul {
  padding: 5px;
  display: flex;
  width: 500px;
  height: 400px;
  flex-flow: wrap row;
  list-style-type: none;
  border: 1px solid black;
  justify-content: space-evenly;
}

li {
  border: 1px solid black;
}
</style>

<ul>
  <li>
    <p>Lorem kjdsfh</p>
  </li>
  <li>
    <p>fhkjdf aksgfe hello</p>
  </li>
  <li>
    <p>AMakxinf skjheianb</p>
  </li>
</ul>
```

---

## References:
* [Basic concepts of flexbox](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Flexible_Box_Layout/Basic_Concepts_of_Flexbox)
* [CSS Flexbox Guide](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Flexible_Box_Layout)