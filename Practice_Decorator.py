"""
Author: Rajendhiran Easu
Date: 25 August 2026
Description: 
"""
from functools import wraps

approved_users = ["qa", "tester", "test"]


def validate_user_access(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        """This is decorator wrapper checking the user level access"""
        print("validation begin")
        usr = args[0]
        if usr in approved_users:
            print(f"valid user {usr}")
            return func(*args, **kwargs)
        else:
            print(f"invalid user: {usr}, can't proceed")
            return None

    return wrapper


@validate_user_access
def check_user_access(user: str):
    """This is used for checking the user level access"""
    print(f"User: {user} is verified successfully")
    print(f"Welcome to Dashboard")


def verify_user_access(user: str):
    """This is used for checking the user level access"""
    print(f"User: {user} is verified successfully")
    print(f"Welcome to Dashboard")


def display_deco():
    print("\n" + "*" * 40)


if __name__ == "__main__":
    ## with decorator -- annotation
    display_deco()
    check_user_access("test")
    display_deco()
    check_user_access("tesst")

    display_deco()
    print("functools.wraps helps to retain func metadata")
    print(f"Func Name: {check_user_access.__name__}")
    print(f"Func Doc: {check_user_access.__doc__}")

    # without decorator -- annotation
    # ver_user_access = validate_user_access(verify_user_access)
    # display_deco()
    # ver_user_access("test")
    # display_deco()
    # ver_user_access("test1")
    #
    # display_deco()
    # print("functools.wraps helps to retain func metadata")
    # print(f"Func Name: {ver_user_access.__name__}")
    # print(f"Func Doc: {ver_user_access.__doc__}")
