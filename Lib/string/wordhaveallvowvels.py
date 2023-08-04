# code to accept a word which a all vowvels

x=input('Enter a words: ')

x=x.lower()
y=['a','e','i','o','u']

z=[]

for i in x:
    if i in y and i not in z:
        z.append(i)
    else:pass

if len(z)==len(y):
    print('Accepted')
else:
    print('Not accepted')