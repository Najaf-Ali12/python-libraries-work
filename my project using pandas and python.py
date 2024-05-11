import datetime
import pandas as pd

# Create an empty list to hold data
data = []

while True:
    num1 =float(input("Enter num1: "))
    num2 =float(input("Enter num2: "))
    result = num1 + num2
    
    # Append the new data to the list
    data.append([num1, num2, result])
    
    ask = input("Do you want to add more numbers (yes/no): ")
    if ask.lower() != 'yes':
        break

# Create a DataFrame from the list of data
df = pd.DataFrame(data, columns=["num1", "num2", "result"])

print(df)


date=datetime.datetime.now().date().strftime("%d-%m-%y")
time=datetime.datetime.now().time()
print(date,end="      ")
print(time)
