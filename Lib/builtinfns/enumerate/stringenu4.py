# enumerate string

x=input('Enter a string input: ')

for i,j in enumerate(x):
    print(i,j)

# giving starting number
for i,j in enumerate(x,100):
    print(i,j)