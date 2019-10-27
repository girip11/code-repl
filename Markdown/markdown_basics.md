# Markdown Basics

The below document captures the syntax of general markdown.

## Headings in markdown

* \# - Heading1 (largest heading)
  > # Heading1

* \#\# - Heading2
  > ## Heading2

* \#\#\# - Heading3
  > ### Heading3

* \#\#\#\# - Heading4
  > #### Heading4

* \#\#\#\#\# - Heading5
  > ##### Heading5

* \#\#\#\#\#\# - Heading6 (smallest heading)
  > ###### Heading6

---

## Spaces and New line in markdown

* Two spaces followed by return (Enter key)
* To introduce a space use **\&nbsp;**
* You can create a new paragraph by leaving a blank line between lines of text.
* Escaping symbols with \ works.

---

## Styling text

| Original Text                  | Displayed Text               |
| ------------------------------ | ---------------------------- |
| `**Text in bold**`             | **Text in bold**             |
| `__Text in bold__`             | __Text in bold__             |
| `*Italics styled text*`        | *Italics styled text*        |
| `_Italics styled text_`        | _Italics styled text_        |
| `**Bold and _italics_**`       | **Bold and _italics_**       |
| `~~This text is striked out~~` | ~~This text is striked out~~ |

---

## Quoting text

* Quote a text with a ">"

Example: `> Quoted text`
> Quoted text.

```Markdown
> Quoted text can be made
> to span multiple lines.
```

The above markdown will be rendered as

> Quoted text can be made to span multiple lines.

---

## Quoting code

* Inline code **\`printf("hello world");\`** will be displayed as `printf("hello world");`

* Block of code

> \`\`\`Bash  
> git status  
> git add  
> git commit  
> \`\`\`

will be displayed as

```Bash
git status
git add
git commit
```

---

## Links

* Syntax `[Link text](link URL)`. `[Wikipedia](https://www.wikipedia.org)` will be displayed as [Wikipedia](https://www.wikipedia.org) |

* Link URL can be relative path as well. `[Contribution guidelines](docs/CONTRIBUTING.md)` markdown snippet will be rendered as [Contribution guidelines](docs/CONTRIBUTING.md)

* Link referencing.

  ```Markdown
  [Link text][Link label]
  [Link Label]: LinkURL "Title"
  ```
  
  The below piece of markdown snippet will be displayed as

  ```Markdown
  Link to [Wikipedia][URL].

  [URL]: https://www.wikipedia.org "Wikipedia"
  ```

  Link to [Wikipedia][URL].

[URL]: https://www.wikipedia.org

---

## Lists

## Unordered lists

```Markdown
List1

* Item1
* Item2

List2

- Item3
- Item4
```

will be displayed as

List1

* Item1
* Item2

List2

- Item3
- Item4

## Ordered lists

```Markdown
1. Item1
2. Item2
```

will be rendered as

1. Item1
2. Item2

## Nested lists

```Markdown
1. Item1 in list1
  - Item1 in first nested list
    * Item1 in second nested list
```

will be rendered as

1. Item1 in list1
  - Item1 in first nested list
    * Item1 in second nested list

---

## Horizontal rule

Equivalent of \<hr/> tag in HTML.

```Markdown
<!-- Syntax -->
***
---
___
```

---

## References

* [Markdown syntax](https://daringfireball.net/projects/markdown/syntax)
* [Markdown basics](https://help.github.com/en/articles/basic-writing-and-formatting-syntax)
* [Github flavored markdown](https://github.github.com/gfm/)
* [Markdown cheatsheet](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet)
* [Another useful markdown cheatsheet](https://developers.datenstrom.se/help/markdown-cheat-sheet)
