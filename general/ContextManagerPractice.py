"""
Author: Rajendhiran Easu
Date: 04/01/26
Description: 
"""

from enum import Enum


class OverDraftType(Enum):
    REPUTATION = 1,
    BUSINESS = 2,


class BankOverDraft:

    def __init__(self, od_type_: OverDraftType = None):
        self.overdraft_type = od_type_

    def __enter__(self):
        print("$" * 15 + " Overdraft Limit " +"$" * 15)
        if self.overdraft_type is None:
            self.overdraft_type = OverDraftType.BUSINESS

        if self.overdraft_type == OverDraftType.REPUTATION:
            return 1_00_000
        elif self.overdraft_type == OverDraftType.BUSINESS:
            return 2_00_000
        else:
            return 50_000

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("$" * 15 + " Over draft type Reset " +"$" * 15)
        self.overdraft_type = None
        print()


bank_od = BankOverDraft(od_type_=OverDraftType.BUSINESS)
print(bank_od.overdraft_type)

with BankOverDraft(od_type_=OverDraftType.REPUTATION) as bod:
    od_amt = bod
    print(od_amt)

print(bank_od.overdraft_type)

# from contextlib import contextmanager
#
#
# @contextmanager
# def check_bank_od(overdraft_type: OverDraftType):
#     print("$" * 15 + " Overdraft Limit " + "$" * 15)
#     if overdraft_type is None:
#         overdraft_type = OverDraftType.BUSINESS
#
#     if overdraft_type == OverDraftType.REPUTATION:
#         od_amt = 1_00_000
#     elif overdraft_type == OverDraftType.BUSINESS:
#         od_amt = 2_00_000
#     else:
#         od_amt = 50_000
#     yield od_amt
#     print("$" * 15 + " Overdraft Limit Announced " + "$" * 15)
#
# with check_bank_od(OverDraftType.REPUTATION) as od:
#     print(od)