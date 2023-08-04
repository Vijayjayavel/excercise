# TO find kth column of matrix

n1 = int(input('Enter the num of rows: '))
n2=int(input('Enter the num of column: '))
m=[[int(input('Enter input of 1st matrix: ')) for j in range(n2)]for i in range(n1)]

flag=1
while flag:
    c=int(input('Enter the column no. to print: '))
    if c>n2+1:
        print('enter a valid column no')
    else:
        flag=0

list=[]
for i in range(len(m)):
    for j in range(len(m[0])):
        if j==c-1:
            list.append(m[i][j])

for x in list:
    print(x)

