# Outlines
outline
* line around the element outside border. displated around the element.
* dont take space in box model. no impact to element position.
* Outline **outlines the element's entire content, even if the content overflows.**


Important properties are (similar to border)
* `outline-color`
* `outline-style`
* `outline-width`

With the help of `outline-offset` property we can draw the outline separated from the border by the mentioned offset. ALong with `outline-offset`, the element can be highlighted around its margin (outline-offset same as margin).


## Shorthand
`outline: <width> <style> <color>`
```CSS
p {
  outline: 1px dotted blue;
}
```

## Outline styles
* dotted
* dashed
* solid
* double
* groove
* ridge
* inset
* outset
* none
* hidden

---

## References:
* [CSS notes for professionals](https://books.goalkicker.com/CSSBook/)