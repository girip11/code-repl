# Advanced text formatting
Use the samples with **codepen.io**.

## Description lists
Description lists are used to markup items and their associated descriptions. Can be used to markup
* terms and definitions 
* questions and answers
* word and its meanings
A single term can be associated with multiple descriptions.
```HTML
<!-- Example of a description list-->
<dl>
<dt>Germane</dt>
<dd>Relevant to a subject under consideration</dd>
<dt>Flabbergaster</dt>
<dd>A person, thing or fact that causes extreme shock</dd>
<dd>A state of surprise or fear</dd>
</dl>
```

## Quotations
### Blockquotes
Used to quote block level content quoted from some source. It is a block element.
URL of the source (if the content is obtained from web) is mentioned in the **cite** attribute.
**Cite** HTML element can also be used to mention the citations. Helps in citing the author or source of the quotations. 
```HTML
<blockquote cite="https://en.wikipedia.org/wiki/HTML">
<p>Hypertext Markup Language (HTML) is the standard markup language for documents designed to be displayed in a web browser.<p>
<!-- Its a good practice to turn website to links -->
<a href="https://en.wikipedia.org/wiki/HTML"><cite>- Wikipedia</cite></a>
</blockquote>
```

### Inline quotations
To quote a content inline, **&lt;q&gt;** tag is used. Intended for short quotations.
```HTML
<p>According to <a href="https://en.wikipedia.org/wiki/Cascading_Style_Sheets">wikipedia</a> Cascading Style Sheets (<abbr>CSS</abbr>) is a <q cite="https://en.wikipedia.org/wiki/Cascading_Style_Sheets">style sheet language used for describing the presentation of a document written in a markup language like HTML</q></p>
```

**NOTE**: While content in the **cite** attribute is useful to screen readers, they arent displayed on the browser. **Cite** HTML element is used when the content needs to be rendered in the browser. If teh citation is from website,  its a good practice to mention the website name in the **cite** element and enclose it inside **&lt;a&gt;** tag with the url to the webpage containing the quotation.


## Abbreviations
```HTML
<!-- Title attribute contains the full expansion of the abbreviation or acronym. It will be displayed like a tooltip when hovered over.-->
<p><abbr title="Cascading Style Sheets">CSS</abbr>
 is a style sheet language used for describing the presentation of a document written in a markup language like <abbr title="Hyper text Markup Language">HTML</abbr></p>
```

## Contact details
**&lt;address&gt;** html element is meant for marking up the contact details of the person who wrote the HTML document.

## Superscript and subscript
Used in
* Mathematical equations
* Chemical formula
```HTML
<p> Mathematical formula (a + b)<sup>2</sup> = a<sup>2</sup> + b<sup>2</sup> + 2 * a * b</p>
<p> Benzene chemical formula C<sub>6</sub>H<sub>6</sub></p>
```
## Marking up Computer code
* **&lt;code&gt;** - marking up computer code. Usually this element is used along with **&lt;pre&gt;** element.

* **&lt;pre&gt;** - Stands for preformatted text. Retains the formatting of the text. Used to mark up block of computer code while retaining the formatting.
  ```HTML
  <pre>
    <code>
      // HelloWorld.scala
      object HelloWorld {
        def main(args: Array[String]): Unit = {
          println("Hello world")
        }
      }
    </code>
  </pre>
  ```

* **&lt;var&gt;** - Marking up variable names
  ```HTML
  <p> Mathematical formula (<var>a</var> + <var>b</var>)<sup>2</sup> = <var>a</var><sup>2</sup> + <var>b</var><sup>2</sup> + 2 * <var>a</var> * <var>b</var></p>
  ```

* **&lt;kdb&gt;** - marking up keyboard input entered in to computer
  ```HTML
  <!-- shell prompt -->
  <p>girish@girish-computer:~ $ <kbd>ping -c 1 github.com</kbd></p>
  ```

* **&lt;samp&gt;** - marking up output of computer program
  ```HTML
  <p>girish@girish-computer:~ $ <kbd>ping -c 1 github.com</kbd>
  <pre>
  <samp>
  PING github.com (13.234.176.102) 56(84) bytes of data.

  --- github.com ping statistics ---
  1 packets transmitted, 0 received, 100% packet loss, time 0ms
  </samp>
  </pre>
  </p>
  ```

## Marking up times and dates
**&lt;time&gt;** element is used for marking up time and date. Makes the time human readable at the same time machine readable.
```HTML
<!-- <time datetime="machine readable time">Human readable time</time> -->
<time datetime="29-07-2019"> 29<sup>th</sup> of July, 2019</time>
```

## References:
[Advanced text formatting](https://developer.mozilla.org/en-US/docs/Learn/HTML/Introduction_to_HTML/Advanced_text_formatting)