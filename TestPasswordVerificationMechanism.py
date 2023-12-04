"""
Author: Yash Kapoor
Student ID: 101163338

THIS IS PROBLEM 4 D): TEST PASSWORD VERIFICATION MECHANISM FOR USER LOGIN
"""

import os
import unittest

from PasswordManager import add_record, verify_password


class TestPasswordVerificationMechanism(unittest.TestCase):
    def test_verify_password(self):
        """
        Tests the verify_password() function that is used during the login process.

        It ensures that the verify_password() function is returning True
        if the plaintext password matches the hashed password of
        a specific user and False otherwise.

        There are four cases:
        1. username and password are correct (True returned by verify_password()).
        2. username is correct, password is incorrect (False).
        3. username is incorrect, password is correct (False).
        4. username is incorrect, password is incorrect (False).

        :return: None.
        """
        test_username = "test_user"
        test_password = "test_password"
        incorrect_password = "incorrect_password"
        nonexistent_user = "incorrect_user"
        test_file = "test_passwd.txt"

        if os.path.exists(test_file):
            # remove the test file if it already exists
            os.remove(test_file)

        add_record(test_username, test_password, "test_role", "active", test_file)

        # username and password are correct
        assert verify_password(test_username, test_password, test_file), ("Password verification shall"
                                                                          " succeed as the credentials are correct")

        # username is correct, but password is incorrect
        assert not verify_password(test_username, incorrect_password, test_file), ("Password verification shall"
                                                                                   " fail as the password is incorrect")

        # username is incorrect, password is correct
        assert not verify_password(nonexistent_user, test_password, test_file), ("Password verification shall"
                                                                                 " fail as the username is incorrect")

        # username and password are incorrect
        assert not verify_password(nonexistent_user, incorrect_password, test_file), ("Password verification shall"
                                                                                      " fail as the username"
                                                                                      " and password incorrect")

        print("\nverify_password works as expected")


if __name__ == '__main__':
    unittest.main()


