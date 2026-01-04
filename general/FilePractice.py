"""
Author: Rajendhiran Easu
Date: 03/01/26
Description: 
"""

def update_file(user_input:str):
    with open("test.txt","a") as f:
        f.write(user_input)
    # f = open("tester.txt", "a")
    # f.write("Welcome to the file \n")
    # f.close()


if __name__ == "__main__":
    update_file("test input1 \n")
    update_file("trail input2 \n")
    update_file("all reals input \n")
