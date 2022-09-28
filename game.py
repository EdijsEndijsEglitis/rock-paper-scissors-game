import random
turns = ["rock", "paper", "scissors"]
player_turns = []
computer_turns = []


while(True):
    human_turn = input("Choose Rock/Paper/Scissors or 'Quit' to quit :")
    computer_turn = random.choice(turns)


    if  human_turn == "quit":
        print("Thanks for playing! Goodbye!")
        break
    
    player_turns.append(human_turn)
    computer_turns.append(computer_turn)
    

    human_turn = human_turn.lower()
    print(f'Human: {human_turn} vs Computer: {computer_turn}')
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
    


print(f'You have played {len(player_turns)} games' )
print(player_turns)
print(computer_turns)



