"""
Author: Rajendhiran Easu
Date: 05/01/26
Description: 
"""
from functools import singledispatchmethod


class OverloadPractice1:

    def __init__(self):
        self.uname = "sys"
        self.a_value = 0

    @singledispatchmethod
    def set_values(self, value):
        raise NotImplementedError

    # @set_values.register
    # def _(self, value:int, value2:int):
    #     self.a_value=value
    #     self.b_value=value2

    @set_values.register
    def _(self, value: int):
        self.a_value = value

    @set_values.register
    def _(self, s: str):
        self.uname = s


olp = OverloadPractice1()
print(olp.uname)
olp.set_values("usr")
print(olp.uname)
olp.set_values(44)
print(olp.a_value)
