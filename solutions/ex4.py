import numpy as np
import numpy.random as rnd

print("Exercise 4::")
print("  4.1:")
print("    Solution 1:")
x = np.arange(1,7,dtype='int32')
y = np.diag(x*x*x -1) + np.ones((6,6),dtype='int32')
print("  y:\n{0}\n".format(y))

print("    Solution 2:")
# Note: the np.diag method has no dtype field
z = np.diag([(i**3-1) for i in range(1,7)]) +np.ones((6,6))
z = z.astype('int32')
print("  z:\n{0}\n".format(z))

print("  4.2:")
np.set_printoptions(precision=4)  # To make matrices more readable
X = np.random.random(9)
Y = np.random.random(6)
print("  X:{0}\n".format(X))
print("  Y:{0}\n".format(Y))

B = 1./(X[:,np.newaxis] - Y)
print("  B (Corresponding Cauchy Matrix):\n{0}\n".format(B))
