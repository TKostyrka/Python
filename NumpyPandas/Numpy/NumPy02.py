import numpy as np

x = np.random.random((3, 10))
np.savetxt('Files\\test.out', x, delimiter=',')

y = np.loadtxt('Files\\test.out', skiprows=0, unpack=True, delimiter=',')
print(y)