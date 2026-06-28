"""
Author: Rajendhiran Easu
Date: 04/05/26
Description: 
"""
import requests
from requests import request


def test_1():
    print("Tester")

def test_2():
    print("testing1")

if __name__ == "__main__":
    #test_1()
    #is_x_flag = True
    #is_y_flag = False
    # data = {'name': 'Alice', 'age': 30, 'city': 'NYC'}
    # for key in data:
    #     print(key)

    #flag = not (is_y_flag or is_y_flag)
    #print(f"Flag value: {flag}")
    response = requests.get("http://ip-api.com/json?fields=countryCode,region")
    print(response.content)