import random
import csv
from turtle import screensize 
random.seed()   #Prepare random number generator


def greetUser():
    name = input("\nPlease enter your first name: ")
    print("Hello ", name, "!")
    return name

    
def gameRound(guessedNumber, userName):
    
    counter = 1
    while True:
        userGuess = int(input("Please guess a number between 1 and 10 ..."))
        
        if userGuess == guessedNumber:
            print("Congratulations," , userName, "! You guessed the number in ", counter, " tries!")
            return counter
        
        else:
            
            if guessedNumber > userGuess:
                print("You guessed too low...")
            else:
                print("You guessed too high...")
                
        counter += 1
        
        
def sortedList(scoreboard):
    
    size = len(scoreboard)
    
    for i in range(0, size):
        for j in range(0, size - i - 1):
            if scoreboard[j][1] > scoreboard[j+1][1]:
                temp = scoreboard[j]
                scoreboard[j] = scoreboard[j+1]
                scoreboard[j+1] = temp
                
    return scoreboard
        

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
     
     
     
    # Fetch the previous top scorer   
    readFile = csv.reader(open("games.csv", "r"))   # Open games.csv file for reading
   
    currentWinnerName = ""
    currentWinnerScore = 0        
    
    cnt = 0
    for row in readFile:
        
        if cnt == 1:
            previousWinnerName = row[0]
            previousWinnerScore = row[1]
            break
        
        cnt += 1
        
   
    # fetch the current top scorer
    scoreboard = sortedList(scoreboard)  # Sort scoreboard
    currentWinnerName = scoreboard[0][0]
    currentWinnerScore = scoreboard[0][1]
    
    # Print header
    print("**** Score Board ****")
    print("---------------------------")
    print("***Player","\t","Score***")    
    print("---------------------------")
    
    print(previousWinnerName,"\t\t",previousWinnerScore)
    print(currentWinnerName,"\t\t",currentWinnerScore)
    
    # Open topScorer.csv file for writing	
    topScorer = csv.writer(open("topScorer.csv", "w", newline=''))   
    topScorer.writerow([previousWinnerName, previousWinnerScore])
    topScorer.writerow([currentWinnerName, currentWinnerScore])
    
    # Open games.csv file for writing
    file = csv.writer(open("games.csv", "w", newline=''))   
    file.writerow(["Name", "Score"])    # Write header row

    for score in scoreboard:
        file.writerow([score[0], score[1]]);    # Write score row 
    
    