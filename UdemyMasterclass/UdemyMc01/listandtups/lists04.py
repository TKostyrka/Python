evs = [2, 4, 6, 8]
ods = [1, 3, 5, 7]

print(min(evs))
print(max(evs))
print(len(evs))

print("mississippi iss:", "mississippi".count("iss"))

# -------------------------------

itms = ["comp", "moni", "mouse", "keyb", "mat"]

for i in itms:
	print(itms.index(i), ":", i)

for i, j in enumerate(itms):
	print(f"{i}: {j}")

# -------------------------------

evs.extend(ods)
print(evs)
evs.sort()
print(evs)
evs.sort(reverse=True)
print(evs)
