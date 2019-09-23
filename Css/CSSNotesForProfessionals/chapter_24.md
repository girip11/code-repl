# Grid
Used for dividing web page into rows and columns.

## Grid layout
This property is applied to the parent element and its immediate children only.

```CSS
display: grid;
/* or */
display: inline-grid;
```

## Create grid rows and columns
`grid-template-rows` and `grid-template-columns`

## Sizing the implicitly created rows
`grid-auto-rows`

## Explicit placing of the items

```CSS
.container .item1 {
  grid-column: 1;
  grid-row: 1;
}
```

For more details on grid, refer [MDN notes on CSS grid](../MDN/GridLayout/1_grid.md)

---

## References:
* [CSS notes for professionals](https://books.goalkicker.com/CSSBook/)