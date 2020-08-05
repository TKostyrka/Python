for a in range(1, 6):
    print("-" * 10)
    for b in range(1, 6):
        if a >= b:
            print("{0} x {1} = {2:2}".format(a, b, a*b))

print("-"*80)

# break vs continue

sl = ["milk", "pasta", "eggs", "spam", "brad", "rice"]

for item in sl:
    if item != "spam":
        print(f"buy: {item}")

print("-"*80)

for item in sl:
    if item == "spam":
        continue
    print(f"buy: {item}")

print("-"*80)

for item in sl:
    if item == "spam":
        break
    print(f"buy: {item}")

