import pizza as p #that means including the entire pizza named py file which is in the same directory, p is an alias of pizza named py file
from pizza import build_profile #that means pizza a py file where build_profile is a function
from pizza import make_pizza #it means there is a function named make_pizza in pizza named py file
from pizza import make_pizza_2 as mp2 #mp2 is the alternative name of a function in the pizza named py file
from pizza import * #including all function from pizza py file

p.make_pizza(15,'papperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
data = build_profile(
    'albert', 'einstein',
    location = 'prinstone',
    field = 'physics',
    occupation = 'scientist'
)

mp2(12,'macoronni')
mp2(16,'cheese','chicken')
print(data)