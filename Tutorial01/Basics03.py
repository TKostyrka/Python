polsk = "jakiś tekścik pą pąłskięmu"
data = polsk.encode('utf8')

print(polsk)
print(data)

# --------------------------------------

z = [1,2,3]
x = ["aple", "banana", "orange"]

print(x)
print(x[2])

x.append("pear")
print(x)

# --------------------------------------

di = {'tomasz' : 123456, 'michał' : 654987}
print(di)

di['tadek'] = 885522
print(di)
print(di['tadek'])

for d in di:
    print(d)

for d in di:
    print(d,":", di[d])