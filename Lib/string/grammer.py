"""Write a Python program to add 'ing' at the end of a given string (length should be at least 3).
If the given string already ends with 'ing', add 'ly' instead.
If the string length of the given string is less than 3, leave it unchanged"""

def grammer(string):

    if len(string)<3:
        return string
    else:
        if string.endswith('ing'):
            x=string+'ly'
        else:
            x=string+'ing'
    return x

print(grammer('going'))
print(grammer('come'))
print(grammer('go'))