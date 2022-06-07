#using arbitrary arguments
def make_pizza(*toppings):
    print("\nMaking a pizza with the following toppings")
    for topping in toppings: 
        print("- "+topping)


make_pizza("pepperoni")
make_pizza('mushroooms','green pepper','extra cheese')

#mixing positional and arbitrary arguments
def make_pizza_2(size,*toppings):
    print("\nMaking a "+ str(size) + "-inch pizza eith the following toppings: ")
    for topping in toppings: 
        print("- "+ topping)

make_pizza_2(12," pepperoni")
make_pizza_2(16,'mushroooms','green pepper','extra cheese')

# using arbitrary keyword arguments

def build_profile(first,last,**user_info):
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key,value in user_info.items():
        profile[key] = value

    return profile

user_profile = build_profile(
    'albert', 'einstein',
    location = 'prinstone',
    field = 'physics',
    occupation = 'scientist'
)

print(user_profile)
