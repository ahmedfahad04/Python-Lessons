# POSITIONAL ARGUMENTS

def describe_pet(animal_type, pet_name='willie'):
    print("\nI have a "+ animal_type+".")
    print("My "+ animal_type+"'s name is "+ pet_name.title()+".")

describe_pet('hamster','harry') #its cares about orders
describe_pet('dog','willie')

# KEYWORD ARGUMENT

describe_pet(animal_type='cat',pet_name='jony') #its dont care about order of arguments
describe_pet('rhino')
describe_pet(animal_type='tiger')


