# n * n matrix creatio
n=int(input('Enter square matrix dimension: '))

list=[[int(input('Enter inputs: '))for i in range(n)]for j in range(n)]

for a in list:
    print(a)