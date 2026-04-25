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
    return await common(client, request_by, take_time)


async def tell_me_joke_with_except(client: httpx.AsyncClient, request_by: str, take_time: int):
    try:
        return await common(client, request_by, take_time)
    except Exception as e:
        print(f"error: {e}")


async def common(client: httpx.AsyncClient, request_by: str, take_time: int):
    print(f"initialize - {request_by}")
    if request_by == "muru1":
        print(f"except - {request_by}")
        raise Exception(f"Requested by user: {request_by} is not allowed")
    print(f"process - {request_by}")
    await asyncio.sleep(take_time)
    result = await client.get("https://official-joke-api.appspot.com/random_joke")
    data = result.json()
    data["author"] = request_by
    return data


async def request_for_joke():
    print("Request for joke")
    async with httpx.AsyncClient() as client:
        users_info = '[{"user":"rajesh","take_time":2},{"user":"muru","take_time":4},{"user":"ganesh","take_time":1}]'
        adapter = TypeAdapter(List[User])
        users = adapter.validate_json(users_info)
        tasks = [tell_me_joke(client=client, request_by=u.user, take_time=u.take_time) for u in users]

        ## Multiple tasks but sequential
        # try:
        #     result = []
        #     for task in tasks:
        #         result.append(await task)
        #     print(result)
        # except Exception as e:
        #     print(e)

        ## create_task is boilerplate code -- gather will implicitly create its task.
        # task = [asyncio.create_task(tell_me_joke(client=client, request_by=u.user, take_time=u.take_time)) for u in users]
        # res = await asyncio.gather(*task, return_exceptions=True)
        # print(res)

        # task = asyncio.create_task(tell_me_joke(client=client, request_by="Kumaran", take_time=3))
        # res = await asyncio.gather(task, return_exceptions=True)
        # print(res)

        ## using gather with exceptions -- splitting the success and failure tasks
        successful_tasks = []
        failure_task = []
        result = await asyncio.gather(*tasks, return_exceptions=True)
        for res in result:
            if isinstance(res, Exception):
                failure_task.append(res)
            else:
                successful_tasks.append(res)
        print(f"Successful Tasks: {successful_tasks} | Task Count: {len(successful_tasks)}", end="\n\n")
        print(f"Failure Tasks: {failure_task} | Task Count: {len(failure_task)}")

        # # Task group allowed to add dynamic tasks, but it cancels other if any tasks fails - for that we have to handle explicit exceptions
        # async with asyncio.TaskGroup() as tg:
        #     tg_tasks = [
        #         tg.create_task(tell_me_joke_with_except(client=client, request_by=u.user, take_time=u.take_time)) for u
        #         in
        #         users]
        #     await asyncio.sleep(2)
        #     new_user = User(user="Sakthi", take_time=1)
        #     tg_tasks.append(
        #         tg.create_task(
        #             tell_me_joke_with_except(client=client, request_by=new_user.user, take_time=new_user.take_time)))
        #
        # print("Get task result - After the taskgroup block, all task execution will be completed")
        # result = [t.result() for t in tg_tasks]
        #
        # print("Display task result")
        # for output in result:
        #     print(output)


if __name__ == '__main__':
    asyncio.run(request_for_joke())
