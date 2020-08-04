for i in range(1, 10):
    print(f"No. {i:4} {i**2:4} {i**3:4}")

age = 17
if age >= 18:
    print("\nold enough to vote")
else:
    print("please come back in {0} year(s)".format(18-age))

age = int(input("give age:"))
if age >= 40:
    print("old")
elif age >= 18:
    print("middle")
else:
    print("young")
