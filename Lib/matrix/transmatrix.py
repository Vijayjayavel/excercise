# find the transporse of a matrix

n1 = int(input('Enter the num of rows: '))
n2=int(input('Enter the num of column: '))
m=[[int(input('Enter input of 1st matrix: ')) for j in range(n2)]for i in range(n1)]
for row in m :
    print(row)
rez = [[m[j][i] for j in range(len(m))] for i in range(len(m[0]))]
print(rez)