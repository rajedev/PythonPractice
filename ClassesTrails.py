class CustomerRequest:
    def __init__(self, cname: str, cphone: str, crequest: str):
        self._cust_name = cname
        self.cust_contact = cphone
        self.work_request = crequest

    @property
    def cust_name(self):
        return self._cust_name

    @cust_name.setter
    def cust_name(self, name: str):
        self._cust_name = name


crequest1 = CustomerRequest("Rajeevan", "9876543210", "Leaking pipe in kitchen")
print(crequest1.cust_name)

crequest1.cust_name = "Ragu"
crequest1.cust_name = "Rajeevan"
print(crequest1.cust_name)
