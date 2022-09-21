import random

x = ["rock", "paper", "scissors"]

human_turn = input("Choose Rock/Paper/Scissors :")
computer_turn = random.choice(x)

human_turn = human_turn.lower()

if human_turn == "rock" and computer_turn == "scissors":
    print("Human wins!")
elif human_turn == "paper" and computer_turn == "rock":
    print("Human wins!")
elif human_turn == "scissors" and computer_turn == "paper":
    print("Human wins!")
elif human_turn == computer_turn:
    print("It's a draw!")
else:
    print("Computer wins!")
