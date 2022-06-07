#8.12 sandwiches

def sandwich_maker(*items):
    print("\nElements used in this sandwitch: ")
    for item in items:
        print("- "+str(item).title())


sandwich_maker('cucumber','mayonese','bread','white_sauce')
sandwich_maker('red sauce','soya sauce','cheese','letus')
sandwich_maker('chicken','egg','carrot','extra_cheese')

print("----------------------")
#8.13 use porfile

def build_profile(first,last,**user_info):
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key,value in user_info.items():
        profile[key] = value

    return profile

user_profile = build_profile(
    'Istaiq Ahmed', 'Fahad',
    location = 'Dhaka_Bangladesh',
    field = "Computer_Science",
    occupation = 'Student'
)

for key,value in user_profile.items():
    print(str(key).title()+ " -> " + value)


print("----------------------------------------------")
#8.14 cars

def make_car(manufacturer, model_no, **arbitrary_info):
    car_details = {}
    car_details['manufacter'] = manufacturer
    car_details['model'] = model_no
    for key, value in arbitrary_info.items():
        car_details[key] = value
    
    return car_details

car = make_car('subaru', 'outback', color='blue', tow_package="True")
for key,value in car.items():
    print(str(key).title()+ " -> " + str(value).title())

car = make_car('honda', 'accord', year=1991, color='white',
        headlights='popup')

print("\n")
for key,value in car.items():
    print(str(key).title()+ " -> " + str(value).title())

print("----------------------------------------------")