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


def add_supported_country(countries: list) -> list:
    countries[0] = "Africa"
    countries[1] = "India"
    countries[3][1] = "Brisbane"
    return countries


# supported_country_list = ["France", "Germany", "Australia", ["sydney", "melbourne"]]
# add_support_country = supported_country_list.copy()
# print(f"After updating new shallow b4change: {add_support_country}")
# sha_support_country=add_supported_country(add_support_country)
# print(f"After updating new shallow {sha_support_country}")
# # add_support_country_deep = add_supported_country(copy.deepcopy(supported_country_list))
# # add_support_country_deep.append("Brazil")
# print(f"Old List: {supported_country_list}")
# #print(f"New List: {add_support_country}")
# # print(f"New List Deep: {add_support_country_deep}")

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

# import os
# from dotenv import load_dotenv, find_dotenv
#
# local_env_path = find_dotenv()
# print(local_env_path)
# # load_dotenv('../.env')
# load_dotenv(override=True)
#
# API_KEY = os.getenv("OPEN_API_KEY")
# USERNAME = os.getenv("USERNAME")
# PASSWORD = os.getenv("PWD")
# print(f"API Key: {API_KEY} ; Username: {USERNAME} ; Password: {PASSWORD}")
# print(os.getenv("USER_NOTE"))


# value1 = [[11,12,13],[14,15,16],[17,18,19]]
# value2 = value1.copy()
# #value2.append([20,21,22])
# value1[2]=[20,21,22]
# #value1[2][2]=98
# value1.append([53,35,21])
# #value1[0]=[444,42,21]
# #value2[0][2]=24
# #value1.append([20,21,22])
# #value1[0]=[222,333,444]
# print(value1)
# print(value2)

# from collections import namedtuple
#
# rgbcolor = namedtuple("rgb", ["red", "blue", "green"])
# rgb = rgbcolor(red=120, blue=180, green=None)
# rgb1 = rgbcolor(red="oneTwenty120", blue="180", green=None)
#
# print(rgb.red)
# print(rgb1.red)
# print(rgb._asdict())
# print(json.dumps(rgb._asdict(), indent=2))
# print(json.dumps(rgb1._asdict(), indent=2))
# print(rgb._replace(green=112))
# print(rgb)
# # rgb.green=24 # error
#
# from typing import NamedTuple
#
#
# class RGBColor(NamedTuple):
#     r: int
#     g: int
#     b: int
#
#
# colors = RGBColor(r=42, g=52, b=13)
# print(colors.r)
# # colors.b = 13  # error
# # print(colors.b)
# print(colors._asdict())
# print(json.dumps(colors._asdict(), indent=2))


# class ExamCenter(TypedDict, total=False):
#     center_id: Required[int]
#     center_name: str
#     center_location: ReadOnly[str]
#     center_staffs: list
#
#
# center2: ExamCenter = {'center_id1': 124, 'center_name': 'voc', 'center_staffs': ["z", "b", "c"]}
#
# #print(center2["center_id1"])
# center2["center_location"] = "Test"
# print(center2)
#
# center1 = ExamCenter(center_id=125, center_name="VOC", center_location="PY",
#                      center_staffs=["Sivam", "Anbu", "Gaya"])
#
# center1["center_name"] = "Calve college"
# print(center1)
# ce_dict = center1.items()
# # print(json.dumps(ce_dict, indent=2))

# class Stock:
#     def __init__(self, stock_id: int = 0, owner_name:str="teste"):
#         self.stock_id = stock_id
#         self.__owner_name=owner_name
#
#
# class Finance:
#
#     def __init__(self, sw_id: int, sw_name: str):
#         self._finance_sw_id: int = sw_id
#         self.finance_sw_name: str = sw_name
#
#     def _secret_protected_method(self):
#         print("I'm from protected method from finance")
#
#     @property
#     def finance_sw_id(self):
#         return self._finance_sw_id
#
#
# #class Management(Finance, Stock):
# class Management(Finance):
#
#     def __init__(self, sid: int, report_sw: str):
#         super().__init__(sw_id=sid, sw_name="Salesforce")
#         #Finance.__init__(self,sw_id=sw_id, sw_name="SAP")
#         #Stock.__init__(self,stock_id=10000)
#         self.report_sw_name = report_sw
#         #self.stock_id=1001
#
#     def __logic_loads_here(self):
#         print("management secret logics")
#
#     def triggering_logic(self, trigger:bool):
#         if trigger:
#             self._secret_protected_method()
#             self.__logic_loads_here()
#         else:
#             print("logic is not triggered")


# manage = Management(sid=121, report_sw="InHouse-Jenie")
# #manage._secret_protected_method()
# manage.triggering_logic(True)
# #print(manage._Stock__owner_name) # Name mangling bec. it is private-pesudo variable
# #print(manage.finance_sw_id, manage.report_sw_name, manage.finance_sw_name, manage.stock_id, sep=" ; ")
# fina1 = Finance(sw_id=124, sw_name="Tally")
# print(fina1.finance_sw_name)
# print(fina1.finance_sw_id)
#
# print(dir(manage))

# from string import Template
# from typing import Literal
#
# t = Template("Hi $uname, welcome to $city")
# welcome_str = t.substitute(uname="Murugan", city="Puducherry")
# print(welcome_str)

# print("Hi {}, welcome to {}".format("Muru", "Chennai"))
# print("Hi {uname}, welcome to {city}".format(uname="Kandan", city="Madurai"))
#
# LAB_DATA = Literal["x-ray", "ecg", "bp", "sugar"]
# lab_data = "eye-checkup"
#
# if lab_data not in get_args(LAB_DATA):
#     print(f"{lab_data} not exist")
# else:
#     print(f"{lab_data} test can be taken here")

# def song(lyric:str):
#     print(f"#@#@#@.... {lyric} #@#@#@....")
#
# movie = song
# del song
# movie("la..lah..laaa..lah.. ha ah")
# #song("tester.... ") # error bec. function deleted
# movie("oo..la..oo...lah..lla..laaa..lah.. ha ah")
# print(movie.__name__)

# from enum import Enum
#
#
# class SongType(Enum):
#     HERO_INTRO = 1
#     HERO_BG_SONG = 2
#     CLIMAX_BG_SONG = 3
#     VILLAN_BG_SONG = 4
#
#
# def song_lyrics(s_type: SongType) -> str:
#     # if s_type is SongType.HERO_INTRO:
#     #     return "alalla lalalal"
#     # elif s_type is SongType.HERO_BG_SONG:
#     #     return "hhahahahhaha"
#     # elif s_type is SongType.CLIMAX_BG_SONG:
#     #     return "ohhhohh ho"
#     # else:
#     #     return "uhohuhoh"
#
#     # match s_type:
#     #     case SongType.HERO_BG_SONG:
#     #         return "hhahahahhaha"
#     #     case SongType.CLIMAX_BG_SONG:
#     #         return "ohhhohh ho"
#     #     case SongType.HERO_INTRO:
#     #         return "alalla lalalal"
#     #     case _:
#     #         return "uhohuhoh"
#
#     songs: dict[SongType, str] = {
#         SongType.HERO_BG_SONG: "hhahahahhaha",
#         SongType.CLIMAX_BG_SONG: "ohhhohh ho",
#         SongType.HERO_INTRO: "alalla lalalal"
#     }
#
#     return songs.get(s_type, "uhohuhoh")
#
#
# def film(l_song):
#     situ_song: str = l_song(SongType.HERO_INTRO)
#     print(f"hero intro song: {situ_song}")
#
#
# film(song_lyrics)

# movie_list = ["Tourist_Family", "uv" ,"Eleven", "Dude","z" ,"Margon", "Parasakthi"]

# movie_list.sort()
# movie_list.sort(reverse=True)
# new_movie_list =sorted(movie_list)
# print(movie_list)
# print(new_movie_list)
# new_movie_list =sorted(movie_list, key = lambda l:max(l))
# print(new_movie_list)
# print("#" * 20)
# for s in new_movie_list:
#     print(f" {s} = max: {max(s)}")


# def unpack_fun(ex, y, z):
#     print(F"{ex=} ; {y=} ; {z=}")
#
#
# unpack_fun(ex=10, y=20, z=30)
# unpack_fun(*(89, 90, 30))
# # unpack_fun(*(89,90,30,78)) ## error no. of positional args is not matching
# unpack_fun(*[89, 90, 30])
# # unpack_fun(*[89,90,30,90,89]) ## error no. of positional args is not matching
# unpack_fun(**{"x": "2", "y": "21", "z": "42"})
# # unpack_fun(**{"x": "2", "y": "21", "z": "42","d":24}) # error due to additional keyword
# # unpack_fun(**{"xa": "2", "y": "21", "z": "42"})  # key should match the variable name

# list_value = [10, 203, 90, 84, 52]
# # print(list_value)
#
# for index in range(0, len(list_value)):
#     print(f"index: {index} ; data: {list_value[index]}")
#
# dic_value: dict = {"x": 20, "y": 290}
#
# for k, v in dic_value.items():
#     print(f"index: {k} ; data: {v}")
#
# print(range(0, len(list_value)))
#
# print(list_value[:3])    # first 3 elements
# print(list_value[3:])    # rest

cate = "hh"
is_boolean = cate in ["Spiritual", "Crime"]
print(is_boolean)


## dictionary check
sam_dict = {
    "eee":{
        "dept":{
            "student":23,
            "faculty":"21"
        },
        "metainfo":{
            "fee":220901,
            "university_code":"2EEE2342"
        }
    },
    "ece":{
        "student":1,
        "faculty":"2"
    },
    "mec":{
        "student":3,
        "faculty":"11"
    }
}
user_value ="eee" # ece / mec
if user_value in sam_dict and sam_dict[user_value]:
    data = sam_dict[user_value]
    print(data)
    is_dept = "dept" in data
    print(is_dept)
else:
    print("no value")

# if hasattr(sam_dict["eee"], "student"):
#     print(sam_dict["eee"])
# else:
#     print("no value")