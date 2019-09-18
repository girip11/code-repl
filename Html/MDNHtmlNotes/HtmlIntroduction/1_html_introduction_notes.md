# Html introduction

## What is HTML?
HTML - Hyper Text Markup language.It is not a programming language but a markup language.  
> **Markup Language**  
    In computer text processing, a markup language is a system for annotating a document in a way that is syntactically distinguishable from the text.  
    The idea and terminology evolved from the "marking up" of paper manuscripts, i.e., the revision instructions by editors, traditionally written with a red or blue pencil on authors' manuscripts.  
    - [Wikipedia](https://en.wikipedia.org/wiki/Markup_language)

## Anatomy of HTML element
Typical HTML element structure looks like  
**`<Opening_Tag attribute="value">Content</Closing_Tag>`**
HTML element consists of three parts.
```HTML
<!-- This is a comment statement -->
<!-- <p> is the "opening tag"
    </p> is the "closing tag" and the text/contentt between the opening and closing tags is the "content". -->
<p>Content of paragraph tag</p>
<!-- Opening and closing tags and the content constitute the HTML element -->
```

Html element can be nested within another HTML element. Rule for nesting is governed by the type of the HTML element.

## HTML element types
HTML element can either be a **block** element or **inline** element.

* **Block element** - A block level element by **default appears on a new line and takes up the entire width of its parent element**. New line separates the block from the content above and below it. This type of formatting is refered to as block formatting style. A block level element can contain either inline element or another block element. Block elements are **placed vertically** one after the other.

* **Inline element** - Inline elements grow horizontally and are usually contained inside block elements. Their default formatting style is refered to as inline formatting. But with CSS, their formatting can be changed to block formatting. **Irrespective of the type of formatting applied to the inline element, only inline elements can be nested inside an inline element**. No new line follows an inline element by default unless the behavior is altered explicitly (using CSS **display** property).

**_NOTE_**: Using CSS, the formatting of inline or block elements can be changed, for instance an inline element can be block formatted, but that does not make the inline element a block element(Inline element **cannot** contain block elements). 

## Empty Elements
* HTML elements without content does not require closing tags. Such elements are referred to as **empty elements**. Example of empty elements are img, meta, link etc

## Attributes
* Html elements can have attributes which can serve a variety of purposes (Styling, storing data etc). Some of the attributes are applicable to all Html elements and are hence called [**global attributes**](../../html_global_attributes.md).
  ```HTML
  <!-- Attributes definition -->
  <!-- Multiple attributes are space separated -->
  <div id="main-content" class="container center"></div>
  <!-- Attribues like class that support multiple values are space separated by space -->
  ```

* Boolean attributes are special types of attributes, which can have only one value which is usually the same as the name of the attribute. Such attributes can be written by just writing their names. No need to explicitly set the value. Absence of the attribute is considered as the attribute not being used.
  ```HTML
  <!-- Boolean attribute -->
  <!-- Hides the div. -->
  <div id="sub-content" hidden></div>

  <!-- Hides the div. -->
  <div id="sub-content" hidden = "hidden"></div>

  <!-- Below div will be displayed since it does not have the hidden attribute-->
  <div id="sub-content" ></div>
  ```

## Quoting attribute values
* Either single quotes or double quotes can be used.
  ```HTML
  <a href = 'http://www.w3schools.com' title="This isn't a dummy site"> W3Schools </a>

  ```

## Anatomy of HTML document
```HTML 
<!-- DOCTYPE can be html or 5 which stands for HTML5 -->
<!DOCTYPE html>
<html>
    <!-- Head tag contains metadata of the HTML document -->
  <head>
    <meta charset="utf-8">
    <meta name="author" content="Girish">
    <title>HTML Page title</title>
    <!-- head can also have link, script and style tags -->
  </head>

    <!-- Body contains the document content that is shown to the users -->
  <body>
    <h1>My document</h1>
    <p>This is my page</p>
  </body>
</html>
```

## Formatting in HTML
* Content/text inside HTML tag can be indented with any whitespaces or tabs but none of it is considered unless the content is inside the **pre** HTML element. Contents formatted inside **pre** HTML elements are represented visually with the formatting preserved.
  ```HTML
  <!-- Below paragraphs will be rendered the same -->
  <p> Hello 
      world</p>
  
  <p> Hello world</p>
  ```

## Special characters in HTML
* Characters <, >, ", ' and & are special characters in HTML and are part of HTML syntax. To incorporate these characters in content or in attribute values we need to escape these characters. These escaped representation is referred to as **character references**.
  | Character | Character |
  | --------- | --------- |
  | <         | `&lt;`    |
  | >         | `&gt;`    |
  | "         | `&quot;`  |
  | '         | `&apos;`  |
  | &         | `&amp;`   |

---

## References
* [MDN HTML introduction](https://developer.mozilla.org/en-US/docs/Learn/HTML/Introduction_to_HTML)
* [HTML Getting started](https://developer.mozilla.org/en-US/docs/Learn/HTML/Introduction_to_HTML/Getting_started)