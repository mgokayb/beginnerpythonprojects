while True:
    fside = input("first side :  ")
    sside = input("second side :  ")
    result = int(fside) ** 2 + int(sside) ** 2
    hiposide = int(input("hipo side :  ")) ** 2
    if result == int(hiposide):
        print("thats a Pythagorean Triangle")
        isquit = input("if u wanna quit just type quit")
        if isquit == "quit":
            break
        else:
            print("here we go again!")
    else:
        input("thats not a pytha triangle")
        isquit = input("if u wanna quit just type quit")
        if isquit == "quit":
            break
        else:
            print("here we go again!")
