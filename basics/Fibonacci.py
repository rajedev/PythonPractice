"""
Author: Rajendhiran Easu
Date: 20/05/25
Description: fibonacci seris
"""


# Simple version
def fibonacci_simple1(no_of_values: int) -> list:
    first = 0
    second = 1
    output = [first, second]  # list()
    for _ in range(no_of_values - len(output)):
        result = first + second
        output.append(result)
        first = second
        second = result
    return output


def fibonacci_simple1_1(no_of_values):
    first = 0
    second = 1
    output = []
    for _ in range(no_of_values):
        output.append(first)
        result = first + second
        first = second
        second = result
    return output


def fibonacci_simple2(no_of_values: int):
    first = 0
    second = 1
    for _ in range(no_of_values):
        print(first, end=" ")
        temp = first + second
        first = second
        second = temp


def fibonacci_simple3(no_of_values: int):
    first = 0
    second = 1
    for _ in range(no_of_values):
        print(first, end=" ")
        first, second = second, first + second


def fibonacci_recursive(n):
    if n <= 1:
        return n
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

if __name__ == "__main__":
    # for i in range(7):
    #    print(fibonacci_recursive(i), end=" ")  # 0 1 1 2 3 5 8 13 21 34

    print(fibonacci_simple1(5))
    print(fibonacci_simple1_1(7))
    fibonacci_simple2(10)
    print()
    fibonacci_simple3(8)