#8.15 printing  models && 8.16 imports

import printing_functions as pf
from printing_functions import greet_users
from printing_functions import print_models as pm

usernames = ['hannah','tenni','margot']
greet_users(usernames)


unprinted_designs = ['iphone case','robot pendant','dodecahendron','motorolla']
completed_models = []

pm(unprinted_designs, completed_models)
pf.show_completed(completed_models)

print("------------------------------------")
#8.16 imports

