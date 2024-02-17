"""This program allows user to access two different financial calculators:
 investment and home loan calculator
 The program outputs calculation based on the choice of the user from the
 menu and compute based on the inputs of the user."""
import math # importing libraries for math function
import os # importing libraries for clear screen function
choice = False
while not choice:
    print("=" * 80 )
    Menu = """\ninvestment - to calculate the amount of interest you'll earn on your investment
              \nbond       - to calculate the amount you'll have to pay on a home loan
              \nquit       - to exit the program
           """
    print(Menu)
    print("=" * 80 )
    menu = input("\nEnter either 'investment'or 'bond' from the menu above to proceed and 'q' to"
                  " exit the program: ").lower()
    os.system('cls') # clears the screen

    # choice1 = "investment"
    choice2 = "bond"
    # user chooses investment, it calculates interest earn in simple or 
    # compound interest.
    if  menu == "investment":
        # choice = False
        # while not choice:
            print("_" * 14, "Investment Calculation", "_" * 14) 
            try:            
                amount_money = float(input("\nEnter amount of money to be deposited:\t\t £"))
                interest_rate = float(input("Enter interest rate. (e.g. 8):\t\t\t %"))
                number_year = int(input("Enter number of years to invest:\t\t  "))
                interest = input("Enter type of interest rate (simple/compound):\t ").lower()
                choice1 = "simple"
                choice2 = "compound"
                if interest == choice1:
                    percentage_rate = interest_rate / 100
                    simple_computation = amount_money * (1 + percentage_rate * number_year )
                    print(f"Your investment would be worth: \t\t £{simple_computation:0.2f}\n")
                elif interest == choice2:
                    percentage_rate = interest_rate / 100
                    compound_computation = amount_money * math.pow((1 + percentage_rate), number_year)
                    print(f"Your investment would be worth: \t\t {compound_computation:0.2f}\t\t\n")
                else:
                    print("\nMake sure to enter simple or compound only!")
                     
                repeat = input("\nWould you like to try again? (Y/N): ")
                os.system('cls')
                if repeat.lower() == 'y':
                    continue
                else:
                    choice = True

            except ValueError:
                print("Invalid input!")
                repeat = input("\nWould you like to continue? (Y/N): ")
                os.system('cls')
                if repeat.lower() == 'y':
                    continue
                else:
                    choice = True
                 
             

    # user chooses 'bond', it calculates the payment for the home loan
    elif menu == choice2:
            print("_" * 17, "Bond Calculation", "_" * 17)
            try:
                value_of_home = float(input("\nEnter present value of the house (e.g. 100000):\t\t £"))
                interest_rate = float(input("Enter interest rate (e.g. 7):\t\t\t\t %"))
                number_month = int(input("Enter number of months to pay the bond. (e.g. 120):\t  "))
                percentage_rate = (interest_rate / 100) / 12
                repayment = (percentage_rate * value_of_home) / (1 - (1 + percentage_rate) ** (-number_month))
                print(f"Your monthly payment is: \t\t\t\t £{repayment:0.2f}\n")
                repeat = input("Would you like to try again? (Y/N) ")
                os.system('cls')
                if repeat.lower() == 'y':
                    continue
                else:
                    choice = True
            except ValueError:
                print("Invalid input")
                repeat = input("\nWould you like to continue? (Y/N): ")
                os.system('cls')
                if repeat.lower() == 'y':
                    continue
                else:
                    choice = True


    # user doesn't type valid input.
    # The `else` statement is executed when the user's input does not match any of the valid options
    # ("investment" or "bond"). It prints a message informing the user that their input is not
    # recognized and reminds them to choose only from the given options.
    elif menu == 'q':
        choice = True
    else:
        print("\033[5mYour input is not recognized. Choose only from the given option\033[0m.\n")
       
       
