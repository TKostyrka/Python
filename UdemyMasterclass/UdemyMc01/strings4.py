sq = ["comp", "monit", "keyboard"]

print(sq)
print(sq[1])
print(sq[1][2:4])

print("hello! " * 15)

today = "friday"
print("day" in today)
print(today, "day" in today)

i = 40
print("a) number:", str(i))
print("b) number: {0}".format(i))

for i in range(1, 11):
    print("No. {0} squared is {1} and cubed is {2}".format(i, i**2, i**3))
print()

for i in range(1, 11):
    print("No. {0:2} squared is {1:4} and cubed is {2:4}".format(i, i**2, i**3))
print()

print("Pi is approx. {0:12}".format(22/7))
print(f"Pi is approx. {22/7:12}")

for i in range(1, 11):
    print(f"No. {i:2} squared is {i**2:4} and cubed is {i**3:4}")
print()
