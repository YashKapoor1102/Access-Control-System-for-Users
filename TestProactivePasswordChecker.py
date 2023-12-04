"""
Author: Yash Kapoor
Student ID: 101163338

THIS IS PROBLEM 3 D): TEST PROACTIVE PASSWORD CHECKER
"""

import unittest
from ProactivePasswordChecker import is_password_valid


class TestProactivePasswordChecker(unittest.TestCase):
    def test_is_password_valid(self):
        """
        Tests the is_password_valid() function (i.e., checks
        whether the is_password_valid() function can differentiate
        between a valid and an invalid password).

        :return: None
        """
        assert not is_password_valid("test_user", "ABC-1234"), \
            "License Plate Numbers in passwords are prohibited"
        assert not is_password_valid("test_user", "CBA5789"), \
            "License Plate Numbers in passwords are prohibited"
        assert not is_password_valid("test_user", "TESTCBA5789"), \
            "License Plate Numbers in passwords are prohibited"
        assert not is_password_valid("test_user", "05/06/2023"), \
            "Dates in passwords are prohibited"
        assert not is_password_valid("test_user", "123-456-7789"), \
            "Phone Numbers in passwords are prohibited"
        assert not is_password_valid("test_user", "Was#1234567899"), \
            "Phone Numbers in passwords are prohibited"
        assert not is_password_valid("test_user", "AwesomeDay123456#"), \
            "Password must be between 8 and 12 characters"
        assert not is_password_valid("test_user", "awesome468#"), \
            "Password must include at least one upper-case letter"
        assert not is_password_valid("test_user", "AWESOME#"), \
            "Password must include at least one lower-case letter"
        assert not is_password_valid("test_user", "awesome#"), \
            "Password must include at least one digit"
        assert not is_password_valid("test_user", "Awesome45"), \
            "Password must include at least one special character from the set: {!, @, #, $, %, ?, *}"
        assert not is_password_valid("test_user", "test_user"), \
            "Password cannot contain the username"
        assert not is_password_valid("Test_user", "test_user567$"), \
            "Password cannot contain the username"
        assert not is_password_valid("test_user", "P@ssw0rd"), \
            "Password cannot be in the common list of passwords"
        assert is_password_valid("test_user", "Awesome567#"), \
            "Password must be valid"

        print("\nis_password_valid() works as expected. All tests passed!")


if __name__ == '__main__':
    unittest.main()
