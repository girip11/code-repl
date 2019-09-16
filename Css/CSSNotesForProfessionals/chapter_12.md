# Overflow

## Overflow property
values are 
* visible - overflowing content shown outside of the element.
* auto - makes the content scrollable if it doesnot fit
* scroll - adds vertical and horizontal scroll bars.
* hidden - overflowing contents are hidden.
* inherit - inherit from the parent element 

These values can be set horizontally and vertically using the `overflow-x` and `overflow-y` properties respectively.

## Overflow-wrap property
* normal - lets a word overflow if its longer than the line.
* break-word - will split the word also in to multiple lines if necessary.
* inherit - inherits value from the parent element.

## Creating block formatting context with overflow
When overflow property is set to value other than visible, a block formatting context is created. Used to align block element next to floated element.

**NOTE**: [placeholder.com](https://placeholder.com) is useful to have image tags with placeholder images.
Sample url `https://via.placeholder.com/150` adds a 150 x 150 image.

---

## References:
* [CSS notes for professionals](https://books.goalkicker.com/CSSBook/)