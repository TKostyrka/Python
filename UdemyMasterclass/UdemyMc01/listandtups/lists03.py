itms = ["comp", "moni", "mouse", "keyb", "mat"]

print(f"itms:{id(itms):10}")

for itm in itms:
	print(f"{itm:10}:{id(itm):10}")

print("-" * 80)

itms.append("headset")

print(f"itms:{id(itms):10}")

for itm in itms:
	print(f"{itm:10}:{id(itm):10}")

print("-" * 80)

# ------------------------------------------------

second_list = itms
second_list.append("additional item")

print(itms[-1])
