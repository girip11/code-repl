# Document and Website Structure

## Sections of a document
* **Header** - Usually contains heading, optionally website logo
* **Navigation menu** - contains links for navigation within the site. This navigation menu is recommended to be consistent for all pages of the website. Generally navigation menu is consisdered to be part of header and the same content is shared across all the pages.
* **Main content** - contains the content fo the webpage
* **Sidebar** - May contain information about the author of the page, quotes, links to related articles etc.
* **Footer** - copyright notices, contact information, sitemap(quick access to popular content) etc

## HTML tags used for document structuring
* **&lt;header&gt;** - contains header information. This element when placed inside body, contains the page level header information and when placed inside **&lt;article&gt;** or **&lt;section&gt;**, represents the section level header information.

* **&lt;nav&gt;** - navigation bar. **&lt;nav&gt;** semantically cannot contain another **&lt;nav&gt;**. This element contains only the primary navigation links.

* **&lt;main&gt;** is used to enclose the document content area. There should be only one **&lt;main&gt;** element per document and placed as direct child of **&lt;body&gt;**. Within the **&lt;main&gt;** element, **&lt;article&gt;**, **&lt;section&gt;**, **&lt;div&gt;** are all used for sectioning the content.

* **&lt;article&gt;** - contains content that makes sense on its own like a blog post.

* **&lt;section&gt;** - contains content that forms a section of the document, for instance image section, map section in a document, sections in a blog post etc. Good practice to begin section with a heading.

* **&lt;aside&gt;** is used for sidebar content and usually placed inside **&lt;main&gt;**

* **&lt;footer&gt;** - contains the footer information.

* **&lt;div&gt;** - generic container for the content. When a content can't be semantically associated with any of the sectioning elements mentioned above, then the content is enclosed inside **&lt;div&gt;** element.

**NOTE**: **&lt;article&gt;** can be comprised of many **&lt;section&gt;**, or **&lt;section&gt;** can be comprised of many **&lt;article&gt;** based on the context.

## References:
* [Document structure](https://developer.mozilla.org/en-US/docs/Learn/HTML/Introduction_to_HTML/Document_and_website_structure)