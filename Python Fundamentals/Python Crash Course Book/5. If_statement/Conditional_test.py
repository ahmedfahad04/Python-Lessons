# simple exaple
cars = ['Audi', 'bmw', 'subaru', 'toyota']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

car = 'AUDI'
print("Result: ",car.lower() == cars[0])
print("Result: ",car.title() == cars[0])
print("Audi" in cars)
print("BMW" in cars)
print(("BMW" == cars[1])or("Audi") == cars[0])
print(("BMW" == cars[1])and("Audi") == cars[0])

if ("BMW" == cars[1])or("Audi" == cars[0]):
    print("Its a true Statement")
else:
    print("Its False")

if "Bmw" not in cars:
    print("Corolla is missing from the list")
else:
    print("It is in the list")