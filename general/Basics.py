# from basics.Fibonacci import fibonacci_simple1

# fib = fibo.fibonacci_simple1(10)
# print(f"Fibonacci series: {fibo.fibonacci_simple1(int(input("Max. No. of Fibonacci: ")))}")
# print(f"No. of Vowels in the word: {vowel.vowels_count1(str(input("Enter any word:")))}")

"""print("God knows All", "Trust in God")
print("UserId:", 123, "Username: Ragavan", "Age:", 23, sep="|")

uValue = "123"
vValue = "12.52"
sValue = 13.5614

print(type(uValue))
print(int(uValue))
print(type(vValue))
print(int(float(vValue)))
print(f"{float(vValue):.1f}")
print(float(vValue))
print(f"{sValue:.2f}")
print("{:.1f}".format(sValue))

hasValue = True
print(type(hasValue))
print(int(hasValue))
print(float(hasValue))

complexInput = 3 + 10j
print(complexInput)
"""
import random

from annotated_types import MinLen, MaxLen

userData = {
    "users": [{
        "username": "Ragu",
        "age": 23
    },
        {
            "username": "Raju",
            "age": 15
        }]
}
# print(user)
'''for u in user.get("users"):
    age = u.get("age")
    username = u.get("username")
    if age >=18:
        print(f"{username} is Right to caste vote")
    else:
        print(f"{username} pls wait for another {18-age} years to caste vote")
'''

'''def check_vote_eligibility(user_list: dict) -> list:
    voters_msg = []
    for user in user_list.get("users"):
        age = user["age"]
        msg = user['username']
        if age >= 18:
            msg += " is Right to caste vote"
        else:
            msg += f" pls wait for another {18 - age} years to caste vote"
        voters_msg.append(msg)
    return voters_msg


print(check_vote_eligibility(userData))'''

'''def check_voter_eligibility(user_obj) -> bool:
    age = user_obj['age']
    return True if age >= 18 else False


for user in userData["users"]:
    if check_voter_eligibility(user):
        msg = f"{user['username']} is Right to caste vote"
    else:
        msg = f"{user['username']} pls wait for another {18 - user['age']} years to caste vote"
    print(msg)'''

'''hasContinue = True
while hasContinue:
    userInput = input("Enter your YoB: (/bye to exit):")
    if userInput == "/bye":
        hasContinue = False
        msg = "Thank you, visit again"
    elif userInput.isdigit():
        user_value = int(userInput)
        msg = f"Your Age is: {2025 - user_value} years | You are {"Eligible" if (2025 - user_value) >= 18 else "Not Eligible"} to caste vote"
    else:
        msg = "Invalid Input, Please enter valid year of birth"
    print(msg)
'''

'''xName = input("Enter your payment option:")
match xName:
    case "/bye":
        print("Thank you, visit again")
    case "Cash":
        print("You selected Cash payment option")
    case "CC":
        print("You selected Credit Card payment option")
    case "UPI":
        print("You selected UPI payment option")
    case _:
        print("Invalid payment option, Please select valid payment option")
'''

# input_str = "Jaque Kallis"
# print(f"{input_str[::-1]}")

"""uValue = 10
vValue = 3

print(uValue%3)
print(uValue//3)

rValue = 20
qValue = 30
data1 = int(input("Enter a value: "))
if data1>=20:
    data="Test"
else:
    data = "tester"

print(data)
print(f"output = {rValue + qValue}") """


def test_return() -> tuple:
    age = int(input("Enter a Age: "))
    name = input("Enter a name:")
    designation = input("Enter a designation:")
    return age, name, designation


# data = test_return()
# print(data[0])
# print(data[1])
# print(data[2])

# a, n, desi = test_return()
# print(type(a))
# print(n)
# print(desi)

crm = {
    "user": [{
        "fname": "Rajesh",
        "lname": "E",
        "sports": ["Cricket", "Tennis"]
    }, {
        "fname": "Rajeevan",
        "lname": "G",
        "sports": ["Hockey", "Chess"]
    }]
}

values = crm.get("user", "NA").append({
    "ename": "Rajesh",
    "eid": "E",
    "erole": ["CTO", "Tech."]
})

# values1 = crm.get("user1", "NA")
# print(values)
# print(values1)
# keys = crm.get("user")[0].keys()
# for k in keys:
#    print(crm.get("user")[0].get(k))

# for k,v in crm.items():
#     print(f"{k}:{v}")


# num = 10
# for value in range(2, num):
#     print(value)
#     if value == 3:
#         break
# else:
#     print("for end")

# is_even = "value is even" if int(input("Enter a number: ")) % 2 == 0 else "value is not even"
# print(is_even)

# def add_supported_country(countries: list) -> list:
#     countries[1] = "India"
#     countries[3][0] = "Brisbane"
#     return countries
#
#
# supported_country_list = ["France", "Germany", "Australia", ["sydney", "melbourne"]]
# add_support_country = add_supported_country(supported_country_list.copy())
# add_support_country_deep = add_supported_country(copy.deepcopy(supported_country_list))
# add_support_country_deep.append("Brazil")
# print(f"Old List: {supported_country_list}")
# print(f"New List: {add_support_country}")
# print(f"New List Deep: {add_support_country_deep}")

# def test_fun(a: int, b: int) -> int:
#     return a + b
#
# print(test_fun(10, 30))
# print(test_fun(10,"teest")) # TypeError

# s:set={"12","rt","tr","rt","12",13}
# s.add("4234")
# print(s)
# u: tuple = ("testere","tes")
# print(u[1])
# y: dict = {"key1": "value1", "key2": "value2", "key3": {"key3_1": "value_3_1"}, "key4": [{"keyA4_1": "valueA4_1"}, ]}
# x: list = ["tet", ["teste", "tes"], 12, 1.24, True, False, y]
# print(x[6])
# print(y)
# print(type(s))
# print(type(u))
# print(type(y))
# print(type(x))

# def args_method(*user_args, **profile_args):
#     print(f"User Args: {user_args} ; Type: {type(user_args)}")
#     print(f"Profile Args: {profile_args} ; Type: {type(profile_args)}")
#     list_of_vowels = [v for v in user_args if v in "AEIOUaeiou"]
#     print(list_of_vowels)
#
# args_method("A","b","u","d", id="124", name="Ragavan",age = 34)

# tup = (10,20,30,40)
# *x,_,z =tup
# print(x,z,sep=";")

xValues = []
for x in range(10):
    xValues.append(x)

yValues = [v for v in range(10)]

# print(xValues)
# print(yValues)

# even = [en for en in range(1, 51) if en % 2 == 0]
# print(even)

# matrix = [[10, 20, 30], [40, 50, 60], [70, 80, 90]]
# print(matrix)
#
# flat_list = []
# for i_row in matrix:
#     for i_num in i_row:
#         flat_list.append(i_num)
#
# print(flat_list)
# flat_list_1 = [i_num for i_row in matrix for i_num in i_row]
# print(flat_list_1)

# def is_odd_or_even(value:int):
#      ans = "even" if value % 2 == 0 else "odd"
#      return f"{value} is " + ans
#     # if value %2 ==0:
#     #     return " is even"
#     # else:
#     #     return " is odd"
#
# odd_even_dict = {value: "is even" if value % 2 == 0 else "is odd" for value in range(1, 51)}
# odd_even_list = [f"{value} is even" if value % 2 == 0 else f"{value} is odd" for value in range(1, 51)]
# odd_even_list_1 = [is_odd_or_even(value) for value in range(1, 51)]
# even = [en for en in range(1, 51) if en % 2 == 0]
# #print(odd_even_dict)
# print(f"{odd_even_list_1=}")
# #print(even)

# def list_fun(ldata=None)->list:
#     if ldata is None:
#         ldata = []
#     print(ldata)
#     #if not ldata is None:
#     ldata.append(100)
#     return ldata
#
# print(list_fun([20]))
# print(list_fun([30,40]))
# print(list_fun())
# print(list_fun())

# xvalue: int | None = None
# yvalue: int | None = 32
#
# print("Yes" if xvalue is None else "No")
# print("Yes" if yvalue is None else "No")

from typing import Annotated, Literal

from pydantic import Field, BaseModel, ConfigDict, AfterValidator

skill_validation_annotation = Annotated[str, Field(min_length=3, max_length=5)]


def validation(v: str) -> str:
    if v == "username":
        return f"u{random.randint(1, 99)}"
    return v


class Userv1(BaseModel):
    model_config = ConfigDict(validate_assignment=True, validate_by_name=True)
    # u_name: Annotated[str, Field(min_length=3, max_length=5), AfterValidator(validation)]
    u_name: Annotated[str, Field(alias="username"), MinLen(5), MaxLen(12), AfterValidator(validation)]
    u_age: Annotated[int, Field(ge=15, le=60)] = 15
    u_dept: Literal["prod", "mark.", "fin."] = "fin."
    e_skills: Annotated[list[skill_validation_annotation], Field(default_factory=list, min_length=3, max_length=10)]


# @dataclass()
# class Employee:
#     e_name: str
#     e_dept: Literal["Prod", "Marketing", "Finance"] = "Prod"


# e1 = Employee("Iyyanar", "Manuf.")
# print(e1)
# try:
#     user1 = Userv1(u_name="username1", u_dept="prod", e_skills=["t2412", "t" * 5, "h" * 3])
#     print(user1)
#     user_dict = user1.model_dump(by_alias=True)
#
#     # print(user_dict)
#     # user2 = Userv1(**user_dict)
#     # print(user2)
#
#     user_json = user1.model_dump_json()
#     print(user_json)
#     user3 = Userv1.model_validate_json(user_json)
#     print(user3)
#     # user1.u_age = 12
#     # print(user1)
# except Exception as e:
#     print(e)

# try:
#     user2 = Userv1(u_name="ggg" * 3, u_age=18)
#     print(user2)
# except Exception as e:
#     print(e)

# print(user.model_dump())
# print(user.model_dump_json(indent=2))

import os
from dotenv import load_dotenv, find_dotenv

local_env_path = find_dotenv()
print(local_env_path)
# load_dotenv('../.env')
load_dotenv(override=True)

API_KEY = os.getenv("OPEN_API_KEY")
USERNAME = os.getenv("USERNAME")
PASSWORD = os.getenv("PWD")
print(f"API Key: {API_KEY} ; Username: {USERNAME} ; Password: {PASSWORD}")
print(os.getenv("USER_NOTE"))
