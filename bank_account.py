first_screen = """"
******************************
    Welcome to Shitty Bank
    Plz type a option
    -"info"
    -"deposit" money
    -"withdraw" money
    -"quit"
******************************
"""
print(first_screen)
customer_name = "John"
customer_surname = "SMITH"
customer_credit = 1000
value = None
customer_input = input(" ------>>>  ").lower()
while True:
    if customer_input == "info" or customer_input == "deposit" or customer_input=="withdraw" or customer_input=="quit":
        if customer_input == "info":
            print(f"""
--------------------------------------------------------------------------------------
                            Here is your info:
            Full Name           : {customer_name} {customer_surname} 
            Your credit limit   : {customer_credit} $
--------------------------------------------------------------------------------------              
                """)
            print(first_screen)
            customer_input = input(" ------>>>  ").lower()
        elif customer_input == "deposit":
            try:
                value = int(input("enter a value :  "))
            except ValueError:
                print("invalid value. Plz only digit!")
                print(first_screen)
                customer_input = input(" ------>>>  ").lower()
                continue
            customer_credit = customer_credit + value
            print(f"""
--------------------------------------------------------------------------------------            
            You deposit {value} $
            Your new credit limit is {customer_credit}
--------------------------------------------------------------------------------------
                """)
            print(first_screen)
            customer_input = input(" ------>>>  ").lower()
        elif customer_input == "withdraw":
            try:
                value = int(input("enter a value :  "))
            except ValueError:
                print("invalid value. Plz only digit!")
                print(first_screen)
                customer_input = input(" ------>>>  ").lower()
                continue
            if value <= customer_credit:
                customer_credit = customer_credit - value
                print(f""""
--------------------------------------------------------------------------------------                
                You have withdraw {value} $
                And you have {customer_credit} $ left
--------------------------------------------------------------------------------------
                        """)
                print(first_screen)
                customer_input = input(" ------>>>  ").lower()
            else:
                print(f"""
                You have entered invalid amount.
                You have {customer_credit}$ and you entered {value}$
                Try again!    
                    """)
                print(first_screen)
                customer_input = input(" ------>>>  ").lower()
        elif customer_input == "quit":
            ques_sure = "Are you sure?!? You are quiting! type 'y' or 'n' ----->> "
            checking_sure = input(ques_sure).lower()
            if checking_sure == "y":
                break
            elif checking_sure == "n":
                print(first_screen)
                customer_input = input(" ------>>>  ").lower()
            else:
                print("""
--------------------------------------------------------                
|                invalid input!                         |
--------------------------------------------------------""")
                print(first_screen)
                customer_input = input(" ------>>>  ").lower()

    else:
        print("you typed invalid option plz try again!")
        customer_input = input(" ------>>>  ").lower()
