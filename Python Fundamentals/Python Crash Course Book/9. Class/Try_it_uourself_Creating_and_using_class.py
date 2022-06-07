#9.1 restaurant

class Restaurant():
    def __init__(self,restaurant_name, cuisine_type):# all atributes will be gathered here
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):  #declearing self is a must
        print("Name is: "+ self.restaurant_name +" And its cuisine is: "+ self.cuisine_type)
    def open_resaturant(self):
        print(self.restaurant_name+" is open")

restaurant_1 = Restaurant("Ocean Paradise","Bangladeshi")
restaurant_2 = Restaurant("White House","English")

print("The hotel named "+ restaurant_2.restaurant_name.title()+" is in "+ restaurant_2.cuisine_type.rstrip("i") +
" which mainly covers the "+restaurant_2.cuisine_type+" cuisine")

restaurant_2.describe_restaurant()
restaurant_2.open_resaturant()


#9.2 three restaurants

r1 = Restaurant("Sonar Bangla Hotel", "Dhanmondi")
r2 = Restaurant("Bali :)","Indonesia")
r3 = Restaurant("Sea GUl", "Chittagong")
r1.describe_restaurant()
r2.describe_restaurant()
r3.describe_restaurant()

#9.3 user

class User():
    def __init__(self,first_name,last_name,phone_no):
        self.first_name = first_name
        self.last_name = last_name
        self.phone_no = phone_no
    def describe_user(self):
        print("Name: " + self.first_name + " " + self.last_name + "\nMobile no: "+ self.phone_no)
    def greet_user(self):
        print("Helle Mr. "+ self.first_name + " " + self.last_name + ", Hope your are hale and hearty.")

usr1 = User("Ashik","Khan","01766610078")
usr1.describe_user()
usr1.greet_user()
# if you are interested you may create more instanses and continue your experiment
    