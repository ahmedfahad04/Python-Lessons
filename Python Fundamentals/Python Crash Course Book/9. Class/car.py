"""A class that can be used to represent a car"""
class Car():
    # initializing all variable within this init method
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 125  # as this value if defined here we need not it to be included as parameter

    # describe all methods like this one
    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + " miles on it")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:  # using self is a must
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!!")

    def increment_odometer(self, miles):
        self.odometer_reading += miles



class Battery():
    def __init__(self,battery_size=80):
        self.battery_size = battery_size
    def describe_battery(self):
        print("This car has a " + str(self.battery_size) + "-KWh battery.")
    def get_range(self):
        global range
        if self.battery_size == 80:
            range = 240
        elif self.battery_size == 85:
            range = 375

        message = "this car can go approximately " + str(range) + " miles on a full charge."
        print(message)
    def upgrade_battery(self):
        if self.battery_size != 85:
            self.battery_size = 85



class ElectricCar(Car):
    def __init__(self, make, model, year):
        self.battery_size = 70
        super().__init__(make, model, year) #this super() method does almost the same work as pass
        self.battery = Battery()            #inheritance as attributes
    def describe_battery(self):
        print("This car has a "+ str(self.battery_size)+"-KWh battery.")
    def fill_gas_tank(self): #as 'self' is not present this class will ignore this method if it is called
        print("This car doesn't need a gas tank!")