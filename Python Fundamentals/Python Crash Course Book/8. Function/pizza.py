def make_pizza(size, *toppings):
#Summarize the pizza we are about to make."""
    print("\nMaking a " + str(size) +
      "-inch pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)


def build_profile(first,last,**user_info):
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key,value in user_info.items():
        profile[key] = value

    return profile


def make_pizza_2(size,*toppings):
    print("\nMaking a "+ str(size) + "-inch pizza eith the following toppings: ")
    for topping in toppings: 
        print("- "+ topping)