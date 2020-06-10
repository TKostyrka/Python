z = sum(x*x for x in range(1,10000001))
print(z)

print(any([True, False, True]))
print(all([True, False, True]))
print(all([True, True]))

sunday = [12,23,45,32,34,43,12,54]
monday = [87,45,23,43,54,22,34,12]

for item in zip(sunday, monday):
    print(item)

for sun, mon in zip(sunday, monday):
    print("avg: ", (sun+mon)/2)