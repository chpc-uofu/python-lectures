import math
import numpy as np
import numpy.random as rnd
import matplotlib.pyplot as plt
np.set_printoptions(precision=5)


print("Exercise 5::")
print("  5.1:")
x = np.arange(1,7)
print("  x:\n{0}\n".format(x))
print("    Solution 1:")
y = np.power(3,x)
print("  y:\n{0}\n".format(y))

print("    Solution 2:")
y = 3**x
print("  y:\n{0}\n".format(y))


print("  5.2:")
A = rnd.random((5,10))
print("  A:\n{0}\n".format(A)) 

max_val = A.max()
print("  Max val for all of A:\n{0}\n".format(max_val))

min_val_eachcol = A.min(axis=0) 
print("  Min. val in each column:\n{0}\n".format(min_val_eachcol))

min_val_fourthrow = A[3,:].min()
print("  Min. val in fourth row:\n{0}\n".format(min_val_fourthrow))

bool_mat = (A < 0.02) | (A > 0.98)
print("  Boolean Matrix:\n{0}\n".format(bool_mat))
print("  Any val <0.02 or >0.98? {0}\n".format(bool_mat.any()))
print("  Corresponding values:\n{0}\n".format(A[bool_mat]))


print("  5.3:")
def calc_sn(n):
    """
    Function which returns an array of 
    partial sums 
    """
    k = np.arange(1,n+1)
    nom = np.sin(k)
    denom = k**2
    return np.cumsum(nom/denom)

N = 100
k = np.arange(1,N+1)
Sk = calc_sn(N)
plt.xlabel("$n$")
plt.ylabel("$S_n$")
plt.title("Convergence of the Partial Sum $S_n$")
plt.plot(k,Sk);
