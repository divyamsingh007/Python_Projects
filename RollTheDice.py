# importing useful lib
import random


# game logic
def gameLogic():

    # generating random number from 1 to 6
    randNum = random.randrange(1, 7)
    # print(randNum)

    # input from user
    userInput = input("Do you want to roll the dice(y/n): ")

    if userInput == "y" or userInput == "Y":
        print("Rolling Die...")
        print("The die has a value of:", randNum)
        gameLogic()
    elif userInput == "n" or userInput == "N":
        print("Thank you for playing.")
    else:
        print("Invalid input.")
        gameLogic()


gameLogic()
