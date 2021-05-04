import random
x = 0
y = 0
while x<3 or y<3:
    player_user = input('Choose your weapon! Rock, paper, or scissors?')
    game = ["rock", "paper", "scissors"]
    player_computer = random.choice(game)
    if player_user == player_computer:
        print("It's a tie!")
    elif player_user == "rock":
        if player_computer == "scissors":
            print("Rock beats scissors! Great job!")
            x = x + 1
        else:
            print("Paper covers rock, bummer! Siri wins this round.")
            y = y + 1
    elif player_user == "paper":
        if player_computer == "rock":
            print("Paper covers rock - way to go! You won this round!")
            x = x + 1
        else:
            print("Scissors slice through paper - this round goes to Siri!")
            y = y + 1
    elif player_user=="scissors":
            if player_computer == "paper":
                print("Scissors beat paper - you made the cut!")
                x = x + 1
            else:
                print("Uh-oh, looks like this rock smashed your scissors! Siri beat you!")
                y = y + 1
else:
    if x == 3:
        print("Congrats Grand Champion! You beat Siri!")
    elif y == 3:
        print("Siri won! Better luck next time!")

