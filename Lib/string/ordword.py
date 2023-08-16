"""Write a Python program that returns a string sorted alphabetically
by the first character of a given string of words"""

def ord_words(string):
    x=string.split()
    return ' '.join(sorted(x))

print(ord_words('an eye for an eye will make the whole world blind '))
