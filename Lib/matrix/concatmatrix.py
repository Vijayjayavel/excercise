# concatenation of matrix vertically
n=int(input('Enter the no. of rows: '))
m=int(input('Enter the no. of columns: '))
list=[[input('Enter inputs: ')for i in range(m)]for j in range(n)]

res = []
N = 0
while N != len(list):
    temp = ''
    for idx in list:
        try:
            temp = temp + idx[N]
        except IndexError:
            pass
    res.append(temp)
    N = N + 1
print(res)