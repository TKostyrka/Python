words = "Kluby League One zagłosowały za zakończeniem sezonu.".split()
print(words)

l =[len(word) for word in words]
print(l)

#----------------------------------------

from math import factorial

print([factorial(x) for x in range(10)])

print([len(str(factorial(x))) for x in range(10)])
print({len(str(factorial(x))) for x in range(10)})

#----------------------------------------

from math import sqrt

def is_prime(x):
    if x<2:
        return False
    for i in range(2, int(sqrt(x))+1):
        if x % i == 0:
            return False
    return True

prs = [x for x in range(101) if is_prime(x)]
print(prs)
