import random

def get_choices():
    player_choice =input("Enter a choice (rock, paper, scissor):")
    options = ["rock", "paper", "scissor"]
    computer_choice = random.choice(options)
    choices ={"player": player_choice,"computer":computer_choice}

    return choices

def check_win(player,computer):
        print("you chose " + player + ", computer chose " + computer)
        if player == computer:
            return "It's a tie!"
        elif player == "rock":
                if computer =="scissor":
                    return "Rock smashes scissors! You win!"
                else:
                    return "Paper covers rock! You Lose."
        elif player == "paper":
                if computer =="rock":
                    return "Paper covers rock! You win!"
                else:
                    return "Scissors cuts paper! You Lose."
        elif player == "scissor":
                if computer =="paper":
                    return "Scissor cut paper! You win!"
                else:
                    return "Rock smashes scissors! You Lose."

choices = get_choices()
result = check_win(choices["player"], choices["computer"])
print(result)