while True:
    num1 = int(input("enter a number: "))
    operation = input("chose a operation +, -, /, * :")
    num2 = int(input("enter a another number :"))
    result = 0
    if operation == "+":
        result = num1 + num2
        print(result)
        break
    elif operation == "-":
        result = num1 - num2
        print(result)
        break
    elif operation == "/":
        result = num1 / num2
        print(result)
        break
    elif operation == "*":
        result = num1 * num2
        print(result)
        break
    else:
        print("please Chose valid operation")

