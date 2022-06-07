#7.4 pizza toppings

promt = "Enter your favorite pizza toppings.\nEnter 'quit' to stop asking questoin."

msg = ''
while True:
    msg = input(promt)
    if msg == 'quit':
        break
    else:
        print("I'll add "+msg.title()+" in your pizza.")

print("-----------------------------------------------------")
#7.5 movie tickets

while True:
    age  = int(input("Enter your age(Enter 0 to quit the loop) >> "))
    if age == 0:
        break

    if age < 3:
        print("Its Free!!!!")
    elif age >=3 and age <12:
        print("Price: 10$")
    else:
        print("Price: 15$")

print("-----------------------------------------")
    
#7.6 three exits

#all of these condition have been used in the previous exercies

#7.7 infinity

i=1
while True:
    print(i)
    i+=1
   