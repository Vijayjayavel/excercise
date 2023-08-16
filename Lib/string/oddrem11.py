"""Write a Python program to remove characters that have odd index values in a given string."""
from functools import reduce
def odd_re(string):
    x=''
    for i in string:
        if (string.index(i))%2==0:
            x+=i
    return x
print(odd_re('abcdefghijklmnopqrstuvwxyz'))
