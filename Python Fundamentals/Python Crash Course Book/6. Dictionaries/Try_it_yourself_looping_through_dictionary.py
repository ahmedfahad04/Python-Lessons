#6.4 glossary 2

person = {'name':'Hazrat_Mohammad(PBUH)','Height':'medium','designation':'Prophet','city':'Mecca',63:'age'}

# 63:age this term added
for keys,values in person.items():
    print(str(keys).title() + " = " + values)

print("-------------------------------------------")
#6.5 rives

rivers = {'nile':'egypt','mississippi':'america','volga':'russia'}

for river,country in rivers.items():
    print("The "+ river.title() + " runs through " + country.title() )


print("---------------------------------------------")
# 6.6 polling

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

users = ['fahad','sarah','shuro','ziddan','jen','phill']

for man in users:
    if man in favorite_languages.keys():
        print("Thanks " + man.title() + " for responding.")
    else:
        print(man.title() + ", you are cordially invited to take the poll.")

print("---------------------------------------------")