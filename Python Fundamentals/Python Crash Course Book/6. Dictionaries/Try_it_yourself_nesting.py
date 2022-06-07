#6.7 people

person_1 = {'name':'Kazi Sakib','age':'55','designation':'Professor','city':'Dhaka'}
person_2 = {'name':'Istiaq Ahmed Fahad','age':'20','designation':'Student','city':'Gazipur'}
person_3 = {'name':'Mahbubul Alam Joarder','age':'57','designation':'Assosiate Professor','city':'Chattogram'}

person = [person_1,person_2,person_3]
for item in person:
    for key,val in item.items():
        print(key.title() + " = " + val.title())
    
    print("-------------------------------------")

#6.8 pets

Dulby = {
    'type' : 'cat',
    'owner' : 'Jong hui',
}

Jacky = {
    'type' : 'dog',
    'owner' : 'Rashed',
}

Lalu = {
    'type' : 'cow',
    'owner' : 'Kashem',
}

pets = [Dulby,Jacky,Lalu]

for item in pets:
    print("It is a "+item['type']+". Her owener is " + item['owner'])

    print("----------------------")

print("-----------------------------------------")
#6.9 favorite places

favorite_place = {'Fahad':'Dream_Holiday_Park','Shuvro':'Fantasy_Kingdom','Ziddan':'Shiatkundo'}

for key,val in favorite_place.items():
    print(key + "'s favorite place is "+ val)


print("-----------------------------------------")
#6.10 favorite numbers

li = []
num = {'ziddan':['10','20','30'],'shuvro':['50','32','22'],'bafil':['47','58'],'arafath':['214','1145'],'sharif':['22','147','12566']}

for key,val in num.items():
    print(key+"'s favorite numbers are >> "+ ", ".join(val))


print("-----------------------------------------")
#6.11 cities

cities = {
    'Dhaka':{
        'country':'Bangladesh',
        'population':'1 core',
        'fact':'Most poluted city',
    },
    'Sydney':{
        'country':'Australia',
        'population':'0.5 Core',
        'fact':'Neat and Clean',
    },
    'Tokey0':{
        'country':'Japan',
        'population':'2 core',
        'fact':'Technologically too advanced',
    },
}

for city,details in cities.items():
    print("\nCity is: "+city)
    print("Details of these cities are given below: ")
    print("Country: "+details['country'])
    print("Total popuolation: "+details['population'])
    print("Interesting Fact: "+details['fact'])
    print("---------------------------------------------")

    
#6.12 Extensions

num = {'ziddan':['10','20','30'],'shuvro':['50','32','22'],'bafil':['47','58'],'arafath':['214','1145'],'sharif':['22','147','12566']}
num['Tamim'] = ['5','265']
print(num['Tamim'])

# I skip this portion.It means you just need to customized 
# dictionary by adding,removing,fomatting the output and many more just
# to discover the acitivity of Dictionary.