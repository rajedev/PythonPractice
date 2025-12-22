"""
Author: Rajendhiran Easu
Date: 22/12/25
Description: 
"""

# def no_of_vowels(s:str)->int:
#    return count for s in s


word = "Tester"


def vowels_count(w: str):
    count: int = 0
    for c in w:
        if c in "aeiou":
            count += 1
    return count


def vowels_count1(w: str):
    # return  sum(1 for c in w if c in "aeiou")
    # return  len([c for c in w if c in "aeiou"])
    return sum(c in "aeiou" for c in w.lower())


if __name__ == "main":
    print(f"No. of Vowels in the word: {vowels_count1(str(input("Enter any word:")))}")
