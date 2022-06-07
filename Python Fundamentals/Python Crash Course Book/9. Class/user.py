class User():
    def __init__(self,first_name,last_name,phone_no):
        self.first_name = first_name
        self.last_name = last_name
        self.phone_no = phone_no
    def describe_user(self):
        print("Name: " + self.first_name + " " + self.last_name + "\nMobile no: "+ self.phone_no)
    def greet_user(self):
        print("Helle Mr. "+ self.first_name + " " + self.last_name + ", Hope your are hale and hearty.")