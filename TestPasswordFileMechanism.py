"""
Author: Yash Kapoor
Student ID: 101163338

THIS IS PROBLEM 2 D)
"""

import os
import unittest

import bcrypt

from PasswordManager import add_record, get_usernames, hash_password, get_all_records


class TestPasswordFileMechanism(unittest.TestCase):

    def test_get_username(self):
        """
        Tests whether usernames are retrieved from the password file
        that stores all the records successfully.

        :return: None
        """
        users = [
            ("test_user1", "test_password1", "test_role1", "active"),
            ("test_user2", "test_password2", "test_role2", "active"),
            ("test_user3", "test_password3", "test_role3", "inactive")
        ]
        test_file = "test_passwd.txt"

        if os.path.exists(test_file):
            # remove the test file if it already exists
            os.remove(test_file)

        for user in users:
            add_record(*user, test_file)

        username_list = get_usernames(test_file)

        assert users[0][0] == username_list[0], "The usernames should match"
        assert users[1][0] == username_list[1], "The usernames should match"
        assert users[2][0] == username_list[2], "The usernames should match"

        print("\nget_username() works as expected. Usernames are correctly retrieved from the passwd.txt file.")

    def test_hash_password(self):
        """
        Tests the hash_password() function.

        Three test cases:
        1. password produces hash value that is not empty
        2. hashed password matches plaintext password
        3. multiple hashed values of the same password produce different hashes

        :return: None
        """
        password = "password_test"

        # Ensure the password produces a hash value that is not empty
        hashed_password = hash_password(password)
        assert hashed_password, "The function produces an empty value for the hash."

        # Check if the hashed password matches the plaintext password
        assert bcrypt.checkpw(password.encode("utf-8"), hashed_password), \
            "The hashed password must match the plaintext password"

        # Ensure multiple hashed values of the same password produce different hashes
        hashed_password_two = hash_password(password)
        assert hashed_password != hashed_password_two

        print("\nhash_password() works as expected.")

    def test_add_record(self):
        """
        Tests whether a record is being added to the password
        file successfully (i.e., tests the add_record() function).

        It ensures all the values that are added to the password file
        are the same as the values that the user entered.

        :return: None
        """
        users = [
            ("test_user1", "test_password1", "test_role1", "active"),
            ("test_user2", "test_password2", "test_role2", "active"),
            ("test_user3", "test_password3", "test_role3", "inactive")
        ]
        test_file = "test_passwd.txt"

        if os.path.exists(test_file):
            # remove the test file if it already exists
            os.remove(test_file)

        for user in users:
            add_record(*user, test_file)

        all_records = get_all_records(test_file)

        assert len(all_records) == len(users), ("The number of records"
                                                " in the file should match"
                                                " the number of records"
                                                " that have been added")
        user_number = 0
        for record in all_records:
            expected_user = users[user_number]
            assert record["username"] == expected_user[0], "Username is incorrect since it does not match"

            # Ensuring the plaintext password matches the hashed password
            assert bcrypt.checkpw(expected_user[1].encode('utf-8'), record["hashed_password"].encode('utf-8')), "Passwords do not match"

            assert record["role"] == expected_user[2], "Role is incorrect since it does not match"
            assert record["account_status"] == expected_user[3], "Account status is incorrect since it does not match"

            user_number += 1

        print("\ntest_add_record() works as expected. Multiple records added successfully in test_passwd.txt file")


if __name__ == '__main__':
    unittest.main()


