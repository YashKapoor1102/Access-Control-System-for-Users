"""
Author: Yash Kapoor
Student ID: 101163338

THIS IS PROBLEM 1 D)
"""

# access control list for Finvest Holdings' System
access_control_list = {
    "client account balance": {
        "Regular Client": ["read"],
        "Premium Client": ["read"],
        "Financial Planner": ["read"],
        "Financial Advisor": ["read"],
        "Investment Analyst": ["read"],
        "Teller": ["read"],
        "Compliance Officer": ["read"]
    },
    "investment portfolios": {
        "Regular Client": ["read"],
        "Premium Client": ["read", "write"],
        "Financial Planner": ["read", "write"],
        "Financial Advisor": ["read", "write"],
        "Investment Analyst": ["read", "write"],
        "Technical Support": ["read"],
        "Teller": ["read"],
        "Compliance Officer": ["read", "validate modifications"]
    },
    "financial advisor contact details": {
        "Regular Client": ["read"]
    },
    "financial planner contact details": {
        "Premium Client": ["read"]
    },
    "investment analyst contact details": {
        "Premium Client": ["read"]
    },
    "private consumer instruments": {
        "Financial Planner": ["read"],
        "Financial Advisor": ["read"],
        "Investment Analyst": ["read"]
    },
    "money market instruments": {
        "Financial Planner": ["read"],
        "Investment Analyst": ["read"]
    },
    "derivatives trading": {
        "Investment Analyst": ["read"]
    },
    "interest instruments": {
        "Investment Analyst": ["read"]
    },
    "client account information": {
        "Technical Support": ["read"]
    },
    "client contact details": {
        "Technical Support": ["read"]
    }
}


def has_access(role, resource, permission):
    """
    Checks if a given role has the specified permission on a resource.

    This function uses the "access_control_list" to determine the permissions
    associated with each role for each resource.

    :param role:    A string, the role of the user (e.g., Regular Client)
    :param resource:    A string, the resource to be accessed (e.g., client account balance)
    :param permission:  A string, the permission to be checked (e.g., read, write)
    :return:    A boolean, True if the role has the specified permission on the resource,
                False otherwise. If the resource specified does not exist in the access_control_list,
                then False is also returned.
    """
    resource_lower = resource.lower()
    permission_lower = permission.lower()

    if resource_lower in access_control_list:
        resource_permissions = access_control_list[resource_lower]
        if role in resource_permissions and permission_lower in resource_permissions[role]:
            print("Permission granted: The role", role, "has the permission", permission, "on", resource)
            return True
        else:
            print("Permission denied: The role", role, "does not have the permission", permission, "on", resource)
            return False
    else:
        print("Invalid resource: The resource", resource, "does not exist")
        return False




