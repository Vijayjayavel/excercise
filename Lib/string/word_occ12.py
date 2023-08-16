""" Write a Python program to count the occurrences of each word in a given sentence."""

def word_occ(string):
    x=string.split()
    return {key:x.count(key) for key in x}
print(word_occ('the quick brown fox jumps over the lazy dog.'))