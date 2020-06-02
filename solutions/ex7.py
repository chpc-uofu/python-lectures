import numpy as np
np.set_printoptions(precision=5)

print(f"Exercise 7::")

# Create the vector
x = np.arange(1,10,dtype='float64')
x[2] = np.nan
x[7] = np.nan
print(f"  x:\n{x}\n")

# Create the mask
mask = ~np.isnan(x)
print(f"  mask:\n{mask}\n")

# Calculate sum & prod.
print(f"  sum :{x[mask].sum()} & should be:{np.nansum(x)}")
print(f"  prod:{x[mask].prod()} & should be:{np.nanprod(x)}")
