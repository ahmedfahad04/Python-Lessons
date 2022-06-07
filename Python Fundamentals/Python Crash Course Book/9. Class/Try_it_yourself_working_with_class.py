#9.4 number served

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



restaurant = Restaurant("Hotel Sheraton","Dhanmondi")
print("Total customer served "+ str(restaurant.number_served))
restaurant.set_number_serving(5)
print("After serving customer now the number is: "+ str(restaurant.number_served))
restaurant.incerement_number_served(15)
print("After serving customer now the number is: "+ str(restaurant.number_served))


#9.5 login attempts


class User():
    def __init__(self,first_name,last_name,phone_no):
        self.first_name = first_name
        self.last_name = last_name
        self.phone_no = phone_no
        self.login_attempt = 0

    def describe_user(self):
        print("Name: " + self.first_name + " " + self.last_name + "\nMobile no: "+ self.phone_no)
    def greet_user(self):
        print("Helle Mr. "+ self.first_name + " " + self.last_name + ", Hope your are hale and hearty.")
    def increment_login_attempts(self):
        self.login_attempt += 1
    def reset_login_attempt(self):
        self.login_attempt = 0

new_user = User("Ahmed",'Fahad',"0178886542")
new_user.increment_login_attempts()
new_user.increment_login_attempts()
new_user.increment_login_attempts()
new_user.increment_login_attempts()
print("Use tried to login "+str(new_user.login_attempt)+" times.")
new_user.reset_login_attempt()

print("After reset, Use tried to login "+str(new_user.login_attempt)+" times.")

