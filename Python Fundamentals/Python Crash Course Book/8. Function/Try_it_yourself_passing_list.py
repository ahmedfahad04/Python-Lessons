#8.9 magicians

def show_magician(names):
    for magician in names:
        print(magician.title())

magicians = ['juel','aich','sohel','rana']
show_magician(magicians)

print("--------------------------")
#8.10 great magicians

def make_great(magics):
    temp_great = []

    #print(magics)
    while magics:
        hold = magics.pop()
        x = "Great " + hold.title()
        temp_great.append(x)
    ##print(temp_great)

    for item in temp_great:
        magics.append(item)

    #return magics

magicians = ['juel','aich','sohel','rana']
make_great(magicians)
show_magician(magicians)
    
print("-----------------------------------------")
#8.11 unchagned magician

def make_great_2(magics):
    temp_great = []

    #print(magics)
    while magics:
        hold = magics.pop()
        x = "Great " + hold.title()
        temp_great.append(x)
    #print(temp_great)
    return temp_great

magicians = ['juel','aich','sohel','rana']
print("\nOriginal List is: ")
show_magician(magicians)

print("\nModified List is: ")
print("\n".join(make_great_2(magicians)))