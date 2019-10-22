from time import sleep
from random import randint

response = [
    "It will",
    "Hmm that's hard one i couldn't sure, ask me later again.",
    "Without a doubt",
    "Yes, definitely",
    "Almost happen",
    "not sure but seems like yes",
    "Most likely",
    "sorry don't know ask again",
    "Yes",
    "Signs point to YES!",
    "Quite possibly",
    "Ask again later",
    "Better not tell you now",
    "Cannot predict now",
    "Don't count on it",
    "No! do not even try!",
    "My sources say no",
    "not so good",
    "Very doubtful but..."]

def play():
    wish = str(input("""Hi darling i am Magic 8-ball. 
    Do u have a wish? 
    Do u wanna know it will happen or not? 
    Go ahead ask me  ---->>>    
    """).lower())
    print("hmm i am thinking wait a bit...")
    sleep(1)
    print(response[randint(0, 19)])
    playloop()





def playloop():
    wish_again = str(input("Would you like to ask another question? (y/n)\n").lower())
    if wish_again == 'y':
        play()

    elif wish_again == 'n':
        print("Goodbye!, come back soon")

    else:
        print("What was that?")
        playloop()
play() 
