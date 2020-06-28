def my_sum(my_integers):
    result = 0
    for x in my_integers:
        result += x
    return result

list_of_integers = [1, 2, 3]
print("suma 1:", my_sum(list_of_integers))
print("suma 2:", my_sum([7,8,9]))

# --------------------------------------------------------------------------------

def my_sum(*args):
    result = 0
    for x in args:
        result += x
    return result

print("suma 3:", my_sum(2,3,4,5,6,7,8))

# --------------------------------------------------------------------------------
# You’re not required to use the name args. You can choose any name that you prefer

def my_sum(*moje_inty):
    result = 0
    for x in moje_inty:
        result += x
    return result

print("suma 4:", my_sum(1, 1,2,2,1,1))