import random
random.seed()   #Prepare random number generator


def greetUser():
    name = input("\nPlease enter your first name: ")
    print("Hello ", name, "!")
    return name

    
def gameRound(guessedNumber, userName):
    
    counter = 1
    while True:
        userGuess = int(input("Please guess a number between 1 and 10 ..."))
        
        while userGuess:
            if userGuess > 10 or userGuess < 1:
                print("Your entered a number that is outside of the 1 through 10 interval.")
                userGuess = int(input("Please guess a number between 1 and 10 ..."))
                
            else:
                break
        
        if userGuess == guessedNumber:
            print("Congratulations," , userName, "! You guessed the number in ", counter, " tries!")
            return counter
        
        else:
            if guessedNumber > userGuess:
                print("You guessed too low...")
            else:
                print("You guessed too high...")
                
        counter += 1
        

if __name__ == '__main__':
    
    status = "Y"
    scoreboard = []
    
    while status == "Y" or status == "Yes" or status == "Yeah":
        
        userName = greetUser()
        guessedValue = random.randint(1, 10)
        score = gameRound(guessedValue, userName)
        
        individualScore = [userName, score]
        scoreboard.append(individualScore)
        
        status = input("Should I start another game? (Y/Yes/Yeah to continue) ")
        
    print("**** Score Board ****")
    print("---------------------------")
    print("***Player","\t","Score***")    
    print("---------------------------")
    
    
    for score in scoreboard:
        print(score[0],"\t\t",score[1])




