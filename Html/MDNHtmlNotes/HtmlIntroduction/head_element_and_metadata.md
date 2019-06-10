# Metadata of Html Document
Covers details on various metadata that can be specified in HTML document and their purpose.

## Setting the language of the HTML document
The root element **html** can have a **lang** attribute. This would help search engines index the HTML document more effectively as well as helpful for screen readers to correctly pronounce a word.
```HTML
<html lang = "en-US">
</html>
```
* Inside html document, if we are using parts of characters from other languages, we can use the **lang** attribute and the corresponding ISO language code(ISO 639-1 standard).

## Head Element in Html
Head tag contains the metadata of the HTML document. Usually metadata of an HTML document contains some or all of the things menitoned below.

* Title of the HTML document
* Information about the author of the document, description, keywords, language character set etc
* Metadata with custom properties apart from the standard ones mentioned above like open graph protocol, twitter. 
* Adding Icon for the HTML document
* Adding information about CSS and JS either as link to external files or containing code internal to the HTML document.

## Title of HTML Document
 Title of an HTML document is assigned via the **&lt;title&gt;** element. This title gets displayed in the browser tag and is usually used as teh document name while bookmarking.

## Standard metadata of HTML document 
Metadata like author, description of HTML document can be added via the **&lt;meta&gt;** element.  
```HTML
    <!-- meta element is an empty element. No closing tags required -->
    <meta charset = "utf-8">

    <!-- if meta tag contains name and content pairs, it cannnot contain other attributes like charset, lang etc -->
    <!-- name and content attributes go together.
    Name attribute contains the type of metadata getting defined and the content attribute contains the value for the metadata mentioned in the name attribute. -->
    <!-- Metadata like description, keywords might be indexed by search engines. So its helpful to set these metadata-->
    <meta name="author" content="Girish">
    <meta name="description" content="Document containing information about specifying metadata in HTML documents">
    <meta name="keywords" content="HTML, Head element, metadata">
```

## Custom metadata for representation in various websites like Facebook
* HTML documents with certain metadata tags can be well represented when shared in websites like Facebook, twitter.
* These websites look for certain metadata tags can defined by their protocol. For instance, Facebook follows [open graph data metadata protocol](https://developers.facebook.com/docs/sharing/webmasters/).
```HTML
<!-- Open graph data metadata -->
<meta property="og:image" content="https://www.phoca.cz/images/projects/phoca-favicon-r.svg">
<meta property="og:description" content="Document containing information about specifying metadata in HTML documents">
<meta property="og:title" content="HTML document metadata">
```

## Adding Icon to the HTML document
Icon can be added to the HTML document via the **&lt;link&gt;** element. Link element is also an empty element.
```HTML
    <link rel="icon" href="favicon.ico" type="image/icon">
```

## Adding CSS Internallly and externally
Link to external CSS scripts can be added via the link element.
```HTML
<!-- href can be relative or point to another external URL -->
<link rel="stylesheet" href="style.css" type="text/css" >
<link rel="stylesheet" type="text/css" href="http://mysite.com/styles.css">
```
Internally style can be added using the **&lt;style&gt;** element.
```HTML
<!DOCTYPE html>
<html lang="en-US">
    <head>
        <style>
            * {
                box-sizing: border-box;
            }
        </style>
    </head>

    <body>
    </body>
</html>
```

## Adding Javascript to the HTML document
* Internal or external Javascript can be added via the **&lt;script&gt;** element. These scripts can also be added in body section. Adding JS scripts at the end of the body is preferred if JS code performs any operation on any HTML element inside the body, so that the HTML element is available for JS code to act up on.

```HTML
    <!-- Internal java script -->
    <script type="text/javascript">
       // Javascript code here 
    </script>

    <script src="link-to-external-js.js" type="text/javascript" />
``` 

## Reference
* [HTML Document metadata](https://developer.mozilla.org/en-US/docs/Learn/HTML/Introduction_to_HTML/The_head_metadata_in_HTML)