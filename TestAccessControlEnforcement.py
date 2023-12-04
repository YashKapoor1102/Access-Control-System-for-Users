"""
Author: Yash Kapoor
Student ID: 101163338

THIS IS PROBLEM 4 D): TEST ACCESS CONTROL ENFORCEMENT MECHANISM
"""

import io
import os
import sys
import unittest
from unittest.mock import patch

import PasswordManager
from LoginInterface import login_user


class TestAccessControlEnforcement(unittest.TestCase):
    def setUp(self):
        """
        Prepares for a test by redirecting the
        output to a temporary stream.
        :return: None
        """
        # Save the original stdout
        self.original_stdout = sys.stdout
        # Create StringIO object
        self.captured_output = io.StringIO()
        # Redirect stdout
        sys.stdout = self.captured_output

    def tearDown(self):
        """
        Cleans up after a test by restoring the original
        standard output.
        :return: None
        """
        sys.stdout = self.original_stdout

    @patch('builtins.input',
           side_effect=["test_user", "Awesome567#"])
    def test_access_control_enforcement_success(self, mock_input):
        """
        Tests successful access control enforcement for a user.

        This method uses @patch to mock the inputs entered by
        the user. Specifically, it simulates the login process
        by inputting a username called "test_user" and the
        test password "Awesome567#" (this user is added
        to the password file first before calling the login function).
        After the user is logged in, this test checks if the output
        that is displayed to the user after a successful login (captured output)
        is equal to the output that must be displayed to the user when they
        log in (expected output).

        :param self: an instance of the test class
        :param mock_input: Mock object for 'input' function.
        :return: None
        """
        test_file = "test_passwd.txt"
        test_user = "test_user"
        test_role = "Premium Client"
        if os.path.exists(test_file):
            # remove the test file if it already exists
            os.remove(test_file)

        # adding user to the password file, so when the user logs in,
        # the credentials can be verified successfully.
        PasswordManager.add_record(test_user, "Awesome567#", test_role, "Active",
                                   test_file)
        # the output that must be displayed to the user when they log in
        expected_output = ("\n\nLogin: \n"
                           "ACCESS GRANTED!\n"
                           "\nUser ID: test_user\nRole: Premium Client\n\n"
                           "List of resources in the system: \n"
                           "client account balance\n"
                           "investment portfolios\n"
                           "financial advisor contact details\n"
                           "financial planner contact details\n"
                           "investment analyst contact details\n"
                           "private consumer instruments\n"
                           "money market instruments\n"
                           "derivatives trading\n"
                           "interest instruments\n"
                           "client account information\n"
                           "client contact details\n"
                           "\nAccess Control List for Premium Client:\n"
                           "client account balance: read\n"
                           "investment portfolios: read/write\n"
                           "financial planner contact details: read\n"
                           "investment analyst contact details: read\n")

        login_user(False, True, test_file)
        # Check the captured output against the expected output
        self.assertEqual(self.captured_output.getvalue().strip(), expected_output.strip(),
                         "Output did not match expected value.")
        print("The list of resources along with the access control list is correct for "
              + test_user + " with the role " + test_role)


if __name__ == '__main__':
    unittest.main()
