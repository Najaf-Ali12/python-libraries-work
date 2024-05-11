import pandas as pd
data=pd.read_csv("E:/one drive/OneDrive/Documents/csv file for practice.csv")
#selecting a particular column or columns
#print(variablename[["column1 head","column2 head",....]])
print(data[["percentage","name"]])
#selecting a particular row using index labels
#print(variablename.loc[index of row])
print(data.loc[4])
#select a single row by integer index
#print(variablename.iloc[index of row]
print(data.iloc[4])
#select multiple rows by index labels
#print(variablename.loc[[index of row1st,index of row2nd.....]]) or by integer index
#print(variablename.iloc[[index of row1st,index of row2nd.....]])
print(data.iloc[[0,2,4]])
#filtering rows
print(data["percentage"]>95)
#adding a new column in last
data["phone_numbers"]=[12,19,13,14,15,16,18]  #will add to all but not same
data["phone numbers"]=3121348757   #will add this number to all
print(data)
#adding a new column at desired position
data.insert(0,"caste","Alkhani")
print(data)
#deleting a column from a dataframe
dropped=data.drop(columns="phone_numbers")    #we will assign the new frame to a variable and will print that variable
print(dropped)
#or deleting a column using del method
del data["phone numbers"]      #here we will create a new variable but will print the original variable in which our dataframe was stored
print(data)
#changing the name of the existing column
print(data.rename(columns={"marks":"marks obtained"}))
#deleting a particular row from a dataframe
print(data.drop([0]))   #sentax is datafram variable name.drop([row number])
#adding a new row at desired position
data.loc[0]=[2,"aftab",999,99,133,3121348757]
print(data)                                     #will automatically replace the already existing row at desired position with new row
   #its syntax is variable.loc[position of new row]=[all items]  note the length of items of new row should be same with the already existing rows.
#updating the existing value at desired location
data.loc[0,"name"]="altaf"    #its synatx is df container.loc[index,"column name"]="new value"
print(data)    
#updating the multiple values
data.loc[[1,2],"name"]=["murtaza","ashraf"]
print(data)
file=pd.read_csv("E:/one drive/OneDrive/Desktop/first csv file.csv")
print(file.rename(columns={"najaf ali":"name","1":"rollno","18":"age","dadu":"city","3.96":"GPA"}))
#note if already existing column is an integer, then to rename that column we have to write it in string


