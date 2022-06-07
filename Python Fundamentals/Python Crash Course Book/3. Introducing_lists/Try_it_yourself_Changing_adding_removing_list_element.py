# 3.4 guest list

my_guests = ['Arafath', 'Ziddan', 'Shuvro', 'Bafil', 'Abir']
print("Mr. "+my_guests[0]+" you are invited to join the dinner")
print("Mr. "+my_guests[1]+" you are invited to join the dinner")
print("Mr. "+my_guests[2]+" you are invited to join the dinner")
print("Mr. "+my_guests[3]+" you are invited to join the dinner")
print("Mr. "+my_guests[4]+" you are invited to join the dinner")

print("-------------------------------------------------------------------")
# 3.5 changing guest list

replace1 = my_guests[1]
replace2 = my_guests[3]

my_guests[1] = 'Tamim'
my_guests[3] = 'Aumio'

print(replace1+" and "+replace2+" can't join the dinner.")

print("Mr. "+my_guests[0]+" you are invited to join the dinner")
print("Mr. "+my_guests[1]+" you are invited to join the dinner")
print("Mr. "+my_guests[2]+" you are invited to join the dinner")
print("Mr. "+my_guests[3]+" you are invited to join the dinner")
print("Mr. "+my_guests[4]+" you are invited to join the dinner")

print("-------------------------------------------------------------------")
# 3.6 more guest

my_guests.insert(0, 'Sajjad')
my_guests.insert(3, 'Nirob')
my_guests.append('Sami')
print('Yah! I found a large dinner table. Now I can manage more poeple to join the party.')
print("Mr. "+my_guests[0]+" you are invited to join the dinner")
print("Mr. "+my_guests[1]+" you are invited to join the dinner")
print("Mr. "+my_guests[2]+" you are invited to join the dinner")
print("Mr. "+my_guests[3]+" you are invited to join the dinner")
print("Mr. "+my_guests[4]+" you are invited to join the dinner")
print("Mr. "+my_guests[5]+" you are invited to join the dinner")
print("Mr. "+my_guests[6]+" you are invited to join the dinner")
print("Mr. "+my_guests[7]+" you are invited to join the dinner")


print("-------------------------------------------------------------------")
# 3.7 shrinking guest list

print("Sorry my dear Friends. I cant invite all. I can only afford 2 people")

friend = my_guests.pop()
print("Sorry " + friend + ", I can't invite you !!")
friend = my_guests.pop()
print("Sorry " + friend + ", I can't invite you !!")
friend = my_guests.pop()
print("Sorry " + friend + ", I can't invite you !!")
friend = my_guests.pop()
print("Sorry " + friend + ", I can't invite you !!")
friend = my_guests.pop()
print("Sorry " + friend + ", I can't invite you !!")
friend = my_guests.pop()
print("Sorry " + friend + ", I can't invite you !!")

print("Hello lucky "+my_guests[0]+", you can still join the dinner")
print("Hello lucky "+my_guests[1]+", you can still join the dinner")

del my_guests[1]
del my_guests[0]
print(my_guests)
print("----------------------------------------------------------------")