import numpy as np

x = np.random.random((3, 5))

print("x:\n", x)
print("x[0,:]:\n", x[0,:])
print("x[0,0]:\n", x[0,0])
print("x[:,0]:\n", x[:,0])

b3 = [x > 0.8]
print("b3:\n", b3)

print("x<0.2:\n", x[x < 0.2])
print("x[b3]:\n", x[tuple(b3)])