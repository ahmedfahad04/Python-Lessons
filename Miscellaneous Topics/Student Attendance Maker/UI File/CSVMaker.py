import csv

filename = input("Enter the file name: ") 
f = open(filename)
file = f.readlines()

f.close()

std_details =  dict()

cnt = 0
names = []
roll = []
attendance = []

for item in file:

    data = item.split("_")
    cnt += 1
    if cnt == 34:
        break
    names.append(data[0])
    roll.append(data[1][:4])
    attendance.append(data[1][5:-1])

std_details["name"] = names
std_details["roll"] = roll
std_details["attendance"] = attendance
print("Data Fetching Done!!")


headings = ["Name","Roll","Attendance","Percentage"]
info = []

CSVfilename = input("Enter output file name(in csv formate): ")
with open(CSVfilename,"w") as f:
    writer = csv.writer(f)

    writer.writerow(headings)
    for i in range(0,33,1):
        info.append(std_details["name"][i])
        info.append(std_details["roll"][i])
        info.append(std_details["attendance"][i])
        info.append(str(int(std_details["attendance"][i])*10)+"%")
        writer.writerow(info)
        
        info.clear()

print("CSV file created Successfully!!")
f.close()