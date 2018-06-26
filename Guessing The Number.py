# Guessing The Number Game
# Authored by Arpita Gupta
import random
randomNumber = random.randrange(0,100)
print("Hello!Welcome to The Guessing Game")
print("Random number has been generated")
guessed = False
while guessed==False:
    userInput = int(input("Please Enter your guessed Number "))
    if userInput==randomNumber:
        guessed = True
        print("Congratulations! You have guessed the right number")
    elif userInput>100:
        print("Our guess range is between 0 and 100, please try a bit lower")
    elif userInput<0:
        print("Our guess range is between 0 and 100, please try a bit higher")
    elif userInput>randomNumber:
        print("Try one more time, this time try a bit lower")
    elif userInput < randomNumber:
        print("Try one more time,this time try a bit higher")

print("End of program")
    
        
        
