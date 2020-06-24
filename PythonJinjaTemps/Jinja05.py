from jinja2 import Template

data = '''
{% raw %}
His name is {{ name }}
{% endraw %}
'''

tm = Template(data)
msg = tm.render(name='Peter')

# this should not work! (it should print "His name is {{ name }}")
print(msg)