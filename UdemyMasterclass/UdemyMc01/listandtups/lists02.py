var01 = 1
var02 = 2

print(id(var01), var01)
print(id(var02), var02)

var01 = var02
var02 += 1

print("-" * 80)

print(id(var01), var01)
print(id(var02), var02)

var03 = True
var04 = True
var05 = 3

print("-" * 80)

print(id(var03), var03)
print(id(var04), var04)
print(id(var05), var05)

