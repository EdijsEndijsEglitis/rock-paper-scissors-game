import random


turns = ["rock", "paper", "scissors"]
player_wins = 0
games_played = 0


while(True):
    human_turn = input("Choose Rock/Paper/Scissors or 'Quit' to quit :")
    computer_turn = random.choice(turns)

    human_turn = human_turn.lower()
    print(f'Human: {human_turn} vs Computer: {computer_turn}')
    if human_turn == "rock" and computer_turn == "scissors":
        print("Human wins!")
        player_wins += 1
        games_played +=1
    elif human_turn == "paper" and computer_turn == "rock":
        print("Human wins!")
        player_wins += 1
        games_played +=1
    elif human_turn == "scissors" and computer_turn == "paper":
        print("Human wins!")
        player_wins += 1
        games_played +=1
    elif human_turn == computer_turn:
        print("It's a draw!")
        games_played +=1
    elif human_turn == "quit":
        print(f'You won {player_wins}/{games_played} games')
        print("Thanks for playing! Goodbye!")
        break
    else:
        print("Computer wins!")
        games_played +=1

