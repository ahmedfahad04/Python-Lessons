import pandas as pd

#Remeber:
# 1. There are two core objects in pandas: the DataFrame and the Series.

#DataFrame
print("DataFrame:-")
data = pd.DataFrame({'Name': ['Istiaq','Ahmed','Fahad'],
                     'Type':['First_Name','Middle_Name','Last_Name']},
                      index=['One','Two','Three'])
print(data)

#Series
print("Series:-")
data2 = pd.Series(['Istiaq','Ahmed_Fahad','1204'], index=['First_Name',"Last_Name","Roll"], name="Introduction")
print(data2)

# 2. Reading Data Files

print("Read_Data:-")
info = pd.read_csv(r"F:\FAHADS FILES\Python\NewExperiments\Panda_Tutorial\CSV_Files\anova.csv")
#info = pd.read_csv("anova.csv", index_col=0) #index_col makes the pointed col as index col
print("Size: " , info.shape)
print("Data: \n", info.head())

# 3. Saving a CSV File
data.to_csv("First_csv_file.csv")