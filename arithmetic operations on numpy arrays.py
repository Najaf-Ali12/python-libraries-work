#for arithmetic operations the size of arrays should be same(size means order):
import numpy as np
x=np.array([[1,3],
            [11,4]])
y=np.array([[12,2],
            [4,9]])
print("the addition of two arrays is\n",x+y)
print("the subtraction is\n",x-y)
print("the multiplication is \n",x*y)   #this will just multiply elements not like that in matrix
print("the matrix multiplication :\n",x@y)   #this will multiply matrices as we do in mathematics
print("the division is\n",x/y)
print("the floar divison is \n",x//y)  #it will give values in integer not in float
print("the exponentation is \n",x**y)  #it will do(1 power 12,3 power 2,11 power 4 and 4 power9)
print("the remainder is\n",x%y)  #it will work orderwise like (1%12,3%2,11%4 and 4%9)
print(x.transpose())  #it will give transpose of x by exchanging the rows and columns of x and y