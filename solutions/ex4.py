import numpy as np
import numpy.random as rnd

print(f"Exercise 4::")
print(f"  4.1:")
print(f"    Solution 1:")
x = np.arange(1,7,dtype='int32')
y = np.diag(x*x*x -1) + np.ones((6,6),dtype='int32')
print(f"  y:\n{y}\n")

print(f"    Solution 2:")
# Note: the np.diag method has no dtype field
z = np.diag([(i**3-1) for i in range(1,7)]) +np.ones((6,6))
z = z.astype('int32')
print(f"  z:\n{z}\n")

print(f"  4.2:")
np.set_printoptions(precision=4)  # To make matrices more readable
X = np.random.random(9)
Y = np.random.random(6)
print(f"  X:{X}\n")
print(f"  Y:{Y}\n")

B = 1./(X[:,np.newaxis] - Y)
print(f"  B (Corresponding Cauchy Matrix):\n{B}\n")
