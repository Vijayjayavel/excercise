#subtraction of two matix
n = int(input('Enter the num of rows: '))
m=int(input('Enter the num of column: '))


list1=[[int(input('Enter input of 1st matrix: ')) for j in range(m)]for i in range(n)]
print(list1)

list2=[[int(input('Enter input of 2nd matrix: ')) for j in range(m)]for i in range(n)]
print(list2)
result = [[0 for j in range(m)]for i in range(n)]
for i in range(len(list1)):
    for j in range(len(list1[0])):
        result[i][j] = list1[i][j] - list2[i][j]

# Printing the result
print("Subtraction of two matrix")
for row in result:
    for element in row:
        print(element, end=" ")
    print()