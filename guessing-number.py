import random
numberofguesses = 0
print("""Hello darling, What's your name? 
        ------------- """)
name = input()
number = random.randint(1,24)
print("I pick a number between 1-24",name,"can you guess it? yes or no?")
yes_no = input()
while True:
    if yes_no == "yes":
        while numberofguesses < 5:
            print("So take a guess =  ")
            guess = int(input())
            numberofguesses = numberofguesses + 1
            if guess < number:
                print("UP!")
            if guess > number:
                print("DOWN!")
            if guess == number:
                break
        if guess == number:
            print("Well Done!", name, "You guessed right number. (",number,")")
            break
        if guess != number:
            number = str(number)
            print("""
                Game Over!!
            The Number was : """, number)
            break
    elif yes_no == "no":
        print("Ok bb!",name,"!")
        break
    else:
        print("Srry wut? plz type 'yes' or 'no'")
        yes_no = input()



