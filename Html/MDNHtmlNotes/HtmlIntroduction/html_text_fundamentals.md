# HTML Text fundamentals

## Headings, paragraphs and content structuring
* Heading tags are **&lt;h1&gt;, &lt;h2&gt;, &lt;h3&gt;, &lt;h4&gt;, &lt;h5&gt; and &lt;h6&gt;**. Paragraph test is placed inside the HTML element **&lt;p&gt;**.
* Various header elements are used to represent the structural hierarchy. Usually a page contains only one **&lt;h1&gt;** tag. Good practice is to have h2 contain h3 rather than the other way. For instance use h2 for chapter titles and h3 for sections in the chapter and not viceversa.
* General practice is to keep the heading levels to 3 per page.
* Heading play an important role in indexing webpages by search engines.
* Headings helps give the document outline when presented through **screen reader**. **Makes the HTML page more accesible.**
```HTML
<!DOCTYPE html>
<html lang="en-US">
  <head>
    <title>Sample HTML document</title>
  </head>
  <body>
    <h1>Document heading</h1>
      <h2>Chapter 1</h2>
        <h3>Introduction to Bash</h3>
          <p> Bash is the default shell of GNU operating system. Bash stands for <b>B</b>ourne <b>A</b>gain <b>SH</b>ell, pun intended on the author of unix shell Stephen Bourne.
        <h3>Bash Documentation</h3>
          <p>Bash manual is available at <a href="https://www.gnu.org/software/bash/manual/bash.html" title="Bash manual"></a></p>
  </body>
</html>
```

## Lists
Lists in html can either be ordered or unordered. Lists can be nested.
```HTML
<!-- Unordered list -->
<ul>
  <!-- li stands for list item -->
  <li>Apple</li>
  <li>Orange</li>
</ul>
<!-- Ordered list -->
<ol>
  <li>Gold medalist</li>
  <li>Silver medalist</li>
  <li>Bronze medalist</li>
</ol>
```

## Emphasis
* semantics is very important in Search Engine Optimization and accessbility.
* Text which needs to be emphasized  is usually enclosed within **&lt;em&gt;** tag.
* While rendering, the text is rendered with italics style and screen readers read the text in a different tone.
* If the purpose is just to style the text with italics, then we can use **&lt;i&gt;** or **&lt;span&gt;** element with CSS styling.

## Importance
* Important text is enclosed within **&lt;strong&gt;** tag.
* Browsers display the text as bold and the screen readers read the text in a different tone.
* If the goal is to just display the text in bold and not associating it with any importance, the  we can use **&lt;b&gt;** or **&lt;span&gt;** element with CSS styling.

## Text underline
* Text can be underlined with **&lt;u&gt;**. It is a common practice to underline hyperlinks.

**NOTE**: Elements **&lt;b&gt;, &lt;i&gt; and &lt;u&gt;** don't have any semantics when it comes to accessibility. They just provide presentational value.

## References:
* [HTML text fundamentals](https://developer.mozilla.org/en-US/docs/Learn/HTML/Introduction_to_HTML/HTML_text_fundamentals)