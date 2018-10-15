import numpy as np

print("Exercise 2::")
print("  2.1:")
a  = np.fromfunction(lambda x,y: x+y,(5,5),dtype='int32')
print(" a:\n{0}\n".format(a))

print("  2.2:")
b = np.eye(6,6) + np.eye(6,6,k=1) + np.eye(6,6,k=-1)
b = b.astype(dtype='bool')
print(" b:\n{0}\n".format(b))
