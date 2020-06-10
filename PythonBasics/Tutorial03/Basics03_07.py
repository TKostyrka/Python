l1 = [('a',10),('b',20),('c',31)]
print(l1)

d1 = dict(l1)
print(d1)

d2 = dict(x=9, y=8, z =7)
print(d2)

for d in d1.keys():
    print(d, ":", d1[d])

for d in d2.items():
    print(d[0], ":", d[1])

m = {
    'A' : [1,5],
    'B' : [2,6],
    'C' : [3,7],
    'D' : [4,8]
}

print(type(m), ">>>", m)