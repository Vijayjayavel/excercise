"""Write a Python program to change a given string to a newly string where
the first and last chars have been exchanged."""

def change_fl(string):
    return string[-1]+string[1:-1]+string[0]

print(change_fl('vijay'))