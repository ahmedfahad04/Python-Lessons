import pandas as pd

info = pd.read_csv(r"F:\FAHADS FILES\Python\NewExperiments\Panda_Tutorial\CSV_Files\anova.csv")
print(">>Full Data SET: ")
print(info)

# 1. selecting
print(">> SELECTION OPERATIONS: ")
print(info.M2) # here M2 is our col name
re = info['M2'] # same as 5th line just a different approach
print(re[1]) # access any row value using [] indexing

# 2. indexing(iloc)
print(">> INDEXING OPERATIONS")
print(">> Printing 4th Row:\n", info.iloc[3]) # printing a perticular row
print(">> Printing 2nd col:\n",info.iloc[:, 1]) # printing a perticular colomn(same as re[1] in 11th line)
print(">> Printing 3rd col:\n",info.M3) # printing a perticular colomn(same as re[2] in 11th line)
print(">> Printing first 3 row of col 1:\n",info.iloc[:3, 0])
print(">> Printing 2,3,4 th data of col 2:\n",info.iloc[1:4,1])
print(info.iloc[:2,:3])

#[ : ,  : ] space between first colon means range of rows
# ans space between second colon means range of columns
# you can also define a list of row number in between spaces of colon

print(">> Exact row location using list:\n",info.iloc[[1,2,4], 0])
print(">> BackTravesal:\n", info.iloc[-3:,])

# 3. label-based selection(loc)

print(">> First Entry of col 'M1' :\n", info.loc[3, "M1"]) # here loc[a,b]; a means row num/position and b means col name
print(">> Extract data using col name:\n", info.loc[:, ['M2','M3']])
print("random: \n", info.iloc[1,1])

# 4. conditional selection

con = pd.read_csv(r'F:\FAHADS FILES\Python\NewExperiments\Panda_Tutorial\CSV_Files\data.csv', index_col=0)
x = con.loc[(con.Gender == 'Male') & (con.Salary > 300)]
y = con.loc[con.Country.isin(['France', 'United States'])]
print(x)
print(y)

# 5. assigning data

con['France'] = "Bangladesh"
print("CHANGED: ")
print(con)
