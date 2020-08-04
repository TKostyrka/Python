n = "319873%3212; 324; 2342, ^432"
s = ""

for c in n:
    if not c.isnumeric():
        s = s + c

print(s)
