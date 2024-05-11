#print(arrayname[index])
import numpy as np
newarray=np.array([6,4,3,5,7,44])
print(newarray[0])
print(newarray[-1])
print(newarray[-5])
'''indexing of two dimensional array
list1=[[1,2,3],[4,5,6],[7,8,9] it will be saved like this in memory
0c 1c 2c   #here c=column
1  2  3   this is 0th row
4  5  6    1r   #here r =row
7  8  9    2r
if we want to access 8 we will write like this[row,column]=[2,1]'''
secondearray=np.array([[11,22,33],[44,55,66],[77,88,99]])
print(secondearray[1,0])
print(secondearray[0,1])
print(secondearray[2,2])
print("the first row is",secondearray[0,:])
print("the first coulumn is",secondearray[:,0])
print("the whole array is:",secondearray[:,:])

