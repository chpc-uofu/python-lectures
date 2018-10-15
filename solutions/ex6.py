import math
import numpy as np
import numpy.random as rnd
import matplotlib.pyplot as plt
np.set_printoptions(precision=5)

print("Exercise 6::")
print("  6.1:")
SZ = 10

# Generate random numbers within [0,1(
x = rnd.random(SZ)
y = rnd.random(SZ)

# Map them into a square
x = 2.0*x -1.0
y = 2.0*y -1.0

print("  Points IN the Square::")
print("    x:\n{0}\n".format(x)) 
print("    y:\n{0}\n".format(y)) 

z = x**2 + y**2
mask = (z >1.0)
print("    z=(x**2+y**2):\n{0}\n".format(z))
print("    mask.shape:{0}".format(mask.shape))
print("    mask (True if OUTSIDE Unit Circle):\n{0}\n".format(mask))

# Find points OUTSIDE Unit-circle 
x_out = x[mask]
y_out = y[mask]
print("\n  Points OUTSIDE the Unit-circle::")
print("    Indices:\{0}\n".format(np.nonzero(mask)))
print("    Coord:")
print("      x (outside unit-circle):\n{0}\n".format(x_out))
print("      y (outside unit-circle):\n{0}\n".format(y_out))

# Set points within Unit-Circle to (0,0)
x[~mask] = 0.0
y[~mask] = 0.0
print("\n  Points AFTER setting points IN the Unit-circle to (0.,0.)::")
print("      x:\n{0}\n".format(x))
print("      y:\n{0}\n\n".format(y))


print("  6.2:")
# Generate the Random Values
x = rnd.random((6,8))
print("  x:\n{0}\n".format(x))

# Calc. |x_ij - 0.5|
absdiff = np.abs(x-0.5)
print("  |x-0.5|:\n{0}\n".format(absdiff))

# Find the col. ind for the minimum on each row 
col_ind = absdiff.argmin(axis=1)
print("  Column indices:\n{0}\n".format(col_ind))

# Corresponding values
values = x[np.arange(x.shape[0]),col_ind]
print("  Values:\n{0}\n".format(values))
