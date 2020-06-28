# ust as non-default arguments have to precede default arguments, so *args must come before **kwargs.
# To recap, the correct order for your parameters is:
#
# 1/ Standard arguments
# 2/ *args arguments
# 3/ **kwargs arguments

def MyFun(Name, *args, **kwargs):
    n1 = Name
    a1 = 0
    k1 = ""

    for arg in args:
        a1 += arg
    for arg in kwargs.values():
        k1 += arg + " "
    return n1, a1, k1

N1, A1, K1 = MyFun("Tomasz", 1,2,3,4,5, a="Te", b="Są", c="Nazwane")

print("n1:", N1)
print("a1:", A1)
print("k1:", K1)