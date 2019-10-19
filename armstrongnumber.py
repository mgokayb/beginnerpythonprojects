number = input("Give me a number for checking its an armstrong number or not >>>> ")
result = 0
for i in range(len(number)):
    a = int(number[i])
    result += a * a * a * a
if result == int(number):
    print(f"This number: ({number}) is an armstrong number.")
else:
    print(f"This number: ({number}) is NOT an armstrong number.")
