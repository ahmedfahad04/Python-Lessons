import pandas as pd

file = open("UI File\Stat Attendance.txt")
new_data = ''
for row in file.readlines():
    for item in row:
        if item == ' ':
            new_data += ", "
        else:
            new_data += item

print(new_data)