#9.6 ice cream stand

class Restaurant():
    def __init__(self,restaurant_name, cuisine_type):# all atributes will be gathered here
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):  #declearing self is a must
        print("Name is: "+ self.restaurant_name +" And its cuisine is: "+ self.cuisine_type)
    def open_resaturant(self):
        print(self.restaurant_name+" is open")
    def set_number_serving(self, val):
        self.number_served = val
    def incerement_number_served(self, new_value):
        self.number_served += new_value

Flavor = ['Vanilla','Chocolate','Strawberry']
class IceCreamStand(Restaurant):
    def __init__(self,restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = Flavor
    def dispaly_flavors(self):
        print("All flavors are listed below: ")
        for item in self.flavors:
            print(item)

ice_stand = IceCreamStand("Sheraton","Dhaka") #must include all the attrib value of super class/parent class(here "Restaurant")
ice_stand.dispaly_flavors()



#9.7 admin

class User():
    def __init__(self,first_name,last_name,phone_no):
        self.first_name = first_name
        self.last_name = last_name
        self.phone_no = phone_no
    def describe_user(self):
        print("Name: " + self.first_name + " " + self.last_name + "\nMobile no: "+ self.phone_no)
    def greet_user(self):
        print("Helle Mr. "+ self.first_name + " " + self.last_name + ", Hope your are hale and hearty.")

Options = ['can add post','can delete post','can ban user']
class Admin(User):
    def __init__(self,first_name,last_name,phone_no):
        super().__init__(first_name,last_name,phone_no)
        self.privilege = Options
        self.piv = Privileges()
    def show_privilege(self):
        print("\nAll privileges are: ")
        for item in self.privilege:
            print(item.title())


#9.8 privileges

class Privileges():
    def __init__(self):
        self.privilege = Options

    def show_privilege(self):
        print("\nAll privileges are: ")
        for item in self.privilege:
            print(item)
    

new_admin = Admin("Sharif","Abdullah","01574555698")
new_admin.piv.show_privilege()

admin_privilege = Admin("Ahmed","Fahad","01766610057")
admin_privilege.show_privilege()

#9.9 battery_upgrade

class Car():
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

class Battery():
    def __init__(self,battery_size=80):
        self.battery_size = battery_size
    def describe_battery(self):
        print("This car has a " + str(self.battery_size) + "-KWh battery.")
    def get_range(self):
        if self.battery_size == 80:
            range = 240
        elif self.battery_size == 85:
            range = 375

        message = "this car can go approximately " + str(range) + " miles on a full charge."
        print(message)
    def upgrade_battery(self):
        if self.battery_size != 85:
            self.battery_size = 85



class NewElectricCar(Car):             #child class of Car
    pass                                # using pass all the attrib of Car will pass through this subclass


class ElectricCar(Car):
    def __init__(self, make, model, year):
        self.battery_size = 70 
        super().__init__(make, model, year) #this super() method does almost the same work as pass
        self.battery = Battery()            #inheritance as attributes
    def describe_battery(self):
        print("This car has a "+ str(self.battery_size)+"-KWh battery.")
    def fill_gas_tank(self): #as 'self' is not present this class will ignore this method if it is called
        print("This car doesn't need a gas tank!")

electric_car = ElectricCar("Lamborghini","Germany","2018")
electric_car.battery.get_range()
electric_car.battery.upgrade_battery()
electric_car.battery.get_range()