# enumerate list elements line b line

a=[input('Enter inputs:') for i in range(int(input('how much elements: ')))]

for i,j in enumerate(a):
    print(i,j)