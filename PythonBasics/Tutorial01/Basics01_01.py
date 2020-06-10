print("hello!")

if True:
    print("dummy test!")

if not(False):
    print("dummy test#2 line #1!")
    print("dummy test#2 line #2!")

i=1
while i<=10:
   print("iteration: " + str(i))
   i += 1

while True:
    response = input("provide int:")
    if int(response) % 7 == 0:
        break

