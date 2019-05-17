# Slim syntax
Slim template will be executed to generate html which will be served as the view in a rails application. Ruby code if any will be evaluated and placed in the generated output html document.

## HTML Tags
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

* Ruby code is placed following the `ruby:` tag. Code inside this tag won't be part of the generated HTML directly.
We can refer to the variables defined in this ruby block and use it in subsequent statements using "=" or "=="(no escaping) or using string interpolation.
  ```slim
    ruby:
      # This is a ruby comment any ruby expression can be used
      # method calls, arithmetic expressions can be computed in this section.
      ruby_exp = (5 * 10)

    div id="main-content" class="container"
      p = ruby_exp
      p "result of 5 multiplied by 2 is #{ruby_exp}"
  ```

* Ruby code can be executed inline and output can be added to the generated output using "=" and "==" prefixes. Dynamic content (ruby code output in this case) follows "=" or "==".
  ```slim
      ruby:
      	a = '<a href="#" title="test-link">Test link</a>'   
      
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

* inline tags using ":"
  ```slim
      li.style-class
        a href="#" Link1

      / is same as below
      li.style-class: a href="#" Link1

      / or 
      li class="style-class": a href="#" Link1
  ```

* Attribute interpolation inside double quoted strings
  ```slim
  ```

* Using ruby expressions in and as attribute values.
  ```slim
    body
      table
        - for user in users
          td id="user_#{user.id}" class=user.role
            a href=user_action(user, :edit) Edit #{user.name}
            a href=(path_to_user user) = user.name
  ```

* Boolean attributes.
  ```slim
    input type="text" disabled=true
    input type="text" disabled=false
    input type="text" disabled=nil
  ```


## Reference:
* [What is slim - rubydocs](https://www.rubydoc.info/gems/slim/frames#What_is_Slim_)