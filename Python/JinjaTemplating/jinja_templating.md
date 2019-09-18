# Jinja templating

## Installation
```Bash
pip3 install jinja2
```

## Delimiters
* `{% %}` - statements 
* `{{ }}` - expressions
* `{# #}` - comments
* `# .. ##` - Line statements

## Variables and filters
Attribute accessing is possible inside the template variables as in `{{ foo.bar }}`

```Python
from jinja2 import Template

# works with both single quotes and double quotes
# commonly used with double quotes.
t= Template("Hello {{name}}, length is {{name.__len__()}}")
t.render(name = "John Doe")
```
Jinja2 has list of [builtin filters](https://jinja.palletsprojects.com/en/2.10.x/templates/#builtin-filters) that can be used on the variables.

```Python
from jinja2 import Template

template_string = "{{ fruits|join(',')}}"
t = Template(template_string)
t.render(['apple', 'mango', 'banana'])
```

## Escaping or Rendering raw template
```Python
t = Template("""
{% raw %}
    <ul>
    {% for item in seq %}
        <li>{{ item }}</li>
    {% endfor %}
    </ul>
{% endraw %}
""")
t.render()
```

## Jinja control structures
* Jinja2 has list of [builtin tests](https://jinja.palletsprojects.com/en/2.10.x/templates/#builtin-tests) that can be used with **if** 

* Within **for** block, we can access some special variables.

```Python
from jinja2 import Template
import random

# if control structure
t = Template("{% if randValue is ge(5)  %} {{print1}} {% else %} {{print2}} {% endif %}")
t.render(randvalue = random.randint(0, 10), print1 = "Hello John", print2 = "Goodbye John")

# for control structure
t = Template("{% for i in range(0, 10) %} {{i}} {% endfor %}")
t.render()
```

## Whitespace control
`-` at the start or end of the block, comment or a variable expression, the whitespace before and after the block will be removed.

```Python
from jinja2 import Template

# adding '-' at the beginning of for block cuts the new line after <ul>
# adding '-' at the end of the for block removes the new line after each <li> element.
template_string= """
<div>
  <ul>
    {%- for item in items %}
      <li>{{item}}</li>
    {%- endfor %}
  </ul>
</div>
"""

print(Template(template_string).render(items = [1,2,3,4,5]))
```

## Template inheritance and super blocks
Define `blocks` in base HTML templates and reuse/override in child templates. In the child templates, `extends` statement is used to specify the inherited template. `{{ super() }}` gets the template content from the parent template. 

> If you want to print a block multiple times, you can, however, use the special self variable and call the block with that name.

**NOTE**: Jinja2 allows block end tags to be named for better readability. 

```HTML
{# base.html.j2 #}

<!DOCTYPE html>
<html lang="en">
<head>
  {% block head %}
    <link rel="stylesheet" href="style.css" />
    <title>{% block title %}{% endblock title %} - My Webpage</title>
  {% endblock head %}
</head>

<body>
  <div id="content">
    {% block content %}
      <p>This is content from base page. </p>
    {% endblock %}
  </div>
  <div id="footer">
    {% block footer %}
      &copy; Copyright
    {% endblock %}
  </div>
</body>
</html>
```
---

```HTML
{# child.html.j2 #}
{% extends "base.html.j2" %}
{% block title %} Child {% endblock %}
{% block head %}
  {# inherit from parent #}
  {{ super() }}
  <script type = "text/javascript">
    console.log("Hello");
  </script>
{% endblock head %}
{% block content %}
    <p>This is content from base page. </p>

    {# any block from parent can be used in child#}
    {% block footer %}
      {{ super() }}
    {% endblock footer %}
{% endblock content %}
```

To run the template inheritance using normal python program, use the below snippet.

```Python
from jinja2 import Template, FileSystemLoader
from jinja2.environment import Environment

# loading templates that use inheritance
env = Environment()
env.loader = FileSystemLoader('.')
template = env.get_template("child.html.j2")
print(template.render())
```

## Manual escaping
```HTML
<!-- escapes the content of name attribute of user object -->
{{ user.name|e }}
```

## Filters
```HTML
{% filter upper %}
  This text will be rendered in uppercase
{% endfilter %}
```
Creation of [custom filters](https://realpython.com/primer-on-jinja-templating/#custom-filters) possible in jinja templating.



## Set variables and block assignments

```Python
from jinja2 import Template

template_string = """
  {% set fruits = ['apple', 'mango', 'orange'] -%}
  <ul>
    {%- for fruit in fruits %}
      <li>{{fruit}}</li>
    {%- endfor %}
  </ul>
"""

t = Template(template_string)
print(t.render())

# block assignments
template_string = """
  {% set fruits %}
    <ul>
      <li>Apple</li>
      <li>orange</li>
    </ul>
  {% endset %}
"""

t = Template(template_string)
t.render(['apple', 'mango', 'orange'])
```

## Include
Include another template contents in to the current namespace. Included templates have variable access of the current context by default.

* `ignore missing` - ignore the statement if the template to be included is missing
* `with context` and `without context` - current contex passed or not.
```HTML
<body>
{% include ['header.html', 'sidebar.html'] ignore missing %}
{# content goes here#}
<p>Hello World</p>
{% include 'footer.html' %}
</body>
```

## Macros
Equivalent to functions in programming languages.

```HTML
{% macro img(src, alt='', title='') -%}
  <img src="{{src}}" alt="{{alt}}" title="{{title}}" width="{{kwargs['width'] | default('')}}" height="{{kwargs['height']|default('')}}">
{%- endmacro  %}

{% macro figcaption(caption) -%}
  <figcaption>{{caption}} : {{varargs|join("_")}}</figcaption>
{%- endmacro  %}

<figure>
  {{ img("http://lorempixel.com/150/200", "placeholder image", "Placeholder image", width=20, height=30) }}
  {{ figcaption('fruits', 'apple', 'orange', 'banana') }}
</figure>
```

Macro has access to special variables
* varargs - list of values
* kwargs - keyword arguments
* `caller()` - macro called from call tag, caller is stored in this variable as callable macro.

Attributes available on macro object
* name - macro name
* arguments - tuple of macro argument names
* defaults - tuple of default values
* catch_kwargs - returns True if macro accepts kwargs
* catch_varargs - returns True if macro accepts varargs
* caller - returns True if macro accesses the special caller variable.

**NOTE**: Macro starting with **one or more underscores** is **private and is not exported and so it can't be imported.**

## call
used for passing macro to another macro.

```HTML
{% macro render_dialog(title, class='dialog') -%}
    <div class="{{ class }}">
        <h2>{{ title }}</h2>
        <div class="contents">
            {{ caller() }}
        </div>
    </div>
{%- endmacro %}

{% call render_dialog('Hello World') %}
    This is a simple dialog rendered by using a macro and
    a call block.
{% endcall %}
```

Passing arguments to `caller()`
```HTML
{% macro dump_users(users) -%}
    <ul>
    {%- for user in users %}
        <li><p>{{ user.username|e }}</p>{{ caller(user) }}</li>
    {%- endfor %}
    </ul>
{%- endmacro %}

{% call(user) dump_users(list_of_user) %}
    <dl>
        <dl>Realname</dl>
        <dd>{{ user.realname|e }}</dd>
        <dl>Description</dl>
        <dd>{{ user.description }}</dd>
    </dl>
{% endcall %}
```

## Import
can import macros from other jinja templates. Importing is similar to python modules. By default current context not passed to the imported templates.

```Python/Jinja2
{# assume we have defined macros in helper.html that contains a macro called img(url, alt, title) #} 
{% import 'helper.html' as helper %}
{{ helper.img('http://lorempixel.com/150/200', 'placeholder image', 'placeholder image') }}
```

---

## References:
* [Jinja templating primer](https://realpython.com/primer-on-jinja-templating/)
* [Jinja templating](https://jinja.palletsprojects.com/en/2.10.x/templates)