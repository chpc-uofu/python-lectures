import numpy as np
# Exercise 1.a.::
print(f"Exercise 1.a::")
ex = [i for i in range(1,11)]
lst = [2**i for i in ex]
print(f"1D array:\n{np.array(lst)}\n")

# Exercise 1.b::
print(f"Exercise 1.b::")
start = 2.
stop   = 3.
num = 5 
base = 10
dx= (stop - start)/float(num-1)

pt = [ start+i*dx for i in range(num)]
lst = [base**item for item in pt]
print(f"{np.array(lst)}")
print(f"{np.logspace(start,stop,num,base)}\n")

# Exercise 1.c::
print(f"Exercise 1.c::")
lst= range(30,0,-1)
print(f"{np.array(lst).reshape((5,6))}\n")
