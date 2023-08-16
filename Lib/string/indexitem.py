''' Write a Python program to print the index of a character in a string.'''

def index_say(string):
    x=[*string]
    for index,i in enumerate(x):
        print((index,i))

print(index_say('jbhalejbhraw454'))