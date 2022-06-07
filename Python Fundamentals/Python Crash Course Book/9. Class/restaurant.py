class Restaurant():
    def __init__(self,restaurant_name, cuisine_type):# all atributes will be gathered here
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):  #declearing self is a must
        print("Name is: "+ '"' +self.restaurant_name + '"'+" And its cuisine is: "+ '"' +self.cuisine_type+'"')
    def open_resaturant(self):
        print(self.restaurant_name+" is open")
    def set_number_serving(self, val):
        self.number_served = val
    def incerement_number_served(self, new_value):
        self.number_served += new_value