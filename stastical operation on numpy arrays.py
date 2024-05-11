'''Statical operations on 1d array
1.max()
2.min()
3.sum()
4.mean()
5.median()
6.prod()
7.var()
8.std()'''
import numpy as np
x=np.array([1,4,33,45,2,99,34])
print("the maximum entry in array is",np.max(x))
y=np.min([23,45,3,2,34,56])
print("the minimum digit is",y)
print("the sum is",np.sum(x))
print("the mean or average is",np.mean(x))
print("the median is",np.median(x))   #in  median it sorts the array first and then will give mid value
                            #if number of elements in array is odd, if it is even then it will give
                             #arithmetic mean of two mid values
print("the product of all elements is",np.prod(x))
#variance={mean-(first element)}**2+{mean-(2nd element)}**2 till nth element/number of elements
print("the varyness is",np.var(x))
print("the standard deviation is",np.std(x)   #standard deviation(sd) is the square root of variation obtained