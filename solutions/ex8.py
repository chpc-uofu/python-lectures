import numpy as np
import numpy.linalg as nla
import numpy.random as rnd
import scipy.linalg as sla
import matplotlib.pyplot as plt
np.set_printoptions(precision=3)

print(f"Exercise 8.1::")
A = np.array([[3, 1, 1],
              [2, 4, 2],
              [1, 1, 3]])

# Step 1:Eigenvalues, eigenvectors
w ,v = nla.eig(A)
print(f"  Eigenvalues:{w}")
print(f"  Eigenvectors:\n{v}")

# Step 2: Calc. the exponential of the diagonal
expD = np.diag(np.exp(w))

# Step 3: Perform a singularity transform 
res = np.dot(np.dot(v,expD), nla.inv(v))   # Same as: res=v @ expD @ nla.inv(v)

print(f"  Matrix exponential of A:\n{res}")

# Check: using scipy.linalg
print(f"  Matrix exponential of A (using scipy):\n{sla.expm(A)}")      



print(f"Exercise 8.2::")

# Step 1: Generate equidistant intervals in ]0,1]
dx = 0.01
N = int(1.0/dx)
x = np.linspace(dx,1.0,num=N) 
print(f"  N:{N:4d}  dx:{dx}")
print(f"  x:\n{x}")
print(f"  x.shape:{x.shape}\n")

# Step 2: Generate the Covariance Matrix
Cov = np.zeros((x.shape[0],x.shape[0]))
for irow in range(0,x.shape[0]):
    Cov[irow,irow:] = x[irow]
    Cov[irow:,irow] = x[irow]
print(f"  Cov:\n{Cov}\n")

# Step 3: Cholesky decomposition of the Covariance matrix
A = nla.cholesky(Cov)
print(f"  A@A.T:\n{A @ A.T}\n")

# Step 4: Calculate the Brownian paths
#         with X[0]=0
NSIM = 10
res = np.zeros((NSIM,N+1))
for isim in range(NSIM):
    Z = rnd.normal(loc=0.0, scale=1.0, size=x.shape[0])
    X = np.squeeze(A @ Z[:,np.newaxis])
    print(X)
    res[isim,1:] = X
print(f"  res:\n{res}")

# Step 5: Plot the PATHS
x = np.linspace(0,1,num=N+1)
print(f"  x:\n{x}")
for i in range(res.shape[0]):
    plt.plot(x,res[i,:])
