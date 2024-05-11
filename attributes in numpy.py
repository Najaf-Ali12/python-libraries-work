'''attributes in numpy
1.ndim :will tell the dimension of the array
2.shape: it will tell the shape or order of the array
3.size: will tell the number of elements in array
4.dtype: will tell the datatype of elements of an array
in array str>complex>float>int ,it means that if all four given in array then its dtype will be in that strength
5.itemsize    :will tell that how bytes memory each element occupy
1byte=8bits
memory of integer data type is 4
that of float is 8 no problem if int type is also in array
that of complex is 16 bytes no problems if a float or int is also in array
that of string is 4bytes if there is onlyone character in apostrophes if there are n characters the size will be n*4'''
import numpy as ab
list1=[[1,"ab",86],[8,89.0,8]]
newarray=ab.array(list1)
dimension=newarray.ndim
print("the array is of",dimension, "dimensions")
size=newarray.size
print("the size of the array is",size)
shape=newarray.shape
print("the shape of the array is",shape)
type=newarray.dtype
print(type)   
itemsize=newarray.itemsize
print(itemsize)