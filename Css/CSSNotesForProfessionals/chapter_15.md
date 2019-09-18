# Typography

## Line height
in px, em or any other valid CSS measurements

## Text Color
Text color. Value can be specified using color name, hex code, rgb or hsl.

## Text alignment and direction
* start - same as left if screen direction is from left to right else similar to right.
* end - same as right if screen direction is from left to right else similar to left.
* left - left align
* right - right align
* center - center align
* justify - text aligned to fill the left and right edges of the line box except for the last line.
* match-parent

direction of the text can be set using the `direction` property.
* rtl - text read from right to left
* ltr - text read from left to right

## Text decoration
* none
* underline
* overline
* line-through - similar to enclosing the content inside `<s>` HTML element.


## Font size
in px, em or any other valid CSS measurements

## Font Style
* normal
* italics - characters drawn differently.
* oblique - roman font skewed by certain degrees(8-12)

```HTML
<style>
  .italicize {
    font-style: italic;
  }

  .oblique {
    font-style: oblique;
  }
</style>

<p class="italicize"> Hello World</p>
<p class="oblique"> Hello World</p>

```

## Font weight
* normal (400 value) - default
* lighter
* bold (700 value)
* bolder
* value between 100 - 900


## Font Family
List of font family names separated by comma. Browser selects the first font in the list that is installed.

## Font Variant
* normal
* small-caps - Sets every letter to uppercase, but makes the lowercase letters(from original text) smaller in size than the letters
that originally uppercase.

## [Font Stretch](https://developer.mozilla.org/en-US/docs/Web/CSS/font-stretch)
Selects normal, condensed or expanded font face from a font. Values: condensed, extra-condensed, condensed, semi-condensed, semi-expanded, expanded, extraexpanded or ultra-expanded. Also accepts percentage values 50% - 200%.

## Font shorthand
```CSS
font: [font-style] [font-variant] [font-weight] [font-size/line-height] [font-family];
```

* `font-size` and `font-family` are mandatory properties for font shortcut to work.


## Quotes
Customize opening and closing of the **`<q>`** tag.
* none
* auto - quote marks based on `lang` attribute
* [<String> <String>]
```HTML
<!-- opening and closing quotes should be specified  -->
<q style="quotes:'$' '$'">This is a quote.</q>
```

## Text Overflow
* clip - default. clips the overflowing content.
* ellipsis - render "..." to represent overflow
* custom string - 

Text overflow requires the following properties set
```CSS
overflow: hidden;
whitespace: nowrap;
```

```HTML
<style>
div {
  width: 300px;
  height: 300px;
  border: 2px solid red;
}

p {
  border: 2px solid black;
  overflow: hidden;
  white-space: nowrap;
  text-overflow: "[..]";
}
</style>

<div>
    <p>Lorem, ipsum dolor sit amet consectetur adipisicing elit. Eaque voluptate delectus maxime asperiores vero eligendi rem repellat rerum ad aliquam nemo voluptatibus labore sapiente illo accusamus aut, dolor iusto!  Reiciendis? Lorem ipsum dolor sit amet consectetur adipisicing elit. Sed maxime ratione, non, placeat sit nisi facere incidunt quo pariatur dignissimos dicta quod animi neque necessitatibus beatae enim eum aliquid eveniet.
    </p>
</div>
```

## Text shadow
```CSS
/* blur radius is optional */
/*  multiple values can be provided by separating with comma */
text-shadow: [horizontal-offset] [vertical-offset] [blur-radius] [color]
```

```HTML
<style>
p {
  text-shadow: 3px 3px 1px black;
}
</style>
<div>
  <p>Lorem, ipsum dolor sit</p>

</div>
```

## Text transform
* uppercase
* lowercase
* capitalize - first letter of every word is capitalized

```HTML
<style>
  .upper {
    text-transform: uppercase;
  }
  .lower {
    text-transform: lowercase;
  }
  .capitalize{
    text-transform: capitalize;
  }
</style>
<div>
  <p class="upper">Lorem, ipsum dolor sit</p>
  <p class="lower">Lorem, ipsum dolor sit</p>
  <p class="capitalize">Lorem, ipsum dolor sit</p>
</div>
```

## Letter spacing
Spacing between each letter. supports negative values.

```HTML
<style>
p {
  letter-spacing: 2px;
}
</style>
<div>
  <p>Lorem, ipsum dolor sit</p>
</div>
```

## Text Indent
Horizontal space with which the first line of the text should be indented.

```HTML
<style>
p {
  text-indent: 20px;
}
</style>
<div>
  <p>Lorem ipsum dolor, sit amet consectetur adipisicing elit. Modi doloribus recusandae consequuntur tempore impedit et dolorem facilis? Commodi veritatis, excepturi neque repudiandae maxime harum? Maxime praesentium quis assumenda officia quo!, ipsum dolor sit</p>
</div>
```

## Text decoration
```CSS
/*  text-decoration is a shorthand for style, line and color */
text-decoration: [text-decoration-style] [text-decoration-line] [text-decoration-color]
```

```HTML
<style>
.decorate {
  text-decoration: solid underline blue;
}
</style>
<div>
  <p>Lorem ipsum dolor, sit amet , <span class="decorate">consectetur adipisicing</span> elit.</p>
</div>
```

## Word spacing
* accepts positive and negative values
* normal - default word spacing

```HTML
<style>
.spacy {
  word-spacing: 5px;
  font-weight: bold;
}
</style>
<div>
  <p>Lorem ipsum dolor, sit amet , <span class="spacy">consectetur adipisicing</span> elit.</p>
```

---

## References:
* [CSS notes for professionals](https://books.goalkicker.com/CSSBook/)