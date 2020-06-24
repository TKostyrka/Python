from jinja2 import Template

person = { 'name': 'Kokosz', 'age': 34 }

tm = Template("My name is {{ per.name }} and I am {{ per.age }}")
msg = tm.render(per=person)

print(msg)

