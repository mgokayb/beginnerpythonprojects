number = input("give me a number that i'll check its armstrong or not  >>  ")
def one_digit(number):
    result = int(number)**1
    if int(result) == int(number):
        print(f"{number} is armstrong number!")
    else:
        print(f"{number} is not an armstrong number!")
def two_digit(number):
    result = int(number[0]) ** 2 + int(number[1])**2
    if int(result) == int(number):
        print(f"{number} is armstrong number!")
    else:
        print(f"{number} is not an armstrong number!")
def three_digit(number):
    result = int(number[0]) ** 3 + int(number[1]) ** 3 + int(number[2]) ** 3
    if int(result) == int(number):
        print(f"{number} is armstrong number!")
    else:
        print(f"{number} is not an armstrong number!")
def four_digit(number):
    result = int(number[0]) ** 4 + int(number[1]) ** 4 + int(number[2]) ** 4 + int(number[3]) ** 4
    if int(result) == int(number):
        print(f"{number} is armstrong number!")
    else:
        print(f"{number} is not an armstrong number!")
def five_digit(number):
    result = int(number[0]) ** 5 + int(number[1]) ** 5 + int(number[2]) ** 5 + int(number[3]) ** 5 + int(number[4]) ** 5
    if int(result) == int(number):
        print(f"{number} is armstrong number!")
    else:
        print(f"{number} is not an armstrong number!")
def check_armstrong(number):
    if len(number) == 1:
        one_digit(number)
    elif len(number) == 2:
        two_digit(number)
    elif len(number) == 3:
        three_digit(number)
    elif len(number) == 4:
        four_digit(number)
    elif len(number) == 5:
        five_digit(number)
    else:
        print("there is smt wrong with"+number+"!!")
        number = input("give me a number that i'll check its armstrong or not >>  ")
        check_armstrong(number)
try:
    val = int(number)
    check_armstrong(number)
except ValueError:
    if number == "quit":
        print("Bye!!")
    else:
        print(f"Plz input only number!")
        number = input("give me a number that i'll check its armstrong or not")

