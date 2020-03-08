# CSS Values and Units

## Numbers, lengths and percentages

- **&lt;integer&gt;** - whole number can be positive or negative
- **&lt;number&gt;** - represents a decimal number
- **&lt;dimension&gt;** - contains a unit like **px**, **deg** etc
- **&lt;percentage&gt;** - represents a fraction of some other value.

## Length

- Relative length
- Absolute length

### Absolute length units

Always considered to be of the same size.

- **cm** - centimeters. Equals
- **mm** - millimeters. Equals (1/10)cm
- **Q** - quarter millimeter. Equals (1/40)cm
- **in** - inches. Equals 2.54cm
- **pc** - picas. Equals (1/16) of an inch
- **pt** - points. Equals (1/72) of an inch
- **px** - pixels. Equals (1/96) of an inch. Most commonly used

### Relative length

Helps scale elements relative to everything on the page.

| Units | Description                             |
| ----- | --------------------------------------- |
| em    | relative to font size of parent element |
| rem   | relative to font size of root element   |
| lh    | relative to line height of the element  |
| vw    | 1vw = 1% of viewport width              |
| vh    | 1vh = 1% of viewport height             |
| vmin  | 1% of viewport's smaller dimension      |
| vmax  | 1% of viewport larger dimension         |

Example:
10vw - 10% of the viewport's width

```HTML
<style>
.wrapper {
  font-size: 1em;
}

.px {
  width: 200px;
}

.vw {
  width: 10vw;
}

.em {
  width: 10em;
}
</style>
<div class="wrapper">
  <div class="box px">I am 200px wide</div>
  <!-- Width changes as the view port size changes-->
  <div class="box vw">I am 10vw wide</div>
  <!-- Increasing the font size causes the width to increase, since the width is specified relative to the font-size -->
  <div class="box em">I am 10em wide</div>
</div>
```

---

## References

- [CSS Values and Units](https://developer.mozilla.org/en-US/docs/Learn/CSS/Building_blocks/Values_and_units)
