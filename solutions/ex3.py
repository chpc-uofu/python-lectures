import numpy as np
import numpy.random as rnd

print(f"Exercise 3::")
print(f"  3.1:")
A = np.arange(1,31).reshape(5,6)
print(f"  A:\n{A}\n")


B=A[:,:4:2]
print(f"  B:\n{B}\n")

C=A[1,1::2]
print(f"  C:\n{C}")
print(f"  C.shape:{C.shape}\n")

D=A[1:2,1::2]
print(f"  D:\n{D}")
print(f"  D.shape:{D.shape}\n")

E=A[0::3,1::3]
print(f"  E:\n{E}\n")

print(f"\n  3.2:")
X = rnd.random((7,7))
X[2:5,2:5]=0.0
print(f"  X:\n{X}\n")

print(f"\n  3.3:")
Y = np.zeros((8,8),dtype='int32')
Y[::2,1::2]=1
Y[1::2,0::2]=1
print(f"  Y:\n{Y}\n")

tmpl= np.array([[0,1],[1,0]],dtype='int32')
Z =np.tile(tmpl,(4,4))
print(f"  Z:\n{Z}\n")
