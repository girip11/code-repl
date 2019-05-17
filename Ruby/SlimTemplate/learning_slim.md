# Slim Basics
> Slim is a template language whose goal is reduce the syntax to the essential parts without becoming cryptic.

* Sample slim
    ```Slim
        / Comment 
        doctype html
        html
        head
            title Slim Examples
            meta name="keywords" content="template language"
            meta name="author" content=author
            javascript:
            alert('Slim supports embedded javascript!')

        body
            h1 Markup examples

            #content
            p This example shows you what a basic Slim file looks like.

            == yield

            - unless items.empty?
                table
                - items.each do |item|
                    tr
                    td.name = item.name
                    td.price = item.price
            - else
                p
                | No items found.  Please add some inventory.
                Thank you!

            div id="footer"
            = render 'footer'
            | Copyright © #{year} #{author}
    ```

* Easier to write html.No need to enclose html elements inside < or > and no explicit closing tags required. Html documents become much more human readable and less cryptic.
* Slim is used as one of the rendering templates in ruby on rails. Alternate templates are ERB(Embedded Ruby) and HAML.

## Reference:
* [Slim lang](http://slim-lang.com/)
* [Slim introduction article](https://code.tutsplus.com/articles/an-introduction-to-slim-templates--cms-26028)
* [What is slim - rubydocs](https://www.rubydoc.info/gems/slim/frames#What_is_Slim_)
* [Slim cheatsheet](https://devhints.io/slim)