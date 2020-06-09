t = ("Norway", 4.987, 5)

print("type:",type(t))
print("t2:",t[2])
print("len:", len(t))
for item in t:
    print(item)

# ------------------------------------------------------

def minmax(items):
    return min(items), max(items)

x = [1,2,3,4,5,6]
print(minmax(x))
lower, upper = minmax(x)

print(lower)
print(upper)

# ------------------------------------------------------

lets = ";".join(["a","b","c","d","e","f"])
print(lets)

x = "unforgetable".partition('forget')
print(x)

dept,sep,arr = "London:Edinburgh".partition(":")
print(dept,sep,arr)