#5.1 conditional test

cars = ['Audi', 'bmw', 'subaru', 'toyota']
cube = [1, 8, 27, 64, 125]


car = 'Subaru'
print(car == cars[2])
print(car.lower() == cars[2])
# more test we have done in Conditional tet python file

print("--------------------------------------------")
#5.2 more conditional tests
print(car == cars[2])
print(car.lower() == cars[2])
print(cube[1]>cube[2])
print(cube[0]<cube[3])
print((cube[0]<cube[1]) and (cube[2]<cube[3]))
print((cube[0]<cube[1]) or (cube[2]>cube[3]))
print("5" in cube)
print(8 in cube)
print("bmw" not in cars)




