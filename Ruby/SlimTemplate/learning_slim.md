# Slim Basics
> Slim is a template language whose goal is reduce the syntax to the essential parts without becoming cryptic.

## Sample slim
```Slim
/ Comment 
doctype html
html
head
    title Slim Examples

    meta name="author" content="Girish"
    meta name="description" content="Slim example"

    javascript:
        alert('Slim supports embedded javascript!')

    link{href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" rel="stylesheet"
    integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" 
    crossorigin="anonymous"}

body
    h1 Markup examples

    #content
        p This example shows you what a basic Slim file looks like.

        == yield

        / control code support
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
        / render from another partial slim file
        = render 'footer'

        / String interpolation
        | Copyright © #{year} #{author}
```

* Easier to write html.No need to enclose html elements inside < or > and no explicit closing tags required. Html documents become much more human readable and less cryptic.
* Slim is used as one of the rendering templates in ruby on rails. Alternate templates are ERB(Embedded Ruby) and HAML.

## Learning slim
Install slim gem using the command `gem install slim`. **Slim** gem comes with a commandline tool that interactively converts slim to html. In the commandline, type `slimrb` to start the  interactive console. Type the slim code and enter `Ctrl + D` keyboard combination to get the resulting html.
```Bash
$ gem install slim
$ slimrb
```

## Reference:
* [Slim lang](http://slim-lang.com/)
* [Slim introduction article](https://code.tutsplus.com/articles/an-introduction-to-slim-templates--cms-26028)
* [What is slim - rubydocs](https://www.rubydoc.info/gems/slim/frames#What_is_Slim_)
* [Slim cheatsheet](https://devhints.io/slim)