animals = list()

for i in range(5):
    animal = input("Please enter an animal name for animal " + str(i + 1) + ": ")
    animals.append(animal)

print("These are the animals that were entered in the list")

for i in range(5):
    print(animals[i])
