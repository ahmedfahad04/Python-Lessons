#passing a list in functin argument
def greet_users(names):
    for name in names:
        msg = "hello, "+ name.title()+ "!"
        print(msg)

usernames = ['hannah','tenni','margot']
greet_users(usernames)

# modifying a list in a function

unprinted_designs = ['iphone case','robot pendant','dodecahendron']
completed_models = []

while sorted(unprinted_designs):
    current_design = unprinted_designs.pop()
    print("Printing model: "+ current_design)
    completed_models.append(current_design)

print("\nThe following models have been printed: ")
for completed_model in completed_models:
    print(completed_model)

# now doing the same task using funcion

def print_models(unprinted_designs, completed_models):
    for item in unprinted_designs:
        current_design = unprinted_designs.pop()
        print("Printing model: "+ item)
        completed_models.append(current_design)

def show_completed(completed_models):
    print("\nThe following models have been printed: ")
    for completed_model in completed_models[::-1]: #it mainly sort the list reversely
        print(completed_model)


unprinted_designs = ['iphone case','robot pendant','dodecahendron','motorolla']
completed_models = []

print_models(unprinted_designs[:], completed_models)
show_completed(completed_models)


# preventing a function from modifying a list

