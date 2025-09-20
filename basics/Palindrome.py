"""
Author: Rajendhiran Easu
Date: 20/05/25
Description: Palindrome on word & number
"""

# Simple version - string


# word="Malayalam"
# word="Malay"
word = "121"


# is_palindrome = word.lower() == word.lower()[::-1]
# print(f"{word} is {'not ' if not is_palindrome else ''}palindrome")

# Function version - String
def is_palindrome(word_input: str) -> bool:
    in_word = word_input.lower()
    start, end = 0, len(in_word) - 1
    while start < end:
        if in_word[start] != in_word[end]:
            return False
        start += 1
        end -= 1
    return True


# user_input = input("Enter a word: ")
# print(f"{user_input} is {'not ' if not is_palindrome(user_input) else ''}palindrome")

palindrome_words = [
    "civIc",
    "lEvel",
    "radAr",
    "rotor",
    "madam",
    "refer",
    "deified",
    "repaper",
    "noon",
    "wow",
    "a",
    "aa",
    "ada",
    "bob",
    "dad",
    "eve",
    "gig",
    "huh",
    "mom",
    "pop",
    "racecar",
    "redivider",
    "detartrated",
    "rotavator",
    "Malayalam"
]


# for word in palindrome_words:
#    print(f"{word} is {'not ' if not is_palindrome(word) else ''}palindrome")

def is_palindrome_on_word(input_word: str) -> str:
    actual = input_word
    rev_word = ""
    for ch in actual:
        rev_word = ch + rev_word
    print(f"rWord: {rev_word} aWord: {actual}", sep=",")
    return actual == rev_word

# This would take time, since every character is iterated, irrespective of match or not
#for w in [wdr.lower() for wdr in palindrome_words]:
#    print(f"{w} is {'not ' if not is_palindrome_on_word(w) else ''}palindrome")


# Function version - integer
def is_palindrome_on_num(num_input: int) -> bool:
    if num_input < 0:
        return False
    actual = num_input
    reverse = 0
    while num_input > 0:
        reminder = num_input % 10
        reverse = reverse * 10 + reminder
        num_input //= 10
    return actual == reverse

# user_input = int(input("Enter a number: "))
# print(f"{user_input} is {'not ' if not is_palindrome_on_num(user_input) else ''}palindrome")
