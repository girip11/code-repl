
The below document captures the syntax of general markdown.

# Headings in markdown
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

# Spaces and New line in markdown
* Two spaces followed by return (Enter key)
* To introduce a space use **\&nbsp;**
* You can create a new paragraph by leaving a blank line between lines of text.
* Escaping symbols with \ works.

---

# Styling text 
* Bold - Enclose the text between \*\* \*\* or \_\_ \_\_.
    >\*\*Text in bold\*\*   ->  **Text in bold**  
    >\_\_Text in bold\_\_   ->    __Text in bold__

* Italic - enclose the text between \* \* or \_ \_
    >\*Italics styled text\* ->  *Italics styled text*  
    >\_Italics styled text\_  ->  _Italics styled text_

* Bold and italics
  >\*\*Bold and \_italics\_\*\*    ->   **Bold and _italics_**

* Strikethrough - Enclose the text between \~\~ \~\~
  >\~\~This text is striked out\~\~    ->   ~~This text is striked out~~ 

---

# Quoting text
* Quote a text with a ">"

    Example: `> Quoted text`
    > Quoted text


---


# Quoting code
* Single line of code \` \`.   
  > \`printf("hello world");\` will be displayed as  
  
    `printf("hello world");`

* Block of code - Encode between \`\`\` \`\`\`
    > \`\`\`  
    git status  
    git add  
    git commit  
    \`\`\`  

will be displayed as  

```     
    git status  
    git add   
    git commit
```

---


# Links
* Syntax \[Link text\]\(link URL\)
Example - \[Wikipedia\]\(https://www.wikipedia.org\)  
    > [Wikipedia](https://www.wikipedia.org)

* Link URL can be relative path as well.
Example of relative link - **\[Contribution guidelines\]\(docs/CONTRIBUTING.md\)**
    > [Contribution guidelines](docs/CONTRIBUTING.md)

* Link referencing.  
  Syntax - 
  > \[Link text\]\[Link label\]  
  > \[Link Label\]: LinkURL "Title"

  Example:
  > \[Wikipedia\]\[URL\]  
  > \[URL\]: https://www.wikipedia.org "Wikipedia"  

  will be displayed as  

    [Wikipedia][URL]

    [URL]: https://www.wikipedia.org


---

# Lists

## Unordered lists
Prefix with \- or \*  
Example-1  
\* Item1  
\* Item2  
will be displayed as
>* Item1 
>* Item2

Example-2  
\- Item1  
\- Item2  
will be displayed as

> - Item1
> - Item2

## ordered lists
Example  
1. Item1
2. Item2

## Nested lists
Example -  
> 1\. Item1 in list1  
> &nbsp; &nbsp; &nbsp; &nbsp; \- Item1 in first nested list  
> &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;\* Item1 in second nested list  

will be displyed as

1. Item1 in list1
   - Item1 in first nested list
      * Item1 in second nested list


---


# Horizontal rule
Equivalent of \<hr/> tag in HTML. Use 3 \_ or \* or \-to get a horizontal rule.

***
---
___  


# Reference
* [Markdown syntax](https://daringfireball.net/projects/markdown/syntax)
* [Markdown basics](https://help.github.com/en/articles/basic-writing-and-formatting-syntax)
* [Github flavored markdown](https://github.github.com/gfm/)
* [Markdown cheatsheet](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet)
* [Another useful markdown cheatsheet](https://developers.datenstrom.se/help/markdown-cheat-sheet)