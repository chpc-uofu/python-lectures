import math
import numpy as np
import numpy.linalg as la
import numpy.random as rnd

print(f"Exercise 8::")
print(f"  8.1:")

A = rnd.random((6,6))
B = ( A+A.T)/2.0

eigval, eigvec = la.eigh(A)
print(f"  B:\n{B}\n".format(B))
print(f"    eig. values:\n{eigval}\n")
print(f"    eig. vector:\n{eigvec}\n")

print(f"  8.2:")
# Generate the elements randomly
n = rnd.randint(4,9)
V = np.arange(1,n+1)
V = V.astype(dtype='int64')

def genVDM(V):
    """
    Generate a Vandermonde matrix based on a vector V
    V = (x1,x2,....xn)
    """
    N  = V.shape[0]
    A = np.hstack([V[:,np.newaxis]**i for i in range(N)])
    return A

def detVDM(V):
    N = V.shape[0]
    res = V - V[0:,np.newaxis]
    mask = np.fromfunction(lambda i,j: i<j,(N,N))
    return np.prod(res[mask])

print(f"  N:{n}")
print(f"  V:\n{V}\n")

A = genVDM(V) 
detA = detVDM(V)
print(f"Own Functions::")
print(f"  A:\n{A}")
print(f"  det(A):{detA}\n")

B = np.vander(V,increasing=True)
detB = la.det(B)
print(f"Check using NumPy::")
print(f"  A:\n{B}".format(B))
print(f"  det(A):{detB}\n".format(detB))
print(f"Diff:{math.fabs(detB-detA):16.12f}")

