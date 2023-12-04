"""
Author: Yash Kapoor
Student ID: 101163338

THIS IS PROBLEM 4 C): ENROLMENT MECHANISM
"""

import time

import PasswordManager
import AccessControlSystem

def get_user_role(username, file="passwd.txt"):
    """
    Gets the role of the user (e.g., Regular Client, Premium Client, etc.)
    from the file that is used to store records (by default, it is set to
    passwd.txt. For testing purposes, I shall use a different file called
    test_passwd.txt, which is why this function takes in a file parameter.
    :param username:    a string, the username to check for existence in the file.
                        After the username is found in the file, then we have found
                        the record that we are looking for. Then, we can search
                        that record for what the user's role is.
    :param file:    A string, the path to the password file where
                    the records are stored. Default file is
                    "passwd.txt". I have introduced this parameter
                    for testing purposes since I am using a different
                    file called "test_passwd.txt" specifically for
                    testing.
    :return:    A string, the role of the user. If the username
                is not found in the password file, then None
                is returned.
    """
    with open(file, 'r') as password_file:
        for record in password_file:
            stored_username = record.strip().split(",")[0]
            stored_role = record.strip().split(",")[2]
            if stored_username == username:
                # username is found in the password file, so
                # return the role that is associated with that username
                return stored_role
    return None


def login_user(testing_login=False, testing_access_control=False, file="passwd.txt"):
    """
    Login interface for an individual to log in
    into the Finvest Holdings' System. This is where existing employees
    can log in into the system by entering their username and password.
    After they log in with a valid set of credentials, then they are displayed
    the following information:
    User ID, role, and a list of the access rights or permissions according to
    the access control policy provided by Finvest Holdings.

    If an individual incorrectly enters their username and/or password five
    times, then they must wait two minutes before retrying. This is to prevent
    brute-force attacks and ensure this system has enhanced security measures.

    Additionally, they can choose which resources they would like to access
    and the system shall either grant or deny them permission depending on
    their access rights.
    :param testing_login: A boolean, specifically for testing the log in functionality.
                          True if a testing function is calling login_user,
                          False otherwise and by default, this is set to False.
    :param testing_access_control: A boolean, specifically for testing the enforcement of
                                   the access control mechanism functionality.
                                   True if a testing function is calling login_user,
                                   False otherwise and by default, this is set to False.
    :param file: A string, the path to the password file where
                 the records are stored. Default file is
                 "passwd.txt". I have introduced this parameter
                 for testing purposes since I am using a different
                 file called "test_passwd.txt" specifically for
                 testing.
    :return: Depending on the parameters used for testing, this function may return a specific
             string indicating the outcome of the test (e.g., "access_granted", "access_denied",
             "successful_enforcement_of_access_control", "go_back"). Otherwise, this shall
             proceed to output user information (i.e., User ID, role, access rights) upon successful login
             or prompt the user to re-enter the fields that they have incorrectly filled out.
    """
    attempts = 0
    max_attempts = 5
    wait_time = 120
    # prevents brute-force attacks

    while attempts < max_attempts:
        # lets the user try to enter their credentials
        # a total of five times before making them
        # wait two minutes
        print("\n\nLogin: ")
        username = input("\nEnter username (q to go to main menu): ")
        if username.lower() == "q":
            return "go_back"

        password = input("Enter password (q to go to main menu): ")
        if password.lower() == "q":
            return "go_back"

        if PasswordManager.verify_password(username, password, file):
            print("ACCESS GRANTED!")
            if testing_login:
                return "access_granted"

            # Enforcing the access control mechanism
            role = get_user_role(username, file)
            if role:
                print("\nUser ID: " + username)
                print("Role: " + role)
                print("\nList of resources in the system: ")
                for resource in AccessControlSystem.access_control_list.keys():
                    print(resource)
                print("\nAccess Control List for " + role + ":")
                for resource, permissions in AccessControlSystem.access_control_list.items():
                    if role in permissions:
                        print(resource + ": " + "/".join(permissions[role]))

                if testing_access_control:
                    return "successful_enforcement_of_access_control"

                while True:
                    # keeps on prompting the user to enter the resource
                    # they would like to access until they decide
                    # to exit the program
                    chosen_resource = input("\nEnter what resource you would like to access (q to sign out): ")
                    if chosen_resource == "q":
                        break

                    if chosen_resource.lower() in AccessControlSystem.access_control_list.keys():
                        while True:
                            # keeps on prompting the user to enter what they want to do with
                            # the resource they have entered until they enter a valid permission
                            # that exists in the system (i.e., read, write, validate modifications)
                            chosen_permission = input("\nChoose what you want to do with"
                                                      " this resource (read, write, validate modifications): ")
                            if (chosen_permission.lower() == "read" or
                                    chosen_permission.lower() == "write" or
                                    chosen_permission.lower() == "validate modifications"):
                                AccessControlSystem.has_access(role, chosen_resource, chosen_permission)
                                break
                            else:
                                print("The permission you entered does not exist in the system. Try again!")
                    else:
                        print("The resource you entered does not exist in the system. Try again!")
            else:
                print("Unable to get the role of the user.")
            break
        else:
            print("ACCESS DENIED!")
            print("Incorrect username and/or password. Please try again!")
            if testing_login:
                return "access_denied"
            attempts += 1

        if attempts == max_attempts:
            print("You have reached the maximum number of login attempts. Please try again in 2 minutes!")
            time.sleep(wait_time)
            attempts = 0
