"""
Author: Rajendhiran Easu
Date: 22/12/25
Description: 
"""
## Malayalam
text = str(input("Enter any words to see the char. frequency: "))
char_freq = {}
for ch in text.lower():
    char_freq[ch] = char_freq.get(ch, 0) + 1

print(char_freq)