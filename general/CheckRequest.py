"""
Author: Rajendhiran Easu
Date: 20/12/25
Description: 
"""
import requests

response = requests.get("https://geo-dev1.console.fktr.io")
data = response.json()
res_code = response.status_code.real
res_content = response.content
print(f" JSON Type {type(data)}")
print(f" JSON {data}")
print(f" data - Country: {data['country']}")
print(f" data - State: {data['region']}")
print(f" type before decode {type(res_content)}")
res_content = res_content.decode()
print(f" type after decode {type(res_content)}")
print(res_code)
print(res_content)
