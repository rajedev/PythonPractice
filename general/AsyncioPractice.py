"""
Author: Rajendhiran Easu
Date: 06/01/26
Description:
"""

import asyncio
from logging import exception


async def test_async():
    print("Welcome to test async")
    await asyncio.sleep(3)
    print("waiting at test async")
    print("test async ended")


async def test_async_return(delay: int):
    if 4 == delay:
        raise "Delay with 4 sec. is not executed"
    else:
        print(F"welcome to test async with {delay} second(s)")
        await asyncio.sleep(delay)
        print(f"waiting at test async with {delay} second(s)")
        print(f"test async finished with {delay} second(s) delay")
        return {f"msg_delay_by_{delay}s": f"test async finished in {delay} seconds"}


# asyncio.run(test_async())

async def execute():
    # await test_async()

    #cancel all jobs on exception
    try:
        coroutines = [test_async_return(4), test_async_return(3), test_async_return(1)]
        tasks = await asyncio.gather(*coroutines, return_exceptions=False)
        response = tasks
        print(response)
    except Exception as e:
        print(e)

    # try:
    #     async with asyncio.TaskGroup() as tg:
    #         task1 = tg.create_task(test_async_return(4))
    #         task2 = tg.create_task(test_async_return(2))
    #         task3 = tg.create_task(test_async_return(3))
    #
    #     res = [task1.result(), task2.result(), task3.result()]
    #     print(res)
    # except *ExceptionGroup as e:
    #     print(e)

    # task2 = asyncio.create_task(test_async_return(2))
    # task3 = asyncio.create_task(test_async_return(3))
    # task1 = asyncio.create_task(test_async_return(1))
    #
    # result: dict[str, str] = {}
    # result.update(await task2)
    # result.update(await task3)
    # result.update(await task1)
    # print(result)


asyncio.run(execute())
