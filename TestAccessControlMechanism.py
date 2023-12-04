"""
Author: Yash Kapoor
Student ID: 101163338

THIS IS PROBLEM 1 E)
"""

import unittest

from AccessControlSystem import has_access


class TestAccessControlMechanism(unittest.TestCase):
    def test_has_permissions(self):
        """
        Tests the access control mechanism.

        This method ensures that the has_access() method is working
        as expected. It passes various roles, resources, and permissions
        to the has_access() method, which checks if a given role has the
        specified permission on a resource.

        If a given role does not have the specified permission on a resource,
        then we are checking to see if the method called has_access() returns False.
        Otherwise, the method shall return True.

        :return: None
        """
        print("Test: Regular Client and its permissions")
        assert has_access("Regular Client", "Client Account Balance", "Read")
        assert has_access("Regular Client", "Investment Portfolios", "Read")
        assert not has_access("Regular Client", "Investment Portfolios", "Write")

        print("\nTest: Premium Client and its permissions")
        assert has_access("Premium Client", "Investment Portfolios", "Write")
        assert not has_access("Premium Client", "Private Consumer Instruments", "Read")

        print("\nTest: Financial Planner and its permissions")
        assert has_access("Financial Planner", "Private Consumer Instruments", "Read")
        assert not has_access("Financial Planner", "Contact Details", "Read")

        print("\nTest: Financial Advisor and its permissions")
        assert has_access("Financial Advisor", "Private Consumer Instruments", "Read")
        assert not has_access("Financial Advisor", "Money Market Instruments", "Read")

        print("\nTest: Investment Analyst and its permissions")
        assert has_access("Investment Analyst", "Private Consumer Instruments", "Read")
        assert not has_access("Investment Analyst", "Client Account Balance", "Write")

        print("\nTest: Technical Support and its permissions")
        assert has_access("Technical Support", "Client Account Information", "Read")
        assert not has_access("Technical Support", "Client Account Information", "Write")

        print("\nTest: Teller and its permissions")
        assert has_access("Teller", "Client Account Balance", "Read")
        assert not has_access("Teller", "Private Consumer Instruments", "Read")

        print("\nTest: Compliance Officer and its permissions")
        assert has_access("Compliance Officer", "Investment Portfolios", "Validate Modifications")
        assert not has_access("Compliance Officer", "Client Contact Details", "Read")

        print("\nTest: Ensuring an invalid role is identified")
        assert not has_access("Invalid Role", "Investment Portfolios", "Write")

        print("\nTest: Ensuring an invalid resource is identified")
        assert not has_access("Compliance Officer", "Invalid Resource", "Write")


if __name__ == '__main__':
    unittest.main()
