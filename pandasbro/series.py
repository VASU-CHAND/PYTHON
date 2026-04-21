# pandas is a library built on top o numpy we work on object known 
# as series and dataframe 
#its like excel on python with steroids
import pandas as pd

print(pd.__version__)
# series is a one dimensional array
# with index and value think like single 
# coloumn in spreadsheet
data =[1,2,3,4,5]
series = pd.Series(data , index=['a','b','c','d','e'])
print(series)
print(series.loc['a'])
print(series['a'])
print(series.iloc[2]) # iloc -- interger location
print(series[series > 3]) # printing values greater than 3
