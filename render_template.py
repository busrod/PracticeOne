from jinja2 import Environment, FileSystemLoader

# Load file from filesystem
loader = FileSystemLoader('templates')

# Create an environment
environment = Environment(loader=loader)

# Obtaining our template
tpl = environment.get_template("file.txt")

# Rendering our template
out = tpl.render()
print(out)
