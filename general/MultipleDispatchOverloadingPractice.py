"""
Author: Rajendhiran Easu
Date: 05/01/26
Description: 
"""

from multipledispatch import dispatch


class OverloadingPractice:
    def __init__(self):
        self.zipcode = None
        self.uname = "def_sys"
        self.a_value, self.b_value, self.c_value = 0, 0, 0

    @dispatch(int, int, int)
    def set_values(self, aValue: int, bValue: int, cValue: int):
        self.a_value = aValue
        self.b_value = bValue
        self.c_value = cValue

    @dispatch(str, int, str)
    def set_values(self, uname: str, aValue: int, zipcode: str):
        self.a_value = aValue
        self.uname = uname
        self.zipcode = zipcode

    @dispatch(int)
    def set_values(self, cValue: int):
        self.c_value = cValue

    def display(self):
        print(self.a_value, self.b_value, self.c_value)
        print(self.uname, self.zipcode)


olp = OverloadingPractice()
olp.set_values(1, 2, 3)
olp.display()
olp.set_values(10, 20, 30)
olp.display()
olp.set_values(40)
olp.display()
olp.set_values("usr1", 50, "605001")
olp.display()
