'Write a Python program to move spaces to the front of a given string'

def rem_space(string):
    return ''.join(i for i in string if i!=' ')
print(rem_space('Write a Python program to move spaces to the front of a given string'))