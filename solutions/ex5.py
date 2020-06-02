import math
import numpy as np
import numpy.random as rnd
import matplotlib.pyplot as plt
np.set_printoptions(precision=5)


print(f"Exercise 5::")
print(f"  5.1:")
x = np.arange(1,7)
print(f"  x:\n{x}\n")
print(f"    Solution 1:")
y = np.power(3,x)
print(f"  y:\n{y}\n")

print(f"    Solution 2:")
y = 3**x
print(f"  y:\n{y}\n")


print(f"  5.2:")
A = rnd.random((5,10))
print(f"  A:\n{A}\n")

max_val = A.max()
print(f"  Max val for all of A:\n{max_val}\n")

min_val_eachcol = A.min(axis=0) 
print(f"  Min. val in each column:\n{min_val_eachcol}\n")

min_val_fourthrow = A[3,:].min()
print(f"  Min. val in fourth row:\n{min_val_fourthrow}\n")

bool_mat = (A < 0.02) | (A > 0.98)
print(f"  Boolean Matrix:\n{bool_mat}\n".format(bool_mat))
print(f"  Any val <0.02 or >0.98? {bool_mat.any()}\n")
print(f"  Corresponding values:\n{A[bool_mat]}\n")


print(f"  5.3:")
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
