# Hyperlinks

## Anatomy of a link
Links are represented using anchor tags(&lt;a&gt;) in HTML. **href** attribute contains the URL location and the title contains the description of what the URL is about.
```HTML
<!-- <a href="URL" title="URL title for tooltip"> Link Text</a> -->
<a href="www.gnu.org" title="GNU website">GNU home</a>
```

## Block level links
Block level elements can be turned in to a link be embedding them inside the anchor tags.
```HTML
<a href="https://www.mozilla.org/en-US/">
  <img src="mozilla-image.png" alt="mozilla logo that links to the mozilla homepage">
</a>
```

## Link to a HTML document fragment
Assign **id** attribute to the HTML element to which the link should point to. Common practice is to assign id to a specific heading on the document. That section can be referred  in the same HTML document in the format `href="#id"`. If the section is referenced in another html document, then in the href attribute mention the html document followed by hash/pound symbol `href="doc.html#id"`. 

```HTML
<!-- Some heading in a HTML document called postgres.html-->
<h2 id="installation">Postgresql installation</h2>

<!-- Link to the installation section looks like below. Clicking on this navigates to the html document and also navigates to the mentioned section in that document-->
<a href="postgres.html#installation">Postgresql installation</a>
```

## Absolute vs relative URLS
* Absolute URLs contain the server domain name and the path to the file in that server as in example `http://www.example.com/directory/index.html`
* Relative URL refers the document path relative to the current document from which its referenced. This makes relative URLs to be used with caution as moving the html document in the file system may invalidate the relative URLS in that document.

## Best practices
* Link text is **should describe** about the link **unlike** in this example `<a href="https://firefox.com/">Click here</a>`

* Link text should not contain the URL itself. Such links lose accessibility.

* Link text should be as short as possible

* Make the link text to link mapping unique throughout the document. For instance using **click here** as link text for multiple URLs is considered as bad practice. Also for all references of the same link, use the same link text.

* Use relative URLs wherever possible, because it avoids DNS lookup which happens with absolute URLs.

* Link text should represent what's the action that happens when you click on the link. For instance, clicking a link might start downloading a file or start playing a video. Descriptive link text helps users getting into such undesired actions.
  ```HTML
  <p><a href="http://www.example.com/large-report.pdf">
    Download the sales report (PDF, 10MB)
  </a></p>

  <p><a href="http://www.example.com/video-stream/" target="_blank">
    Watch the video (stream opens in separate tab, HD quality)
  </a></p>

  <p><a href="http://www.example.com/car-game">
    Play the car game (requires Flash)
  </a></p>
  ```

* using **download** attribute helps to provide a default filename to save on trigeering the download.
`<a href="https://www.ruby-lang.org/en/downloads/" title="Download ruby 2.6.3" download="ruby-2_6_3.exe">Download Ruby 2.6.3</a>`


## Email links
```HTML
<!-- Mail using the prefix "mailto:" in href -->
<!-- Specifying destination mail id is optional  -->
<a href="mailto:girip@example.com">Send email to Girish</a>

<!-- We can add other mail fields like subject, cc, bcc and body. Values of these fields must be URL encoded-->
<a href="mailto:client@example.com?cc=ccclient@example.com&subject=Hello&body=email%20body">Send email to Client</a>
```

## References:
* [Creating hyperlinks](https://developer.mozilla.org/en-US/docs/Learn/HTML/Introduction_to_HTML/Creating_hyperlinks)