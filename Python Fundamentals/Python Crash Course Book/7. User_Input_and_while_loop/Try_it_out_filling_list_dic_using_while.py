#7.8 deli 

sandwitch = ['tomato','chiken','beef','mutton','pastrame','pastrame','pastrame']
finished = []

while sandwitch:
    finished = sandwitch.pop()
    print("I made "+ finished.title() + " sandwitch for you.")

print("----------------------------------------")
#7.9 no pastram

sandwitch = ['tomato','chiken','beef','mutton','pastrame','pastrame','pastrame']
print("Deli has ran out of pastrami.")

while 'pastrame' in sandwitch:
    sandwitch.remove('pastrame')

print(sandwitch)


print("----------------------------------------")
#7.10 Dream Vacation

promt = "if you could visit one palce in the world where would you go?"

user = input(promt)
print("I would like to go "+user)



