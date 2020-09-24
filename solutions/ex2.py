import numpy as np
import numpy.linalg as la
np.set_printoptions(precision=4)

print(f"Exercise 2::")
print(f"  2.1:")
a  = np.fromfunction(lambda x,y: x+y,(5,5),dtype='int32')
print(f" a:\n{a}\n")

print(f"  2.2:")
b = np.eye(6,6) + np.eye(6,6,k=1) + np.eye(6,6,k=-1)
b = b.astype(dtype='bool')
print(f" b:\n{b}\n")

print(f"  2.3:")
p = 0.7
n = 10000
sz= 8
up  = np.diag([1.0] + (sz-2)*[p], k= 1)
low = np.diag((sz-2)*[1.0-p] + [1.0], k=-1)
P = up+low
print(f" P:\n{P}")
Pn = la.matrix_power(P,n)
print(f" P^{n}:\n{Pn}")
