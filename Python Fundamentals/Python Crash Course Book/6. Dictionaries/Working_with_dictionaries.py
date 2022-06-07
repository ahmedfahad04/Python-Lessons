#a simple dictionary

alien = {'color':'green','points':5}
print(alien['color'])
print(alien['points'])

print("You just earned: "+str(alien['points'])+" points")
new_point = alien['points']+5
print("After this attack your new point is: "+str(new_point))

# adding new key value pair

print("Before adding new values dictionary is: ")
print(alien)

alien['x position'] = 0
alien['y position'] = 25

print("After adding new values new dictionary is: ")
print(alien)

# starting with empty dictionary

new_alien={}

new_alien['color'] = 'red'
new_alien['points'] = 10

print(new_alien)

# modifying vlaue in a dictionary

new_point = alien['points']+5
print("After this attack your new point is: "+str(new_point))

pos = {'x':0, 'y':25,'speed':'fast'}
print("Original x-position: "+ str(pos['x']))

if pos['speed'] == 'slow':
    x_in = 1
elif pos['speed'] == 'medium':
    x_in = 2
else:
    x_in = 3

pos['x'] = pos['x']+x_in

print("New x_position: "+str(pos['x']))

# removin key value pair

print("Befor deleting element dictionary is: ")
print(new_alien)

del new_alien['points']
print("After deletion new dictioary is: ")
print(new_alien)

# a dictionary of similar objects

favorite_language = {
    'jen' : 'python',
    'sarah' : 'C',
    'edward' : 'ruby',
    'phill' : 'python',
}

print("Jen favorite language is: "+str(favorite_language['jen']))

