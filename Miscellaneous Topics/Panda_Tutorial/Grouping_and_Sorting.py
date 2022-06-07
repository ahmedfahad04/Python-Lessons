import pandas as pd

file = pd.read_csv("CSV_Files/data.csv", index_col=0)

data = file.groupby('Age').idxmin()
print(data)

# print("\n##Data with their Frequencies: \n")
# x = file.groupby('Age').Age.count()# creates a series of the frequency of Age col
# #or x = file.groupby('Age').size()
# print(x)
#
# print("\n##Frequency of Minimum Age in basis of Gender_1: \n")
# x = file.groupby('Gender').Age.min()
# print(x)
#
# print("\n##Frequency of Maximum Age in basis of Country: \n")
# x = file.groupby('Country').Age.max()
# print(x)
#
# print("\n##Country wise Id division: \n")
# x = file.groupby('Country').apply(lambda p: p.Id)
# y = file.groupby('Country').apply(lambda p: p.Id.iloc[0])
# print(y)
# print(x)
#
# x = file.groupby(['Country', 'Date']).apply(lambda p: p.loc[p.Age.idxmin()]) #confused
# print(x)
#
# print("\n##Stats about Age of Different Countries\n")
# x = file.groupby('Country').Age.agg([len,min,max,]) #show little stats about the Age of Different countries
# print(x)
#
# print("\n##Stats about Age of Different Countries & Gender \n")
# k = file.groupby(['Country','Gender']).Age.agg([len]) #show little stats about the Age of Different countries
# print(k)
#
# print("\n##Sorted Data: ")
# country_data = file.groupby('First_Name').First_Name.agg([len])
# #country_data = country_data.sort_values(by='len',ascending=False) #confused
# #country_data = country_data.sort_index()
# _data = country_data.sort_values(by=['First_Name', 'len'])
# print(_data)
#
#
#







