"""
Author: Rajendhiran Easu
Date: 19/12/25
Description: 
"""

from abc import ABC, abstractmethod
class abstractTrails(ABC):

    @abstractmethod
    def test(self):
        print("test abstract")


class guru(abstractTrails):

    def test(self):
        super().test()
        print("Guru test abstract")

    def display(self):
        print("Guru Print")


# g = guru()
# g.display()
# g.test()


class inher1:
    def inher1_method(self):
        print("Parent")


class inher2(inher1):
    def inher1_method(self):
        super().inher1_method()
        print("Child")


in2 = inher2()
in2.inher1_method()