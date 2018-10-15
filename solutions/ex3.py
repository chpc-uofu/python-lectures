import numpy as np
import numpy.random as rnd

print("Exercise 3::")
print("  3.1:")
A = np.arange(1,31).reshape(5,6)
print("  A:\n{0}\n".format(A))


B=A[:,:4:2]
print("  B:\n{0}\n".format(B))

C=A[1,1::2]
print("  C:\n{0}".format(C))
print("  C.shape:{0}\n".format(C.shape))

D=A[1:2,1::2]
print("  D:\n{0}".format(D))
print("  D.shape:{0}\n".format(D.shape))

E=A[0::3,1::3]
print("  E:\n{0}\n".format(E))

print("\n  3.2:")
X = rnd.random((7,7))
X[2:5,2:5]=0.0
print("  X:\n{0}\n".format(X))

print("\n  3.3:")
Y = np.zeros((8,8),dtype='int32')
Y[::2,1::2]=1
Y[1::2,0::2]=1
print("  Y:\n{0}\n".format(Y))

tmpl= np.array([[0,1],[1,0]],dtype='int32')
Z =np.tile(tmpl,(4,4))
print("  Z:\n{0}\n".format(Z))
