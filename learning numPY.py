#how to create numpy array:
import  numpy as np #we write np so we donot have to write numpy again and again,not necessary to write np can write any letter
list1=[1,2,3,4,5]
list2=[67,3,89.9]   #as array has homogenous data type, if we give different data types in list then it will change them in one datatype
array=np.array(list2)
new_array=np.array(list1,dtype="U16")   #here we can mention the datatype of array elements in which we want them 
print(new_array)                         #U32 or U16 is used for character data type for other types like int,float etc
print(array)
print(type(new_array))
list3=[[7,5,4],["z","v","b"],[8.8,7.9,6.5]]
print(np.array(list3))
#using range function to create arrray
print(np.arange(1,9))
otherarray=np.arange(1,7).reshape(2,3)   #reshape shows that the array will have 2 rows,3 coulums total 6 elements so we passed 6 elements in arange.
print(otherarray)
#to make null array containing only zeros
null=np.zeros(4)                         #will create one dimensional array of zeros
print(null)
nullarray=np.zeros((3,4))              #will create two dimensional array of zeros containg 3 rows and 4 columns total 12 elements
print(nullarray)  
single=np.ones((1,2))               #will create one two dimensional array of ones
print(single)        