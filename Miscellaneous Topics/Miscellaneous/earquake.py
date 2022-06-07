from datetime import date

earthquake = []
aftershock = []
all_date_objects = []

n = int(input("Enter number of events you want to test: "))

# taking and storing dates
for i in range(n):
    print("Evnet ", i+1, "--")
    year = int(input("Year: "))
    month = int(input("Month: "))
    day = int(input("Date: "))

    dateObj = date(year, month, day)
    if i == 0:
        earthquake.append(dateObj)
    all_date_objects.append(dateObj) # stroe all date objects

print(all_date_objects)

# sort out the main earthquake and aftershocks
for i in range(0,len(all_date_objects)):
    if all_date_objects[i] in aftershock:
        continue
    else:
        for j in range(i+1, len(all_date_objects)):

            date1 = all_date_objects[i].day
            date2 = all_date_objects[j].day
            diff = date2 - date1

            if diff <= 5:
                print(date2, ", Its an AfterShock")    
                aftershock.append(all_date_objects[j])
            else:
                print(date2, ", Its an Earthquake")    
                earthquake.append(all_date_objects[j])
                break

print("Earthquake: ", earthquake)
print("AfterShock: ", aftershock)






