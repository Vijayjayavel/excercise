# addition of two or more matrix
"""n=[int(input('Enter the matrix dimensions : ')) for i in range(0,2)]
print("give the inputs with space inbetween")
list=[[0]*n[1]]*n[0]
print(list)


for i in range(0,n[0]):
    for j in range(0,n[1]):
        print(str(i) + " " + str(j))
        list[i][j]=int(input())

        print(list)"""


n = int(input('Enter the num of rows: '))
m=int(input('Enter the num of column: '))


list1=[[int(input('Enter input of 1st matrix: ')) for j in range(m)]for i in range(n)]
print(list1)

list2=[[int(input('Enter input of 2nd matrix: ')) for j in range(m)]for i in range(n)]
print(list2)
re=[[0 for j in range(m)]for i in range(n)]
for i in range(n):
    for j in range(len(list1[0])):
        re[i][j]=list1[i][j]+list2[i][j]
print(re)
