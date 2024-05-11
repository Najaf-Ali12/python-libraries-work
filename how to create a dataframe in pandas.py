import pandas as pd
#method1:making a data frame manually, not a commonly used method
data=[(1,"najafa ali",18,"male","dadu"),
      (2,"mushtaque",15,"male","hyderabad"),
      (3,"hira mani",30,"female","karachi")]
dataframe=pd.DataFrame(data,columns=["roll_no","name","age","gender","city"])    #d and f of dataframe will always be capital
print(dataframe)
#second method is
pakistan=pd.read_csv("E:/one drive/OneDrive/Desktop/first csv file.csv")   
print(pakistan) 
#operations using inbuilt functions
'''1:df.head(), will execute top five rows by default 
if give number in bracket will print top numbers rows
2:df.tail(), will execute last five rows by default if number 
given then will print those last rows
3:df.shape, will print number of rows,number of columns
4:df.columns, will give the name of columns
5:df.age or df[["age","name"]], this will print the data of particular column age
6:df.size, will give total number of elements
7:df.dtypes, will tell the data type of each column
8:df.values, will give the data in list form
9:df.index, will give the start,stop and step values'''
#use / instead of \ in directory and in last write the name of 
#file.csv if one/ gives error give // double
#indexing of rows and columns start from zero