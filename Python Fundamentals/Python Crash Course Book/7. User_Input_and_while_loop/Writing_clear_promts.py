
prompt = "If you tell us who you are, we can personalize the messages you see."
prompt += "\nWhat is your first name? "

name = input(prompt)
print("\nHello, " + name + "!")

# use int() for numerical inputs
prmp = "How old are you?"
age = int(input(prmp))
print("I am "+str(age)+' years old.')
# age = int(age)
# print(type(age))

# the modulo operator
num = int(input("Enter a number. I'll tell you whether it is odd or even.."))

if num%2 == 0:
    print("Its even.")
else:
    print("Its odd.")


