"""Write a Python program to count characters at the same position in a given string
(lower and uppercase characters) as in the English alphabet."""

import string

low=list(string.ascii_lowercase)
upp=list(string.ascii_uppercase)

def count_chrmatch(string):
    x=[*string]
    count=0
    for i in string:
        if i.isupper()==True:
            if upp.index(i)==x.index(i):
                count+=1
        elif i.islower()==True:
            if low.index(i)==x.index(i):
                count+=1
    return count

print(count_chrmatch('ABcdefjhgajjs'))
