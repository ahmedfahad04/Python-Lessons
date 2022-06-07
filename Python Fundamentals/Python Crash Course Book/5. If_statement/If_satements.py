age = 2

if age >= 20:
    print("it is greater")
else:
    print("Its not")

if age<4:
    print("Fee is: $0")
elif (age>=4 and age<=18):
    print("Fee is: $5")
else:
    print("Fee is: $10")

requested_toppings = ['mushrooms', 'extra cheese']
if 'mushrooms' in requested_toppings:
    print("Adding mushrooms.")
if 'pepperoni' in requested_toppings:
    print("Adding pepperoni.")
if 'extra cheese' in requested_toppings:
    print("Adding extra cheese.")

print("\nFinished making your pizza!")