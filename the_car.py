command = ""
started = False
while command != "quit":
    command = input("Give command to the car > >  ").lower()
    if command == "start":
        if started:
            print("Car has already started")
        else:
            started = True
            print(f"Car start moving")
    elif command == "stop":
        if started:
            started = False
            print("car stopped")
        else:
            print("car has already stopped")
    elif command == "quit":
        print("quiting from the loop...")
        break
    else:
        print(f"i dont understand the command '{command}'")
