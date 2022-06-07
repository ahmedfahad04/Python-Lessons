import pandas as pd

data = pd.read_csv("CSV_Files/data.csv", index_col=0)
print(data)

# summary function

print("\n##Summary of Age Column: \n") #numeric data
sm = data.Age.describe(); print(sm)
print("Mean Age: ", data.Age.mean())

print("\n##Summary of Date of Birth Column: \n") #string data
sm = data.Date.describe(); print(sm)
print("\n##Unique Values:\n", data.Date.unique())
print("\n##Frequencies:\n",data.Country.value_counts())


# maps

data_age_mean = data.Age.mean()
k2 = data.Age - data_age_mean # option 1
k = data.Age.map(lambda p: p - data_age_mean) # option 2
k3 = data.Country + " - " + str(data.Age)
print("\n##Age Differences: \n",k2)
print(data.Country + " - " + data.iloc[:, 1])

print('Name having the Max Age')
age_max_id = data.Age.idxmax() # fetching specific info using max/min age index
name = data.loc[age_max_id, ["First Name", "Date"]]
print(name)

uk = data.Country.map(lambda p: 'United States' in p).sum() # counting frequencis using map
print("United States",uk)
fr = data.Country.map(lambda p: 'France' in p).sum()
print("France: ", fr)


def nature(row):
    if row.Country == 'France':
        return "Traitor"
    elif row.Country == 'United States':
        return "Business"
    else:
        return "Neutral"

k2 = data.apply(nature, axis='columns') # using apply module we can set condition to row wise data
print(k2)
