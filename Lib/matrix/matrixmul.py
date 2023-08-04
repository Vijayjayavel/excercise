# matrix multiplication
n = int(input('Enter the num of rows: '))
m =int(input('Enter the num of column: '))

A=[[int(input('Enter input of 1st matrix: ')) for j in range(m)]for i in range(n)]
print(A)

B=[[int(input('Enter input of 2nd matrix: ')) for j in range(m)]for i in range(n)]
print(B)
multiResult = [[0, 0],
               [0, 0]]
# Using nested for loop method on A & B matrix
for m in range(len(A)):
   for n in range(len(B[0])):
          for o in range(len(B)):
               multiResult[m][n] += A[m][o] * B[o][n] # Storing multiplication result in empty matrix
# Printing multiplication result in the output
print("The multiplication result of matrix A and B is: ")
for res in multiResult:
   print(res)