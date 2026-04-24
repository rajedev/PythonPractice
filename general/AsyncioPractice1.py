"""
Author: Rajendhiran Easu
Date: 23/04/26
Description: Asyncio Practice with request
"""
import asyncio
from typing import List

import httpx
from pydantic import BaseModel, TypeAdapter


class User(BaseModel):
    user: str
    take_time: int


async def tell_me_joke(client: httpx.AsyncClient, request_by: str, take_time: int):
    if request_by == "muru1":
        raise Exception(f"Requested by user: {request_by} is not allowed")
    await asyncio.sleep(take_time)
    result = await client.get("https://official-joke-api.appspot.com/random_joke")
    data = result.json()
    data["author"] = request_by
    return data


async def request_for_joke():
    print("Request for joke")
    async with httpx.AsyncClient() as client:
        users_info = '[{"user":"rajesh","take_time":2},{"user":"muru1","take_time":4},{"user":"ganesh","take_time":1}]'
        adapter = TypeAdapter(List[User])
        users = adapter.validate_json(users_info)
        tasks = [tell_me_joke(client=client, request_by=u.user, take_time=u.take_time) for u in users]

        # try:
        #     result = []
        #     for task in tasks:
        #         result.append(await task)
        #     print(result)
        # except Exception as e:
        #     print(e)

        successful_tasks = []
        failure_task = []
        try:
            result = await asyncio.gather(*tasks, return_exceptions=True)
            for res in result:
                if isinstance(res, Exception):
                    failure_task.append(res)
                else:
                    successful_tasks.append(res)
            print(f"Successful Tasks: {successful_tasks} | Task Count: {len(successful_tasks)}", end="\n\n")
            print(f"Failure Tasks: {failure_task} | Task Count: {len(failure_task)}")
        except Exception as e:
            print(e)

asyncio.run(request_for_joke())
