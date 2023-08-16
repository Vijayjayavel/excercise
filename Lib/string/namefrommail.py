""" Write a Python program to extract and display the name from a given Email address."""

def name(string):
    x=string.split('@')
    return ''.join(i for i in x[0] if i.isalpha())

print(name('Vijayjayavel64@gmail.com'))
print(name('le.gowtham14@gmail.com'))