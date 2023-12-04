"""
Author: Yash Kapoor
Student ID: 101163338

THIS IS PROBLEM 4 D): TEST USER LOGIN PROCESS
"""

import os
import unittest
from unittest.mock import patch

import PasswordManager
from LoginInterface import login_user


class TestLogin(unittest.TestCase):
    @patch('builtins.input',
           side_effect=["test_user", "Awesome567#"])
    def test_login_user_success(self, mock_input):
        """
        Tests the successful login of the user.

        If the user enters a valid username and a valid password that
        exists in the password file, then the login is successful.

        In this case, I am simulating the login process by inputting
        appropriate values by using @patch. Once the user has logged in, I ensure the
        login_user() function has returned "access_granted".

        testing_login is set to True and testing_access_control is set to False
        since we are testing the successful login of the user.

        :param self: an instance of the test class.
        :param mock_input: Mock object for 'input' function.

        :return: None
        """
        test_file = "test_passwd.txt"
        if os.path.exists(test_file):
            # remove the test file if it already exists
            os.remove(test_file)
        PasswordManager.add_record("test_user", "Awesome567#", "Regular Client", "Active",
                                   test_file)
        result = login_user(True, False, test_file)
        assert result == "access_granted", "Access should be granted since the correct user and password are entered"
        print("Access is granted successfully upon entering the credentials that are in the system.")

    @patch('builtins.input',
           side_effect=["test_user", "incorrect_password"])
    def test_login_user_failure_incorrect_password(self, mock_input):
        """
        Tests an unsuccessful login of the user if the password
        entered for the user is incorrect.

        In this case, I am simulating the login process by using @patch
        again. However, the password for the user is incorrect (correct
        password would have been Awesome567#, but the user enters
        incorrect_password as the password, so passwords do not match). Hence,
        access_denied shall be returned by the login_user() function.

        :param self: an instance of the test class.
        :param mock_input: Mock object for 'input' function.
        :return: None
        """
        test_file = "test_passwd.txt"
        if os.path.exists(test_file):
            # remove the test file if it already exists
            os.remove(test_file)
        PasswordManager.add_record("test_user", "Awesome567#", "Regular Client", "Active",
                                   test_file)
        # login_user shall use the mocked values that I provided using @patch
        # It uses test_user as the username and incorrect_password as the password
        result = login_user(True, False, test_file)
        assert result == "access_denied", "Access should be denied since the incorrect password is entered"
        print("Access is denied upon entering the incorrect password that is not in the system.")

    @patch('builtins.input',
           side_effect=["incorrect_user", "Awesome567#"])
    def test_login_invalid_user_failure(self, mock_input):
        """
        Tests an unsuccessful login of the user if the username
        entered for the user is incorrect.

        In this case, I am simulating the login process by using @patch
        again. However, the username for the user is incorrect (correct
        username would have been test_user, but the user enters
        incorrect_user as the username, so usernames do not match). Hence,
        access_denied shall be returned by the login_user() function.

        :param self: an instance of the test class.
        :param mock_input: Mock object for 'input' function.
        :return: None
        """
        test_file = "test_passwd.txt"
        if os.path.exists(test_file):
            # remove the test file if it already exists
            os.remove(test_file)
        PasswordManager.add_record("test_user", "Awesome567#", "Regular Client", "Active",
                                   test_file)
        # login_user shall use the mocked values that I provided using @patch
        # It uses incorrect_user as the username and Awesome567# as the password
        result = login_user(True, False, test_file)
        assert result == "access_denied", "Access should be denied since the incorrect username is entered"
        print("Access is denied upon entering the incorrect username that are not in the system.")

    @patch('builtins.input', side_effect=["q"])
    def test_login_user_quit(self, mock_input):
        """
        Tests whether the user can go back to the main menu if needed.

        This method uses @patch to mock the "input" built-in function,
        so it simulates the user entering "q" to go back to the main menu.

        :param self: an instance of the test class.
        :param mock_input: Mock object for 'input' function.
        :return: None
        """
        result = login_user()
        assert result == "go_back", "We must go back to the main menu."


if __name__ == '__main__':
    unittest.main()
