# loop while in action

current_number = 1

while current_number<=10:
    print("The number is ", current_number)
    current_number += 1

# let user choose when to quit

promt = "\nTell me something, and I will repeat it back to you: "
promt += "\nEnter 'quit' to end the program."

msg = ''

while msg != 'quit':
    msg = input(promt)
    if msg != 'quit':
        print(msg.strip())
    if msg.strip() == 'quit':
        break

