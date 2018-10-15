import numpy as np
np.set_printoptions(precision=5)

print("Exercise 7::")

# Create the vector
x = np.arange(1,10,dtype='float64')
x[2] = np.nan
x[7] = np.nan
print("  x:\n{0}\n".format(x))

# Create the mask
mask = ~np.isnan(x)
print("  mask:\n{0}\n".format(mask))

# Calculate sum & prod.
print("  sum :{0} & should be:{1}".format(x[mask].sum(),np.nansum(x)))
print("  prod:{0} & should be:{1}".format(x[mask].prod(),np.nanprod(x))) 
