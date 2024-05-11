import numpy as np
x=np.array([[12,11,15],
            [21,20,25],
            [16,18,27]])
y=np.sort(x)    #for row wise can also write y=np.sort(x.axis=1)      #will sort row wise by default
z=np.sort(x,axis=0)    #now will sort column wise
print("row wise sorted is\n",y)
print(f"the column wise sorted is\n:{z}")  
t=np.argsort(x,axis=1) #see file sorting in numpy arrays for argsort
p=np.argsort(x,axis=0)
print("the row wise sorting is\n",t)
print("the column wise sorting is\n",p)
x.sort()
print("in place sorting is\n",x)
