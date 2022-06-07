unconfirmed_users = ['alice', 'bob', 'hogwarts', 'harry']
unconfirmed_users.sort(reverse=True)
confirmed_users = []

while unconfirmed_users:
    current_users = unconfirmed_users.pop()
    print("Verifying user: "+current_users.title())
    confirmed_users.append(current_users)

for usr in confirmed_users:
    print(usr.title())

# Removing All Instances of Specific Values from a List
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)
while 'cat' in pets:
    pets.remove('cat')
print(pets)

# filling a dictionary with user input

responses = {}
# Set a flag to indicate that polling is active.
polling_active = True
while polling_active:
    # Prompt for the person's name and response.
    name = input("\nWhat is your name? ")
    response = input("Which mountain would you like to climb someday? ")
# Store the response in the dictionary:
    responses[name] = response
# Find out if anyone else is going to take the poll.
    repeat = input("Would you like to let another person respond? (yes/ no) ")
    if repeat == 'no':
        polling_active = False
# Polling is complete. Show the results.
print("\n--- Poll Results ---")

for name, response in responses.items():
    print(name + " would like to climb " + response + ".")
