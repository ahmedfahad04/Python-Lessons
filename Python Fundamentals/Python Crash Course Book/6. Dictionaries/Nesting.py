# a list of dictionary
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

alien = [alien_0, alien_1, alien_2]

print("All alien dictionary is in a list.")
for alie in alien:
    print(alie)

new_aliens = []

# Make 10 green aliens
for num in range(10):
    na = {'color': 'green', 'points': 5, 'speed': 'slow'}
    new_aliens.append(na)

for num in range(5):
    na = {'color': 'yellow', 'points': 3, 'speed': 'medium'}
    new_aliens.append(na)

print("First 3 alien dict.")
# show the first 3 aliens
for alie in new_aliens[:3]:
    print(alie)

print("...")

print("Total " + str(len(new_aliens)) + " green aliens have been created.")

# changing value of dictionary values
for values in new_aliens[:]:
    if values['color'] == 'green':
        values['color'] = 'brown'
        values['speed'] = 'medium'
        values['points'] = 25
    elif values['color'] == 'yellow':
        values['color'] = 'red'
        values['speed'] = 'fast'
        values['points'] = 50

for value in new_aliens:
    print(value)


# a list in a dictionary

# Store information about a pizza being ordered.
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
}

# summarize the order
print("You ordered a " + pizza['crust'] +
      "-crust pizza with the following toppings:")

for top in pizza['toppings']:
    print("\t" + top)


# a dictionary in a dictionary

users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
    },
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
    },
}

for username, user_info in users.items():
    print("\nUsername: "+ username)
    full_name = user_info['first'] + " " + user_info['last']
    location = user_info['location']

    print("\tFull name: "+ full_name.title())
    print("\tLocation: "+ location.title())


