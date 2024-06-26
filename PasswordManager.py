"""
Author: Yash Kapoor
Student ID: 101163338

THIS IS PROBLEM 2 C) AND
PROBLEM 4 B) IS THE VERIFY_PASSWORD() FUNCTION AT THE VERY END OF THIS FILE.
"""

import bcrypt


def hash_password(password):
    """
    Hashes a password using bcrypt. It takes a plaintext
    password as input, generates a salt using bcrypt, and
    then hashes the password, which is then returned.

    The hashed password contains a hash value along
    with the salt that was generated by bcrypt.

    :param password:    a string, the plaintext password to hash
    :return:    a number of bytes, the hashed password
    """
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password.encode('utf=8'), salt)


def get_all_records(file='passwd.txt'):
    """
    Gets all the records that are in the password file.
    :param file: A string, the path to the password file where
                 the records are stored. Default file is
                 "passwd.txt".
    :return:    a list of dictionaries, where each dictionary
                represents a user record.
    """
    records = []
    with open(file, 'r') as password_file:
        for line in password_file:
            record_elements = line.strip().split(",")
            record = {
                "username": record_elements[0],
                "hashed_password": record_elements[1],
                "role": record_elements[2],
                "account_status": record_elements[3]
            }
            # appending each dictionary to a list
            # to store the user records.
            records.append(record)
    return records


def add_record(username, password,
               role,
               account_status, file='passwd.txt'):
    """
    Adds a new record to the password file.
    Before adding a new record to the password file,
    this function hashes the password entered by the
    individual. Once it has been hashed, the record
    is added to the password file.

    :param username:    a string, the username of the new user
    :param password:    a string, the plaintext password of the new user
    :param role:    a string, the role of the new user
    :param account_status:  a string, the account status of the new user
    :param file:    A string, the path to the password file where
                    the records are stored. Default file is
                    "passwd.txt".
    :return: None
    """
    hashed_password = hash_password(password).decode('utf-8')
    with open(file, 'a') as password_file:
        password_file.write(username + ',' + hashed_password + "," + role + "," + account_status + "\n")


def get_usernames(file='passwd.txt'):
    """
    Gets a list of usernames from the password file.

    :param file: A string, the path to the password file where
                 the records are stored. Default file is
                 "passwd.txt".
    :return:    a list of usernames
    """
    usernames = []
    with open(file, 'r') as password_file:
        for record in password_file:
            username = record.strip().split(",")[0]
            usernames.append(username)
    return usernames


def verify_password(username, password, file="passwd.txt"):
    """
    THIS IS PROBLEM 4 B): PASSWORD VERIFICATION MECHANISM

    Verifies if the plaintext password matches the hashed password of
    a specific user.

    :param username:    a string, the username of the user whose password shall be verified
    :param password:    a string, the plaintext password that shall be verified
    :param file:    A string, the path to the password file where
                    the records are stored. Default file is
                    "passwd.txt".
    :return:    a boolean, True if the plaintext password matches the hashed password,
                False otherwise.
    """
    records = get_all_records(file)
    for record in records:
        if record["username"] == username and bcrypt.checkpw(password.encode('utf-8'),
                                                             record["hashed_password"].encode("utf-8")):
            # ensures the password entered by the user matches the hashed password
            return True
    return False












