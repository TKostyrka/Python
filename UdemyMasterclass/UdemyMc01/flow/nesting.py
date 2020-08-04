for a in range(1, 6):
    print("-" * 10)
    for b in range(1, 6):
        if a >= b:
            print("{0} x {1} = {2:2}".format(a, b, a*b))
