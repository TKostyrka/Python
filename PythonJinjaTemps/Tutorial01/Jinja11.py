from jinja2 import Template

cars = [
    {'name': 'Audi', 'price': 23000},
    {'name': 'Skoda', 'price': 17300},
    {'name': 'Volvo', 'price': 44300},
    {'name': 'Volkswagen', 'price': 21300}
]

tm = Template(
"""
The sum of car prices is {{ cars | sum(attribute='price') }}
    {% for car in cars %}{% if car.price > 20000 %}{{- car.name }} is expensive.
    {% endif %}
    {%- endfor %}
"""
)

output = tm.render(cars = cars)
print(output)