import random
point = 0
while True:
    list = [
        "rock",
        "paper",
        "scissors",
    ]
    player = input("Hi Rock-Paper-Scissors's game. You have " + str(point) + " point. Start choosing one!  >>  ")
    i = random.randint(0, 2)
    if player.lower() == "rock" and list[i] == "scissors":
        print("Hey! You win!!")
        point = point + 1
    elif player.lower() == "rock" and list[i] == "rock":
        print("No winner, again!")
    elif player.lower() == "paper" and list[i] == "rock":
        print("Hey! You win!!")
        point += 1
    elif player.lower() == "paper" and list[i] == "paper":
        print("No winner, again!")
    elif player.lower() == "scissors" and list[i] == "paper":
        print("Hey, you win!")
        point += 1
    elif player.lower() == "scissors" and list[i] == "scissors":
        print("No winner! Try again!")
    elif player.lower() == "quit":
        break
    else:
        print("You lose!!")
        point -= 1
