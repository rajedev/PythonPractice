"""
Author: Rajendhiran Easu
Date: 01/01/26
Description: Decorator Practices
"""

from functools import wraps


def add_log_for_sre(exec_fun):
    @wraps(exec_fun)
    def wrapper(*args, **kwargs):
        print(f"logged this to sre {exec_fun.__name__}")
        return exec_fun(*args, **kwargs)

    return wrapper


def add_log_on_all_execution_0(exec_func):
    @wraps(exec_func)
    def wrapper(*args, **kwargs):
        print(f"logged the method {exec_func.__name__}")
        return exec_func(*args, **kwargs)

    return wrapper


def add_log_on_all_execution(exec_func, to_log: bool):
    @wraps(exec_func)
    def wrapper(*args, **kwargs):
        if to_log:
            print(f"logged the method {exec_func.__name__}")
        return exec_func(*args, **kwargs)

    return wrapper


def add_log_on_all_execution_1(to_log: bool):
    def decorator(exec_func):
        @wraps(exec_func)
        def wrapper(*args, **kwargs):
            if to_log:
                print(f"logged the method {exec_func.__name__}")
            return exec_func(*args, **kwargs)

        return wrapper

    return decorator


# should_log: bool = True
#
# @add_log_for_sre
# @add_log_on_all_execution_1(to_log=should_log)
# def execute_invoice():
#     print("invoice executed", end="\n\n")
#
#
# @add_log_on_all_execution_1(to_log=should_log)
# def execute_receipt(dep: str = "automatic"):
#     print(f"receipt signed for {dep}", end="\n\n")
#
# @add_log_for_sre
# @add_log_on_all_execution_1(to_log=should_log)
# def execute_petty_cash_trans():
#     print("petty cash account tallied", end="\n\n")
#
# print("###" * 25)
# execute_invoice()
# execute_receipt(dep="manual")
# execute_petty_cash_trans()

# print("###" * 25)
#
# def execute_invoice():
#     print("invoice executed", end="\n\n")
#
# def execute_receipt(dep: str = "automatic"):
#     print(f"receipt signed for {dep}", end="\n\n")
#
# def execute_petty_cash_trans():
#     print("petty cash account tallied", end="\n\n")
#
# should_log: bool = True
# invoice = add_log_on_all_execution(execute_invoice, should_log)
# invoice()
# receipt = add_log_on_all_execution(execute_receipt, should_log)
# receipt()
# petty_cash = add_log_on_all_execution(execute_petty_cash_trans, should_log)
# petty_cash()

# print("###" * 25)
#
# def execute_invoice():
#     print("invoice executed", end="\n\n")
#
# def execute_receipt(dep: str = "automatic"):
#     print(f"receipt signed for {dep}", end="\n\n")
#
# def execute_petty_cash_trans():
#     print("petty cash account tallied", end="\n\n")
# should_log: bool = True
# if should_log:
#     invoice = add_log_on_all_execution_0(execute_invoice)
#     invoice()
#     receipt = add_log_on_all_execution_0(execute_receipt)
#     receipt()
#     petty_cash = add_log_on_all_execution_0(execute_petty_cash_trans)
#     petty_cash()
# else:
#     execute_invoice()
#     execute_receipt()
#     execute_petty_cash_trans()

# print("###" * 25)
# @add_log_on_all_execution_0
# def execute_invoice():
#     print("invoice executed", end="\n\n")
#
# @add_log_on_all_execution_0
# @add_log_for_sre
# def execute_receipt(dep: str = "automatic"):
#     print(f"receipt signed for {dep}", end="\n\n")
#
# @add_log_on_all_execution_0
# @add_log_for_sre
# def execute_petty_cash_trans():
#     print("petty cash account tallied", end="\n\n")
#
# execute_invoice()
# execute_receipt(dep="manual")
# execute_petty_cash_trans()