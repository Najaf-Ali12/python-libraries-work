'''sorting in numpy arrays
1:np.sort(arrayname)    it will return a sorted copy of an array
2:np.argsort(arrayname)  it will return the indices that would sort the array
3:arrayname.sort()       uses array name and sort it at place doesnot create its copy like above'''
import numpy as np
#use of sort method
x=np.array([2,6,4,33,3,67,35])
new=np.sort(x)
print("the original array is",x)
print("the sorted ccopy of an array in ascending order is",new)
print("the sorted copy of an array in descending order is",new[::-1])
#use of argsort method
t=np.array([7,2,3,9,6])
sorted=np.argsort(t)
print("the actual array is",t)
print("the index based sorted is ",sorted) 
'''it works like this" it gives their indices but on the bases 
that it give the index of smallest first(2 whose index is 1, then comes 3 whose index is 2,
then 6 whose index 4,then 7 whose index is 0 and in last 9 whose index is 3 now in output it will 
gives indices like this(1,2,4,0,3))'''
#use of third method
t.sort()
print("sorted original array is:",t)
'''sorting on Alphabets'''
n=np.array(["a","z","r","f"])
print("original array is",n)
new=np.sort(n)
print("sorted array of alphabets is",new)
arg=np.argsort(n)
print("sorting array of index of alphabets is",arg)
n.sort()
print(n)