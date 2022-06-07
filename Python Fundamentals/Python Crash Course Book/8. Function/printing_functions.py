def greet_users(names):
    for name in names:
        msg = "hello, "+ name.title()+ "!"
        print(msg)

def print_models(unprinted_designs, completed_models):
    for item in unprinted_designs:
        print("Printing model: "+ item)
        completed_models.append(item)

def show_completed(completed_models):
    print("\nThe following models have been printed: ")
    for completed_model in completed_models: 
        print(completed_model)

