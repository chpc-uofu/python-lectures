import math
import numpy as np
import numpy.linalg as la
import numpy.random as rnd

print("Exercise 8::")
print("  8.1:")

A = rnd.random((6,6))
B = ( A+A.T)/2.0

eigval, eigvec = la.eigh(A)
print("  B:\n{0}\n".format(B))
print("    eig. values:\n{0}\n".format(eigval))
print("    eig. vector:\n{0}\n".format(eigvec))

print("  8.2:")
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

print("  N:{0}".format(n))
print("  V:\n{0}\n".format(V))

A = genVDM(V) 
detA = detVDM(V)
print("Own Functions::")
print("  A:\n{0}".format(A))
print("  det(A):{0}\n".format(detA))

B = np.vander(V,increasing=True)
detB = la.det(B)
print("Check using NumPy::")
print("  A:\n{0}".format(B))
print("  det(A):{0}\n".format(detB))
print("Diff:{0:16.12f}".format(math.fabs(detB-detA)))

