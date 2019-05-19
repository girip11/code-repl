# Slim syntax
Slim template will be executed to generate html which will be served as the view in a rails application. Ruby code if any will be evaluated and placed in the generated output html document.

* Use **slimrb** console from **slim** gem to tryout these snippets.

* No angular brackets required. No closing tags needed.
  ```slim
  div id="main-content" class="container"
    p This is a paragraph
  ```

* Comment and html comment
  ```slim
  / This is a comment statement in slim. 
  / This comment wont be present in the generated HTML.
  /! This is a HTML comment. This will be present in the generated HTML.
  ```

* Inline javascript using `javascript:` tag.
  ```Slim
  doctype html
  html
    head
      title Sample slim
      meta name="author" content="Girish"
      javascript:
        alert("Slim supports inline javascript!")
    body
      #content.container
        p 
          | Hello World!!
  ```

* Ruby code is placed following the `ruby:` tag. Code inside this tag won't be part of the generated HTML directly. We can refer to the variables defined in this ruby block and use it in subsequent statements using "=" or "=="(no escaping) or using string interpolation.
  ```slim
  ruby:
    # This is a ruby comment any ruby expression can be used
    # method calls, arithmetic expressions can be computed in this section.
    ruby_exp = (5 * 10)

  div id="main-content" class="container"
    p = ruby_exp
    p "result of 5 multiplied by 2 is #{ruby_exp}"
  ```

* To get the content from slim to html as such without any processing use "|"(**pipe**).
  ```slim
  p
    | This is a verbatim text.
        Text following pipe gets the content as it is in the final html
        including the formatting.

  / HTML can be placed following pipe
  if items.empty?
    | <p>No items!</p>
  ```

* Control statements like if, unless, for are prefixed with **-**
  ```Slim
  ruby:
    items = [1, 2, 3, 4, 5]

  - if items.empty?
      | No items
  - else
      p Total items are #{items.length}
  
  / Loops through the collectiona and places output of each iteration to
  / resulting output html
  - items.each do |item|
      p Item value is #{item}

  / Below also works
  - for item in items
      p Item is  #{item}
  ```

* Ruby code can be executed inline and output can be added to the generated output using "=" and "==" prefixes. Dynamic content (ruby code output in this case) follows "=" or "==". Dynamic content value is html escaped when  **=** is used and no html escaping when  **==** is used. If your ruby code needs to use multiple lines, append a backslash \ at the end of the lines. 
  ```slim
  ruby:
    a = '<a href="#" title="test-link">Test link</a>'
    str = "This is a ruby statement \
    spanning multiple lines"
  
  div id="main-content"
    p = a # escape the value of a
    p == a  # doesnot escape the value of variable
  ```

* Inline html can also be placed inside slim file.
  ```slim
  <html>
    head
      title Example
    <body>
    </body>
  </html>
  ```

* Shorthand for classes(.) and ids(#) which is similar to CSS where id is prefixed with "#" and class with "." when used as the CSS selector.
  ```slim
  / below statements are all equivalent
  div id="main-content" class="container"
  
  / above statement can also be written succintly as below
  div#main-content.container

  / div need not be mentioned explicitly. This is not the case with other html tags
  #main-content.container

  / div with multiple classes
  div id="main-content" class="center jumbotron"

  / Using attribute chaining 
  #main-content.center.jumbotron

  / attribute merging happens in this case. the resulting div will have / two classes
  div.center class="jumbotron"

  / Array can be used for attribute values
  div class=["center", "jumbotron"]

  / Below syntax also causes attributes to be merged
  div class=:center,:jumbotron

  / attribute wrapping using {} or [] or ()
  / helps attributes span across multiple lines
  nav{class="navbar navbar-fixed-top"
      id="navigation-links"}
  ```

* html doctype for html5
  ```slim
  doctype 5

  / or

  doctype html
  ```

* Closing tags with "/" and leading and trailing spaces with "<" and ">".
  ```slim
  / ending statement with "/" to denote closing tags.
  / Closing tags are actually not required.
  img src="favicon.png" /

  / Adds trailing whitespace in the generated HTML
  a> href='url1' Link1

  / Adds leading whitespace in the generated HTML
  a< href='url2' Link2

  / Adds leading and trailing whitespace in the generated HTML 
  a<> href='url3' Link3
  ```

* Inline html elements using ":" instead of placing in newline
  ```slim
  li.style-class
    a href="#" Link1

  / is same as below
  li.style-class: a href="#" Link1

  / or 
  li class="style-class": a href="#" Link1
  ```

* Text interpolation for attributes values inside double quoted strings
  ```slim
  ruby:
    div_alignment = "center"
    url = "https://www.google.com"
  div class="#{div_alignment} jumbotron"

  / break quoted attributes across multiple lines using "\"
  div class="navbar navbar-fixed-top  \
            navbar-inverse"
  ```

* Using ruby code for attribute values. Ruby code is placed directly after the "=". Output of the ruby code will become the attribute value. Ruby code with spaces is enclosed in **(...)**. Hashes and arrays can be written directly.
  ```slim
  body
    #content.container
      / ruby code is placed after the "=". Observe the use of paranthesis when ruby code has spaces 
      a href=get_url(param1, :action) Dynamic output url
      a href=(get_url param1 :action) Dynamic output url
  ```

* Boolean attributes can have **true**, **false** and **nil** values. **nil** is a ruby object that represents nothing but in a boolean expression evaluates to false.
  ```slim
  input type="text" disabled=true
  input type="text" disabled=false
  input type="text" disabled=nil
  ```

* Splat attributes be placing * followed by ruby hash. This turns ruby hash to attribute value pairs. Prefix for splattng can also be changed using `splat_prefix` option.
  ```Slim
  / Splat attributes using hash
  .container *{'data-url'=>place_path(place), 'data-id'=>place.id} = place.name
  
  / The below statement takes care of attribute merging as well.
  .container *{class: [:center, :jumbotron]} 

  / Use ruby method calls that return hash or hash instance variable
  .container *method_which_returns_hash = item.name
  .container *@hash_instance_variable = item.name
  ```

* Dynamic tags can be embedded using splat attributes. The hash has to contain a key called **tag** and the value is the required html tag
  ```Slim
  ruby:
    def get_item_url(item)
      item.url.nil? ? {tag: 'span', class: 'no-url'} : {tag: 'a', href="#{item.url}"}
    end

  *get_item_url(item) = item.name
  ```

## Reference:
* [What is slim - rubydocs](https://www.rubydoc.info/gems/slim/frames#What_is_Slim_)