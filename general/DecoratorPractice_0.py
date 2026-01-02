"""
Author: Rajendhiran Easu
Date: 02/01/26
Description: 
"""
from functools import wraps

def log_for_home_matches(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f" {"*" * 5} Home Match Series {"*" * 5} ")
        call = func(*args, **kwargs)
        print(f"Sponsor by: Respective State Govt.")
        return call

    return wrapper


def log_for_away_matches(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f" {"#" * 5} Away Match Series {"#" * 5} ")
        call = func(*args, **kwargs)
        print(f"Sponsor by: Respective Hosting Country")
        return call

    return wrapper

def log_for_ipl_matches(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f" {"#" * 5} IPL Series {"#" * 5} ")
        call = func(*args, **kwargs)
        print(f"Sponsor by: Respective Franchises")
        return call

    return wrapper


@log_for_home_matches
def test_match(head_coach_by: str):
    print(F"this is test match team ; head coach by: {head_coach_by}")


@log_for_away_matches
def odi_match(head_coach_by: str):
    print(F"this is limited over match - 50-50 ; coached by: {head_coach_by}")

@log_for_ipl_matches
@log_for_away_matches
def t20_match(head_coach_by: str):
    print(F"this is limited over edition - 20-20 ; coaching head by: {head_coach_by}")

test_match("Ravi")
print()
odi_match("Lakshman")
print()
t20_match("Dravid")
