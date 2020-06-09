try:
    x = 1/0
    print("tego nie będzie")
except ZeroDivisionError:
    print("nope.")
finally:
    print("a to będzie.")