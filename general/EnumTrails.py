from enum import Enum


class PaymentOptions(Enum):
    CREDIT_CARD = ("CC", "Credit Card Payment", 1001)
    DEBIT_CARD = 1002
    PAYPAL = 1003
    BANK_TRANSFER = 1004
    CASH = 1005
    CRYPTOCURRENCY = 1006


pay_option= PaymentOptions.CREDIT_CARD.value
print(pay_option)

class AppUserTypes(Enum):
    ADMIN = (100, "CRUD", "admin")
    SADMIN = (101, "CRU", "superadmin")
    USER = (102, "RU", "app user")
    GUEST = (103, "R", "guest user")

    def __init__(self, code: int, permissions: str, role: str):
        self.code = code
        self.permissions = permissions
        self.user_role = role


app_admin = AppUserTypes.USER
print(app_admin.user_role)
print(app_admin.code)
print(app_admin.permissions)
print(app_admin.user_role)

