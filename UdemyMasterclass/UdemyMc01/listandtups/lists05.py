
# -------------------------------

itms = ["comp", "moni", "mouse", "keyb", "mat", "mat", "mat", "mat"]

for i in itms:
	print(f"{i}: {id(i)}")

print("-" * 80)

itms.remove("mat")

for i in itms:
	print(f"{i}: {id(i)}")
