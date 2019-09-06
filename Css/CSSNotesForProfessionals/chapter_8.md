# Margins

| values    | description                             |
| --------- | --------------------------------------- |
| 0         | margin set to none                      |
| auto      | evenly set values on eah side           |
| units(px) | set specified units margin on each side |
| inherit   | inherit the margin from parent          |
| initial   | restore to initial value                |

## Margin collapsing
**margins touching vertically collapse, but wont collapse when touching horizontally**. In vertical overlapping, `max(bottom_margin, top_margin)` decides the total margin between the elements.
```CSS
/* bottom margin of first div will collapse with the top margin of the adjacent second div making both the margins occupy 10px combined instead of 10px each */
div {
  margin: 10px;
}

/* If there are two div places side by side, their left and right margins would take up 10px each. No collapsing happens here */
```

With border size specified, the vertical margin bewteen **parent, child** wont collapse, but with border 0px, vertical margins collapse between parent and child.

Irrespective of border size specified, vertical margins between adjacent elements always collapse.

## Margin on specific sides
* margin-left
* margin-right
* margin-top
* margin-bottom

margin on a given side can be specified explicitly, or using shorthand notation.

Shorthand notation. Start from top and move clockwise.
`margin: <top> <right> <bottom> <left>`

```CSS
div {
  margin-left: 10px;
}

/*  using shorthand notation */
div {
  margin: 0 10px 10px 20px;
}

/* apply same margni all directions */
div {
  margin: 10px;
}

/* apply same margin vertically and horizontally */
div {
  margin: 10px 15px; /* 10px top and bottom, 15px left and right*/
}
```

## Horizontally center using margin
* block element, with **width** explicitly specified, margin can center align those elements. **auto** value is used for the **left and right margins**

```CSS
/* 10% left margin and 10% right margin */
/* div is a block element and has width explicitly mentioned */
div {
  width: 80%;
  margin: 0 auto;
}
```

## Negative margins
Margin accepts negative values. used to overlap elements without absolute positioning.

```CSS
.inline {
  display: inline;
}

/* div with this class overlaps the element left to it */
.overlap {
  margin-left: -20px; 
}

/* test teh above style with HTML
  <div class="inline">Base div</div>
  <div class="overlap inline">Overlapping div</div>
 */
```

---

## References:
* [CSS notes for professionals](https://books.goalkicker.com/CSSBook/)