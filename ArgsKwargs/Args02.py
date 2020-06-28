# Okay, now you’ve understood what *args is for, but what about **kwargs?
# **kwargs works just like *args, but instead of accepting positional arguments it accepts keyword (or named) arguments.

def concatenate(**kwargs):
    result = ""
    for arg in kwargs.values():
        result += arg + " "
    return result

print(concatenate(a="Real", b="Python", c="Is", d="Great", e="!"))

# ---------------------------------------------------------------

def concatenate(**words):
    r1 = ""
    r2 = ""
    for arg in words:
        r1 += arg
    for arg in words.values():
        r2 += arg
    return r1, r2

a1, a2 = concatenate(a="Real", b="Python", c="Is", d="Great", e="!")

print("keys:", a1)
print("values:", a2)