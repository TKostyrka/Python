r = [1123,32,4324,546,76,56,789]
print(r[-2])
print(r[2:4])

s = [[-1,1]] * 5
print(s)
print(s[2])

s[2].append(7)
print(s)

# ------------------------------------------------------------

w = "the quick brown fox jumps over the lazy dog".split()
print(w)

print("first fox:",w.index("fox"))

print("cont the:",w.count("the"))
print("first the:",w.index("the"))

j = w.index("unicorn")