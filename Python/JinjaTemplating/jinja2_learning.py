from jinja2 import Template, FileSystemLoader
from jinja2.environment import Environment

# loading templates that use inheritance
env = Environment()
env.loader = FileSystemLoader('.')
template = env.get_template("template.html.j2")
print(template.render())
