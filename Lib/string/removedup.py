# remove duplicate character from a string

x=input('Enter the input: ')
x=[*x]
y=[]
for i in x:
    if i not in y:
        y.append(i)
y=''.join(y)
print(y)
