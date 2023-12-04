"""
Author: Yash Kapoor
Student ID: 101163338

THIS IS PROBLEM 3 C)
"""

import os

import ProactivePasswordChecker
import PasswordManager
import LoginInterface


def is_username_invalid(username, file='passwd.txt'):
    """
    Checks if the username already exists in the password file specified
    (default is passwd.txt file if the file is not specified)

    :param username:    A string, the username that the individual enters
    :param file:    A string (optional parameter), the path to the password file
                    where the usernames are stored. Default file is "passwd.txt"
                    if it is not specified.
    :return:    True if the username exists in the file (valid username),
                False otherwise (invalid username)
    """
    # Check if the file exists
    if not os.path.exists(file):
        # If the file doesn't exist, the username is invalid (it's not in the file)
        return False

    if len(username) < 4 or len(username) > 20:
        print("The username must be between 4 and 20 characters long. Try again!")
        return True

    existing_usernames = PasswordManager.get_usernames(file)
    if username in existing_usernames:
        print("This username is already taken. Please try inputting a different username.")
    return username in existing_usernames


def register_user(file="passwd.txt", testing=False):
    """
    Enrolment interface for an individual to enroll themselves
    into the Finvest Holdings' System. This is where new employees
    can enroll themselves into the system by creating a username, password,
    and selecting their role in the company.
    :param file:        A string, the path to the password file where
                        the records are stored. Default file is
                        "passwd.txt". I have introduced this parameter
                        for testing purposes since I am using a different
                        file called "test_passwd.txt" specifically for
                        testing.
    :param testing:     A boolean, specifically for testing purposes.
                        True if a testing function is calling register_user,
                        False otherwise and by default, this is set to False.
    :return:    Returns a string indicating the outcome of the registration process
                ("go_back, "username_already exists", "password_mismatch", "password_weak",
                "invalid_role_number) if we are running this in a testing environment.
                Otherwise, this shall proceed to the login interface upon
                successful registration or prompt the user to re-enter
                the fields that they have incorrectly filled out.
    """
    while True:
        # keeps prompting the user to enter their username
        # until what they have entered is valid (i.e., does
        # not exist in the password file, and it is between
        # 4 and 20 characters)
        print("\n\nRegistration:")
        username = input("Enter username (Type q to go back to the main menu): ")
        if username == "q":
            return "go_back"
        if is_username_invalid(username.lower(), file):
            if testing:
                return "username_already_exists"
            continue
        break

    while True:
        # keeps prompting the user to enter their password
        # until what they have entered is valid (i.e., the
        # proactive password checker returns True, and
        # they have confirmed their password successfully)
        password = input("Enter password (Type q to go back to the main menu): ")
        if password == "q":
            return "go_back"
        confirm_password = input("Confirm password: ")
        if password != confirm_password:
            print("Passwords do not match. Please try again!")
            if testing:
                return "password_mismatch"
            continue
        if not ProactivePasswordChecker.is_password_valid(username, password):
            print("Oops! This password cannot be chosen. Try again!")
            if testing:
                return "password_weak"
            continue
        break

    roles_list = {
        "1": "Regular Client",
        "2": "Premium Client",
        "3": "Financial Planner",
        "4": "Financial Advisor",
        "5": "Investment Analyst",
        "6": "Technical Support",
        "7": "Teller",
        "8": "Compliance Officer"
    }

    while True:
        # keeps prompting the user to enter their role
        # until what they have entered is valid (i.e., a number
        # from 1 to 8). The role is chosen from roles_list above by
        # entering a number from 1 to 8)
        print("\nList of roles: ")
        for number, role in roles_list.items():
            print(number + ": " + role)
        user_role_input = input("Enter the number that corresponds to your role: ")
        user_role = roles_list.get(user_role_input)
        if user_role is None:
            # user has entered a number that is invalid (outside the range of 1 to 8)
            print("You have entered an invalid role number. Please try again!")
            if testing:
                return "invalid_role_number"
            continue
        break

    PasswordManager.add_record(username.lower(), password,
                               user_role,
                               "Active", file)
    print("Enrolled successfully!")

    if not testing:
        # let the user log in after they have
        # registered as long as we are not
        # in the testing environment
        LoginInterface.login_user()

