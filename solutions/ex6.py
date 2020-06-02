import math
import numpy as np
import numpy.random as rnd
import matplotlib.pyplot as plt
np.set_printoptions(precision=5)

print(f"Exercise 6::")
print(f"  6.1:")
SZ = 10

# Generate random numbers within [0,1(
x = rnd.random(SZ)
y = rnd.random(SZ)

# Map them into a square
x = 2.0*x -1.0
y = 2.0*y -1.0

print(f"  Points IN the Square::")
print(f"    x:\n{x}\n")
print(f"    y:\n{y}\n")

z = x**2 + y**2
mask = (z >1.0)
print(f"    z=(x**2+y**2):\n{z}\n")
print(f"    mask.shape:{mask.shape}")
print(f"    mask (True if OUTSIDE Unit Circle):\n{mask}\n")

# Find points OUTSIDE Unit-circle 
x_out = x[mask]
y_out = y[mask]
print(f"\n  Points OUTSIDE the Unit-circle::")
print(f"    Indices:\{np.nonzero(mask)}\n")
print(f"    Coord:")
print(f"      x (outside unit-circle):\n{x_out}\n")
print(f"      y (outside unit-circle):\n{y_out}\n")

# Set points within Unit-Circle to (0,0)
x[~mask] = 0.0
y[~mask] = 0.0
print(f"\n  Points AFTER setting points IN the Unit-circle to (0.,0.)::")
print(f"      x:\n{x}\n")
print(f"      y:\n{y}\n\n")


print(f"  6.2:")
# Generate the Random Values
x = rnd.random((6,8))
print(f"  x:\n{x}\n")

# Calc. |x_ij - 0.5|
absdiff = np.abs(x-0.5)
print(f"  |x-0.5|:\n{absdiff}\n")

# Find the col. ind for the minimum on each row 
col_ind = absdiff.argmin(axis=1)
print(f"  Column indices:\n{col_ind}\n")

# Corresponding values
values = x[np.arange(x.shape[0]),col_ind]
print(f"  Values:\n{values}\n")
