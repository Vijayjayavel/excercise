"""Write a Python program to create a Caesar encryption"""

import string
def caeser(strings,n):
    x1=list(string.ascii_lowercase)
    x2=list(string.ascii_uppercase)
    y=[*strings]
    z=[]
    for i in strings:
        if i.islower():
            a=x1.index(i)
            b=(n+a)%26
            z.append(x1[b])
        else:
            a = x2.index(i)
            b = (n + a) % 26
            z.append(x2[b])
    return ''.join(z)

print(caeser('Vanakkam',4)) # Zereooeq (encrpted output)
