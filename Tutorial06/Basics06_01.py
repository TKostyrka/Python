f = open("document.txt", "r")
print(f.read())
f.close()

# ---------------------------------------------------------------

f = open("document01.txt", "w+")
f.write('Add new line 01\n')
f.write('Add new line 02\n')
f.write('Add new line 03\nend')
f.close()

# ---------------------------------------------------------------

f = open("document01.txt", "r")
print(f.read(10))
print(f.read())

f.seek(0)
print(f.read())

f.seek(0)
print("l1:",f.readline())
print("l2:",f.readline())

f.seek(0)
x = f.readlines()
print(x)

f.close()

# ---------------------------------------------------------------

f = open("document01.txt", "a")
f.writelines(
    ['\n01: sadkhiauhdiuhas ',
     '\n02: daushdkaskdjhakdhaksuhdkas',
     '\n03: suahdiukashdaskdaskd',
     '\n04: fushdfjhsdkfuhds']
)

f.close()
f = open("document01.txt", "r")
print(f.read())
f.close()

