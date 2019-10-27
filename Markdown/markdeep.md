# Markdeep Basics

> [Markdeep]((http://casual-effects.com/markdeep/)) is a technology for writing plain text documents that will look good in any web browser, whether local or remote. It supports diagrams, calendars, equations, and other features as extensions of Markdown syntax.

Markdeep files have **.md.html** as the extension.

Markdeep syntax documentation can be found [here](https://casual-effects.com/markdeep/features.md.html?noformat)

Markdeep document can be composed for varoius purposes using the right stylesheets. Stylesheets are available for the following purposes.

* API documentation
* Latex article
* Presentation slides
* Dark mode

## Exporting markdeep document

Exporting to PDF using **google chrome** or **chromium**

```Bash
# For google chrome use "google-chrome" instead of "chromium"
# using chromium browser
chromium --headless --print-to-pdf=[output.pdf] [Markdown_FILE_URL]

# Example
chromium --headless --print-to-pdf=[output.pdf] 'file:///home/girish/Documents/Tryouts/markdeep/example.md.html'
```

---

Converting to word document involves two steps.

* Convert markdeep document to HTML document by opening the markdeep document in the browser with **export** option and save the resulting file. You can also use [**markdeep-rasterizer**][MarkdeepRasterizer] for converting to HTML.

  ```bash
  # installs markdeep-rasterizer
  npm i markdeep-rasterizer

  # command to convert to HTML
  node_modules/.bin/markdeep-rasterizer example.md.html .
  ```

* Using [**pandoc**][Pandoc] convert the html file to the word document file.

  ```bash
  pandoc -f html -t docx example.html -o example.docx
  ```

## References

* [Markdeep](http://casual-effects.com/markdeep/)
* [Markdeep Rasterizer][MarkdeepRasterizer]
* [Pandoc - Universal document converter][Pandoc]

[MarkdeepRasterizer]: https://github.com/romainguy/markdeep-rasterizer
[PanDoc]: https://pandoc.org/
