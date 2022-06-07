#9.10 imported restaurant

from restaurant import *

rest = Restaurant("Hotel Sea Shell","Cox's Bazar",)
rest.describe_restaurant()

#9.11 imported admin

import admin

user_admin = admin.Admin("Istiaq ","Ahmed Fahad","0176610097")
user_admin.show_privilege()

#9.12 multiple modules

from admin2 import Admin

user_admin2 = Admin("Istiaq ","Ahmed Fahad","0176610097")
user_admin2.show_privilege()
print(user_admin2.phone_no)