""" Write a Python program to strip a set of characters from a string"""

def strip_chars(str, chars):
    return "".join(c for c in str if c not in chars)

print(strip_chars("The quick brown fox jumps over the lazy dog.", "aeiou"))

