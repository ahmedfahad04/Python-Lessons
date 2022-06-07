#4.10 slices

cube = [1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]

print("First three item in the list are:\n",cube[:3])
print("Three items from the middle:\n",cube[5:8])
print("Last three items in the list:\n",cube[-3:])


print("---------------------------------------------")
#4.11 my pizzas, your pizzas

# friends_pizza = [] # if use this process then new item in this list will also append the main list
pizza = ['Chicken','Beef','Chesse']
friends_pizza = pizza[:]

pizza.append('Creamy')
friends_pizza.append('Butter')


print("My favorite pizzas are: ")
for item in pizza:
    print(">>",item)
print("My friends favorite pizza are: ")
for item in friends_pizza:
    print(">>",item)


print("---------------------------------------------")
#4.12 more loops

#just use loop to interate over the food item mentioned in foods.py program

