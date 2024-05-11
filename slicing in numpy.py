#SLICING IN NUMPY
#SLICING:slicing is a way to extract a subset data from a numpy array
#print(arrayname[start:stop:step]) if you donot give step it is 1 by default
#slicing for 1d array
import numpy as np
newarray=np.array([10,20,30,40,50,60,70,80])
print(newarray[1:4])
print(newarray[1:7:2])
print(newarray[-1:-7:-1])
print(newarray[-1:-8:-2])
print(newarray[::2])       #it measns start and end are by default(0 to last) step is given 
print(newarray[::-1])   #end and start by default but will print in reverse
#Slicing for 2d array
#print(arrayname[rstart:rend,cstart:cend])  rend=row end ,cstart=column start
#for understanding the structure of 2d array see file "indexing in numpy"
anotherarray=np.array([[15,16,17],[25,26,27],[35,36,37],[45,46,47]])
print(anotherarray[1,:])
print(anotherarray[:,1])
print(anotherarray[2:4,1])
print(anotherarray[1,0:2])
print(anotherarray[2:4,1:3])   #compare line 21 and line 22
print(anotherarray[2:4,1:3])
print(anotherarray[:,1:6])   #if we give rend,cend a value that not exist it will not give error but will consider the last rend,cend
print(anotherarray[1:9,:])    #see line 23 and line 24
print(anotherarray[1:3,:1])
print(anotherarray[1:3,1])
print(anotherarray[:,:])    #will print whole array
'''it will be saved like be low
15  16 17
25  26 27
35  36 37
45  46 47
it has four rows(0-3) and 3 columns(0-2)'''