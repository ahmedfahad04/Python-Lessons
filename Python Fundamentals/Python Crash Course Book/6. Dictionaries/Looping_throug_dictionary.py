num = {'ziddan': '10', 'shuvro': '333',
       'bafil': '7', 'arafath': '11', 'sharif': '20'}

# loop using only keys
for item in num.keys():
    print(item.title())

# loop using only values
for item in num.values():
    print(item)

# loop using both keys and values
for key, value in num.items():
    print("\nKeys: "+key.title()+"("+value+")")

# looping through a dictionary's key in order
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}
for name in sorted(favorite_languages.keys()):
    print(name.title() + ", thank you for taking the poll.")

new_dict = favorite_languages # copy a dictionay in new dictionary
print(sorted(new_dict))

# use set to include only the distinct elements
for item in set(favorite_languages.values()):
    print(item.title()+ ", thank you for taking the poll." )

