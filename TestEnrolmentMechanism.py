"""
Author: Yash Kapoor
Student ID: 101163338

THIS IS PROBLEM 3 D): TEST ENROLMENT MECHANISM
"""

import os
import unittest
from unittest.mock import patch

import bcrypt

import PasswordManager
from EnrolmentInterface import register_user


class TestEnrolmentMechanism(unittest.TestCase):
    @patch('builtins.input',
           side_effect=["test_user", "Awesome567#", "Awesome567#", "1"])
    def test_register_user_success(self, mock_input):
        """
        Tests the successful registration of the user.

        If the user enters a valid username (between 4 and 20 characters),
        a valid password (proactive password checker returns True),
        and chooses a valid role (inputs a number from 1 to 8), then
        the registration is successful.

        In this case, I am simulating the registration process by inputting
        appropriate values by using @patch. Once the user is registered, I ensure the
        record is being added to the designated password file (i.e., test_passwd.txt)
        correctly.

        testing is set to true since we are in the test environment.

        :param self: an instance of the test class.
        :param mock_input: Mock object for 'input' function.
        :return: None
        """
        test_file = "test_passwd.txt"
        if os.path.exists(test_file):
            # remove the test file if it already exists
            os.remove(test_file)
        register_user(test_file, testing=True)
        all_records = PasswordManager.get_all_records(test_file)
        assert len(all_records) == 1

        for record in all_records:
            assert record["username"] == "test_user", "Username is incorrect since it does not match"

            # Ensuring the plaintext password matches the hashed password
            assert bcrypt.checkpw("Awesome567#".encode('utf-8'), record["hashed_password"].encode('utf-8')), \
                "Passwords do not match"

            assert record["role"] == "Regular Client", "Role is incorrect since it does not match"
            assert record["account_status"] == "Active", "Account status is incorrect since it does not match"

        print("The user gets registered successfully with the correct information")


    @patch('builtins.input',
           side_effect=["test_user", "Awesome567#", "incorrect_confirmation", "1"])
    def test_register_user_failure_confirmation_incorrect(self, mock_input):
        """
        Tests an unsuccessful registration of the user if confirmation password
        is incorrect.

        In this case, I am simulating the registration process by using @patch
        again. However, the confirmation password is incorrect, so register_user()
        shall return password_mismatch, meaning that the record is not added
        to the password file (i.e., test_passwd.txt still does not exist since
        no new records were added).

        :param self: an instance of the test class.
        :param mock_input: Mock object for 'input' function.
        :return: None
        """
        test_file = "test_passwd.txt"
        if os.path.exists(test_file):
            # remove the test file if it already exists
            os.remove(test_file)
        result = register_user(test_file, testing=True)
        assert result == "password_mismatch", "Passwords should not match"
        assert not os.path.exists(test_file), "Test file should not exist after failed registration"
        print("The user gets notified upon entering an incorrect confirmation password")

    @patch('builtins.input',
           side_effect=["test_user", "Awesome567#", "Awesome567#", "1"])
    def test_register_existing_user_failure(self, mock_input):
        """
        Tests an unsuccessful registration of the user if username
        already exists in the password file.

        In this case, I am simulating the registration process by using @patch
        again. However, the username already exists in the password file, so register_user()
        shall return username_already_exists, meaning that the record is not added
        to the password file.

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
        # only one record exists in the file before registration
        all_records = PasswordManager.get_all_records("test_passwd.txt")
        assert len(all_records) == 1
        result = register_user(test_file, True)
        # only one record exists in the file after registration since it was unsuccessful
        assert len(all_records) == 1
        assert result == "username_already_exists", "Username should already exist"
        print("The user gets notified upon entering an existing username")

    @patch('builtins.input',
           side_effect=["test_user", "awesomeeee", "awesomeeee", "1"])
    def test_register_user_failure_weak_password(self, mock_input):
        """
        Tests an unsuccessful registration of the user if the password
        is weak.

        In this case, I am simulating the registration process by using @patch
        again. However, the password that was entered is invalid (too weak), so register_user()
        shall return password_weak, meaning that the record is not added
        to the password file.

        :param self: an instance of the test class.
        :param mock_input: Mock object for 'input' function.
        :return: None
        """
        test_file = "test_passwd.txt"
        if os.path.exists(test_file):
            # remove the test file if it already exists
            os.remove(test_file)
        result = register_user(test_file, testing=True)
        assert result == "password_weak", "Password should be invalid (weak)"
        assert not os.path.exists(test_file), "Test file should not exist after failed registration"
        print("The user gets notified upon entering a weak password")

    @patch('builtins.input',
           side_effect=["test_user", "Awesome567#", "Awesome567#", "20"])
    def test_register_user_failure_invalid_role(self, mock_input):
        """
        Tests an unsuccessful registration of the user if inputted role
        is invalid (not between 1 and 8)

        In this case, I am simulating the registration process by using @patch
        again. However, the role that was entered is invalid, so register_user()
        shall return invalid_role_number, meaning that the record is not added
        to the password file.

        :param self: an instance of the test class.
        :param mock_input: Mock object for 'input' function.
        :return: None
        """
        test_file = "test_passwd.txt"
        if os.path.exists(test_file):
            # remove the test file if it already exists
            os.remove(test_file)
        result = register_user(test_file, testing=True)
        assert result == "invalid_role_number", "Role number should be invalid"
        assert not os.path.exists(test_file), "Test file should not exist after failed registration"
        print("The user gets notified upon entering an invalid role number that is outside the range of 1-8")


    @patch('builtins.input', side_effect=["q"])
    def test_register_user_quit(self, mock_input):
        """
        Tests whether the user can go back to the main menu if needed.

        This method uses @patch to mock the "input" built-in function,
        so it simulates the user entering "q" to go back to the main menu.

        :param self: an instance of the test class.
        :param mock_input: Mock object for 'input' function.
        :return: None
        """
        result = register_user()
        assert result == "go_back", "We must go back to the main menu."


if __name__ == '__main__':
    unittest.main()
