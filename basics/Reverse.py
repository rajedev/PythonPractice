"""
Author: Rajendhiran Easu
Date: 20/09/25
Description:
"""

# Simple Version
user_value = str(584214)

#u=user_value[4:1:-2]
#print(u)
#print(user_value[::-1])



def reverse_a_number(input_value: int):
    temp_val = abs(input_value)
    reverse_value = 0
    while temp_val > 0:
        digit = temp_val % 10
        reverse_value = reverse_value * 10 + digit
        temp_val //= 10
    return -reverse_value if input_value < 0 else reverse_value


# user_val = int(input("Enter a number to reverse: "))
# print(reverse_a_number(user_val))

def reverse_a_word(input_word: str):
    temp_word = input_word
    rev_str = ""
    for ch in temp_word:
        print(f"rs: {rev_str}")
        rev_str = ch + rev_str

    print()
    rev_str1=""
    for ch in range(len(temp_word),0,-1):
        rev_str1 = rev_str1 + temp_word[ch-1]
        print(temp_word[ch-1], end="")
    print()
    print(rev_str)
    print(rev_str1)


#reverse_a_word("tester")
