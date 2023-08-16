"""Write a Python program to capitalize the first and last letters of each word in a given string."""

def firlast_cap(string):
    x=string.title()[:-1]+string[-1].upper()
    return x
print(firlast_cap('vijay'))

a='lets make it new as possible'
print(' '.join(list(map(firlast_cap,a.split()))))