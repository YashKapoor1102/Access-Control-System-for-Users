"""
Author: Yash Kapoor
Student ID: 101163338

THIS IS PROBLEM 4 C): PROACTIVE PASSWORD CHECKER
"""

import re


def load_common_weak_passwords(file="common_weak_passwords.txt"):
    """
    Loads a list of a common weak passwords from the file called
    common_weak_passwords.txt. For now, I have only added four common
    weak passwords in the file. However, in the future, we can add more
    common weak passwords to it if needed.
    :param file:    a string, the path to the common_weak_passwords.txt file
                    to read the common weak passwords from.
    :return:    a list of strings, where each string represents
                a common weak password.
    """
    with open(file, 'r') as common_weak_passwords_list:
        return common_weak_passwords_list.read().splitlines()


def is_password_valid(username, password):
    """
    Checks whether the password specified by the user is valid.
    It ensures the password does not include dates, license plate numbers,
    and phone numbers. Also, it ensures the password is between 8
    and 12 characters, includes at least one upper-case letter, one
    lower-case letter, one digit, and one symbol from the set: {!, @, #, $, %, ?, *}.
    Moreover, it ensures the username is not included in the password. Finally, it
    prevents the user from choosing a password that is included
    in the common_weak_passwords.txt file.

    :param username:    a string, the username of the individual that is enrolling
                        in the system.
    :param password:    a string, the password of the individual that is enrolling
                        into the system. This is the password that shall be checked to
                        ensure it is valid.
    :return:    a boolean, True if the password meets all the conditions above (valid password entered),
                False otherwise (invalid password entered).
    """
    common_weak_passwords = load_common_weak_passwords()

    if username.lower() in password.lower():
        return False
    if re.search(r'\b\d{1,2}/\d{1,2}/\d{2,4}\b', password):
        # first pattern checks to see if calendar dates exist anywhere in the string
        print("Your password cannot include dates")
        return False
    if re.search(r'[A-Z]{2,3}-?[0-9]{3,4}', password):
        # second pattern checks to see if license plate numbers exist anywhere in the string
        print("Your password cannot include license plate numbers")
        return False
    if re.search(r'\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4}', password):
        # third pattern checks to see if phone numbers exist anywhere in the string
        print("Your password cannot include phone numbers")
        return False
    if len(password) < 8 or len(password) > 12:
        print("Your password must be between 8 and 12 characters")
        return False
    if not any(char.isupper() for char in password):
        print("Your password must include at least one upper-case letter")
        return False
    if not any(char.islower() for char in password):
        print("Your password must include at least one lower-case letter")
        return False
    if not any(char.isdigit() for char in password):
        print("Your password must include at least one digit")
        return False
    if not any(char in '!@#$%?*' for char in password):
        print("Your password must include at least one special character from the set: {!, @, #, $, %, ?, *}")
        return False
    if password in common_weak_passwords:
        print("Oops! Your password is in the common list of passwords. Try again!")
        return False

    return True









