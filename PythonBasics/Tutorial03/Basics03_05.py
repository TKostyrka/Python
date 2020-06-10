x = "The age of {0} is {1}. {0}'s birthsday is on Oct 31st".format("Koksoz", 33)
print(x)

y = f"wynikiem działania jest: {123 * 45}."
print(y)

# ---------------------------------------

import datetime
z = f"The current time is {datetime.datetime.now().isoformat()}"
print(z)

# ---------------------------------------

import math

k = f"Math: pi = {math.pi:.5f}, e = {math.e:.5f}"
print(k)

# ---------------------------------------

t = [12312,3242,24254234,5687]
for p in enumerate(t):
    print(p)

for i,v in enumerate(t):
    print(f"i = {i}, val = {v}")