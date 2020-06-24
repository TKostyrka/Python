from jinja2 import Template
from classes.Person import Person

person = Person('Peter', 34)

tm = Template("My name is {{ per.get_name() }} and I am {{ per.get_age() }}")
msg = tm.render(per=person)

print(msg)