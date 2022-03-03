import numpy as np
import numpy.linalg as la
import scipy.linalg as sla

print(f"Exercise 8::")
A = np.array([[3, 1, 1],
              [2, 4, 2],
              [1, 1, 3]])

# Step 1:Eigenvalues, eigenvectors
w ,v = la.eig(A)
print(f"  Eigenvalues:{w}")
print(f"  Eigenvectors:\n{v}")

# Step 2: Calc. the exponential of the diagonal
expD = np.diag(np.exp(w))

# Step 3: Perform a singularity transform 
res = np.dot(np.dot(v,expD), la.inv(v))   # Same as: res=v @ expD @ la.inv(v)

print(f"  Matrix exponential of A:\n{res}")

# Check: using scipy.linalg
print(f"  Matrix exponential of A (using scipy):\n{sla.expm(A)}")      

