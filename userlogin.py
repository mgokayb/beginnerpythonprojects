print(""""
************************************
          User login 
          interface!
Enter the your id and password Plz
************************************
""")
try_limit = 3
user_id = "john"
user_pass = "nhoj"
while try_limit > 0:
    id = input("ID : ")
    password = input("PASSWORD : ")

    if try_limit == 0:
        print("Failed to log in!! B Y E")
    else:
        print(f"You have {try_limit-1} chance to log in! Try Again!")
        if user_id != id and user_pass == password:
            try_limit -= 1
            print(f"ID is wrong.")
        elif user_id == id and user_pass != password:
            try_limit -= 1
            print(f"PASSWORD is wrong.")
        elif user_id != id and user_pass != password:
            try_limit -= 1
            print(f"ID and PASSWORD is wrong.")
        else:
            print(""""
            ****************************** 
              Hello John. Welcome!
            
              You are logged on.
            ******************************
            """)
