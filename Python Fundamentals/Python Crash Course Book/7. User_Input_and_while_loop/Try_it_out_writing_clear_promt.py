#7.1 rental car

car = input("What kinds of car do uou want? ")
print("Let me see if I can find you a "+car.title())

print("------------------------------------------------")
#7.2 restaurant seating

people = int(input("How many people are there? "))
 
if people > 8:
    print("You will have to wait for a while.")
else:
    print("Table is ready.")

print("------------------------------------------------")
#7.3 multiples of ten

num = int(input("Enter a number: "))
if num%10 == 0:
    print("Its a multiple of 10")
else: 
    print("Its not")



