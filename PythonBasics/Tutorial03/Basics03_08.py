p = {123,43,543345,666}
print(type(p))


t = [1,2,5,4,3,4,4,2,3,1,2,3,4,1]
s = set(t)

print(t)
print(s)

#-------------------------------------------------

s1 = {1,2,3}
s2 = {3,4,5}

print("u: ", s1.union(s2))
print("i: ", s1.intersection(s2))
print("d: ", s1.difference(s2))