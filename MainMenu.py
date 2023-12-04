"""
Author: Yash Kapoor
Student ID: 101163338

THIS IS THE FILE THAT NEEDS TO BE RUN
TO RUN THE PROGRAM.
"""

from LoginInterface import login_user
from EnrolmentInterface import register_user

if __name__ == '__main__':
    """
    This is the main menu of the program.
    It lets the individual choose from two options, 
    which are to enroll themselves into the Finvest
    Holdings' system or log in if they already have 
    an account (i.e., they already enrolled themselves). 
    They can also type "q" to exit the program. 
    """
    while True:
        print("\n1. Register (Enroll)")
        print("2. Log In")
        print("\nType \"q\" to quit at any time\n")
        user_choice = input("Please enter the number corresponding to the action you wish to perform: ")

        if user_choice == "q":
            break
        if user_choice == "1":
            register_result = register_user()
            if register_result == "go_back":
                # The user can go back to the main menu
                # from the registration page if they want
                # to by typing "q"
                continue
        elif user_choice == "2":
            login_result = login_user()
            if login_result == "go_back":
                # The user can go back to the main menu
                # from the login page if they want
                # to by typing "q"
                continue
        else:
            # User chose neither option 1 nor option 2
            print("Oops! You have entered an invalid input. Try again!")