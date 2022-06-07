class Car:
    #initializing all variable within this init method
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 125 # as this value if defined here we need not it to be included as parameter

    #describe all methods like this one
    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' '+ self.model
        return long_name.title()

    def read_odometer(self):
        print("This car has "+ str(self.odometer_reading)+ " miles on it")
    
    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:# using self is a must
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!!")

    def increment_odometer(self,miles):
        self.odometer_reading += miles

class Battery:
    def __init__(self,battery_size=80):
        self.battery_size = battery_size
    def describe_battery(self):
        print("This car has a " + str(self.battery_size) + "-KWh battery.")
    def get_range(self):
        global range # adding a globl statement
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 80:
            range = 270

        message = "this car can go approximately " + str(range) 
        message += " miles on a full charge."
        print(message)



class NewElectricCar(Car):             #child class of Car
    pass                               # using pass all the attrib of Car will pass through this subclass


class ElectricCar(Car):
    def __init__(self, make, model, year):
        self.battery_size = 70 
        super().__init__(make, model, year) #this super() method does almost the same work as pass
        self.battery = Battery()            #inheritance as attributes
    def describe_battery(self):
        print("This car has a "+ str(self.battery_size)+"-KWh battery.")
    def fill_gas_tank(self): #as 'self' is not present this class will ignore this method if it is called
        print("This car doesn't need a gas tank!")


my_corolla = NewElectricCar("CorollaX", "RTx250", "2002")
print(my_corolla.get_descriptive_name())

my_tesla = ElectricCar("Tesla","M310","2015")
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()
my_tesla.fill_gas_tank()
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()


