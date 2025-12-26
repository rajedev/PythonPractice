class CustomerRequest:
    dept: str = ""
    def __init__(self, cname: str, cphone: str, crequest: str, cid: int):
        self.__cust_id = cid
        self._cust_name = cname
        self.cust_contact = cphone
        self.work_request = crequest

    @property
    def cust_name(self):
        return self._cust_name

    @cust_name.setter
    def cust_name(self, name: str):
        self._cust_name = name

    @cust_name.getter
    def get_cust_name(self):
        return self._cust_name

    @property
    def cust_id(self):
        return self.__cust_id

    @cust_id.setter
    def cust_id(self, id):
        self.__cust_id = id

    @cust_id.deleter
    def cust_id(self):
        del self.__cust_id

    @classmethod
    def assign_work(cls, department:str):
        cls.dept = department

    @staticmethod
    def user_status(obj):
        print(f"User's id: {obj.__cust_id}")


crequest1 = CustomerRequest("Rajeevan", "9876543210", "Leaking pipe in kitchen", cid=1242)
crequest1.assign_work("Manuf.")

print(crequest1.cust_id)
crequest1.cust_id = 34
print(crequest1.cust_id)

# deleting the variable
# del crequest1.cust_id
#crequest1.cust_name="tester"

# Name mangling
print(crequest1._CustomerRequest__cust_id)
crequest1._CustomerRequest__cust_id = 10
print(crequest1._CustomerRequest__cust_id)

print(crequest1.dept)
print(crequest1.cust_name)
print(crequest1.dept)
print(crequest1.get_cust_name)
print(crequest1.cust_id)
CustomerRequest.user_status(crequest1)

# crequest1.cust_name = "Ragu"
# print(crequest1.cust_name)
# crequest1.cust_name = "Rajeevan"
# print(crequest1.cust_name)
