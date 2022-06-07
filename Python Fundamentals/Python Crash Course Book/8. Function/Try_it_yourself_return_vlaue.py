#8.6 city names

def city_country(name,country):
    sentence = '"'+name.title() + ", " +country.title()+'"'

    return sentence

print(city_country("Dhaka","Bangladesh"))
print(city_country("Sydney","australia"))
print(city_country("toronto","Canada"))

print("--------------------------------------------")
#8.7 album

def make_album(artist, title, track):
    if track:
        music = {'artist':artist, 'title':title, 'track':track}
    else:
        music = {'artist':artist, 'title':title}
    return music

print(make_album("Atif Aslam","Kese bata un....",""))
print(make_album("Asif","Bangladesh egiye jao..",""))
print(make_album("Aiub Baccu","Bondhu asche bohu din pore",'25'))

print("-----------------------------------------------")
#8.8 user albums

while True:
    print("Enter 'q' to quit the loop.")
    artist = input("Enter artist name: ")
    
    if artist == 'q':
        break

    title = input("Enter song title: ")

    if title == 'q':
        break


    print(make_album(artist,title,''))