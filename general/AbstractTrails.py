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

    def test22(self):
        pass


class guru(abstractTrails):

    # def __init__(self):
    #     self.__test1 = "UPI"

    def __init__(self):
        self.__test1 = None

    def test(self):
        super().test()
        print("Guru test abstract")

    @property
    def test1(self):
        return self.__test1

    @test1.setter
    def test1(self, values: str):
        self.__test1 = values

    def display(self):
        print("Guru Print", self.__test1)

g = guru()
g.display()
g.test()
g.test1="TES"
g.display()
print(g.test1)
print(g.test1)
print(g._guru__test1)
g.test1 = "ada"
print(g.test1)


class inher1:
    def inher1_method(self):
        print("Parent")


class inher2(inher1):
    def inher1_method(self):
        super().inher1_method()
        print("Child")

# in2 = inher2()
# in2.inher1_method()
