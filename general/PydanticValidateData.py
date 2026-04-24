"""
Author: Rajendhiran Easu
Date: 24/04/26
Description:
"""

from typing import List

from pydantic import BaseModel, TypeAdapter

user_obj = {"user": "rajesh", "take_time": 2}
user_json_obj = '{"user": "rajesh", "take_time": 2}'
users_array_obj = [{"user": "rajesh", "take_time": 2}, {"user": "muru1", "take_time": 4},
                   {"user": "ganesh", "take_time": 1}]
users_json_array = '[{"user":"rajesh","take_time":2},{"user":"muru1","take_time":4},{"user":"ganesh","take_time":1}]'


class UserInfo(BaseModel):
    user: str
    take_time: int


u_object = UserInfo.model_validate(user_obj)
u_object_from_json = UserInfo.model_validate_json(user_json_obj)

print(u_object.user, u_object.take_time)
print(u_object_from_json.user, u_object_from_json.take_time)

obj_adapter = TypeAdapter(UserInfo)

u_object_from_adapter = obj_adapter.validate_python(u_object)
u_object_json_from_adapter = obj_adapter.validate_json(user_json_obj)

print(u_object_json_from_adapter.user, u_object_json_from_adapter.take_time)
print(u_object_from_adapter.user, u_object_from_adapter.take_time)

array_adapter = TypeAdapter(List[UserInfo])

u_array_from_adapter = array_adapter.validate_python(users_array_obj)
print(u_array_from_adapter[1].user, u_array_from_adapter[1].take_time)

u_json_array_from_adapter: List[UserInfo] = array_adapter.validate_json(users_json_array)
print(u_json_array_from_adapter[1].user, u_json_array_from_adapter[1].take_time)
