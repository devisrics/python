import random

print("Welcome to the game")
user_input=input("Please enter any one rock paper or scissor: ").lower()
computer_input=["rock","paper","scissor"]
computer_choice=computer_input[random.randint(0,2)]


if user_input==computer_choice:
    print("Match Draw!")

elif user_input=="rock":
    if computer_choice=="paper":
        print("You lose!")
    else:
        print("you won!")
    
elif user_input=="paper":
    if computer_choice=="scissor":
        print("You lose!")
    else:
        print("You Won!")

elif user_input=="scissor":
    if computer_choice=="paper":
        print("You won!")
    else:
        print("you lose")

else:
    print("Invalid Input")

print( f"You Chose:{user_input} and Computer Chose:{computer_choice}")
