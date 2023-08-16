"""Write a Python program that takes a string and returns # on both sides of each element, which are not vowels"""

def insertsym(string):
    vowels=['a','e','i','o','u']
    x=''
    for i in string:
        if i.lower() not in vowels:
            x=x+'-'+i+'-'
        else:
            x+=i
    return x
print(insertsym('Green'))
print(insertsym('White'))



