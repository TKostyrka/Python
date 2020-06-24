from jinja2 import Environment, FileSystemLoader

content = 'This is about page'

file_loader = FileSystemLoader('htmls')
env = Environment(loader=file_loader)

template = env.get_template('about.html')

output = template.render(content=content)
print(output)