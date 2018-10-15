import numpy as np
# Exercise 1.a.::
print("Exercise 1.a::")
ex = [i for i in range(1,11)]
lst = [2**i for i in ex]
print("1D array:\n{0}\n".format(np.array(lst)))

# Exercise 1.b::
print("Exercise 1.b::")
start = 2.
stop   = 3.
num = 5 
base = 10
dx= (stop - start)/float(num-1)

pt = [ start+i*dx for i in range(num)]
lst = [base**item for item in pt]
print("{0}".format(np.array(lst)))
print("{0}\n".format(np.logspace(start,stop,num,base)))

# Exercise 1.c::
print("Exercise 1.c::")
lst= range(30,0,-1)
print("{0}\n".format(np.array(lst).reshape((5,6))))
