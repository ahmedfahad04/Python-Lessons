# returning a simple value
def get_formatted_name(first_name, last_name):
    full_name = first_name + " " + last_name
    return full_name.title()


musician = get_formatted_name('jimi', 'hendrix')
print(musician)

# making a argument option


def get_formatted_name2(first_name, middle_name, last_name):
    if middle_name:
        full_name = first_name + " " + middle_name + " " + last_name
    else:
        full_name = first_name + ' ' + last_name

    return full_name.title()


print(get_formatted_name2('istiaq', 'ahmed', 'fahad'))
print(get_formatted_name2('istiaq', '', 'fahad'))

# returning a dictionary


def build_person(first_name, last_name, age=''):
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age

    return person

print(build_person('jimi','hendrix',))

#using a function with a while loop

while True:
    print("\nPlease tell me our name: \n(Please enter 'q' to quit the progarm")

    f_name = input("First name: ")
    if f_name == 'q':
        break
    l_name = input("Last name: ")
    if l_name == 'q':
        break

    formatted_name = get_formatted_name(f_name,l_name)
    print("\nHello, " + formatted_name + "!")






