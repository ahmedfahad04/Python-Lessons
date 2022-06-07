from car import * # it will import everything included the car.py module
# import car # if I use only this line then I will need to modify Car('audi','b54',2017) to car.Car....
# from car import Car
# from car import ElectricCar #it is same as "from car import Car,ElectricCar"
# from car import Car, ElectricCar

my_new_car = Car('audi','b54',2017)
print(my_new_car.get_descriptive_name())

my_new_car.odometer_reading = 255
my_new_car.read_odometer()

my_tesla = ElectricCar('tesla','Xtream',2002)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
my_tesla.battery.upgrade_battery()
my_tesla.battery.get_range()
my_tesla.odometer_reading = 1020
my_tesla.read_odometer()

