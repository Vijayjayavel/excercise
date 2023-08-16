""" Write a Python program to find the smallest and largest words in a given string"""

def smalllarge_word(string):
    x=string.split()
    small=x[0]
    large=x[0]
    for i in x:
        if len(i)>len(large):
            large=i
        elif len(i)<len(small):
            small=i
    return small,large

print(smalllarge_word('an eye for an eye makes the whole world blind'))

