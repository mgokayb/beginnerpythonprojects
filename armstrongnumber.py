
number = input("Give me a number for checking its an armstrong number or not >>>> ")
while True:
    try:
       val = int(number)
       result = 0
       for i in range(len(number)):
           a = int(number[i])
           result += a * a * a * a
       if result == int(number):
           print(f"This number: ({number}) is an armstrong number.")
           number = input("Give me a number for checking its an armstrong number or not >>>> ")
       else:
           print(f"This number: ({number}) is NOT an armstrong number.")
           number = input("Give me a number for checking its an armstrong number or not >>>> ")
    except ValueError:
        if number == "quit":
            break
        else:
            print("That's not a number!")
            number = input("Give me a number for checking its an armstrong number or not >>>> ")
