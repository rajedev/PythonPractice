"""
Author: Rajendhiran Easu
Date: 20/12/25
Description: 
"""


class Care:
    def __init__(self, ctype: str, dept_name: str = "Production"):
        self.__care_type = ctype
        self.dept = dept_name

    def care_data_display(self):
        print(f"Type: {self.__care_type} ; Dept: {self.dept}")

    @property
    def care_type(self):
        return self.__care_type

    @care_type.setter
    def care_type(self, ctype: str):
        self.__care_type = ctype


def care_data(obj: Care):
    # obj.care_data_display()
    # print(f"Type: {obj.__care_type} ; Dept: {obj.dept}")
    # print(f"Type: {obj._Care__care_type} ; Dept: {obj.dept}") #-- Access private instance._<ClassName>__private_var
    print(f"Type: {obj.care_type} ; Dept: {obj.dept}")


care_obj = Care(ctype="Customer", dept_name="CRM")
care_data(care_obj)
care_obj.care_type = "tester"
care_obj.dept = "NA"
# core_obj = Care(ctype="Core")

care_data(care_obj)
# care_data(core_obj)
