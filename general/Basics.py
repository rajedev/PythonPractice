from basics import Fibonacci as fibo, Vowels as vowel

# from basics.Fibonacci import fibonacci_simple1

fib = fibo.fibonacci_simple1(10)
print(f"Fibonacci series: {fibo.fibonacci_simple1(int(input("Max. No. of Fibonacci: ")))}")
print(f"No. of Vowels in the word: {vowel.vowels_count1(str(input("Enter any word:")))}")

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
