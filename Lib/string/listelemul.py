# multiplication of element in list

n=int(input('Enter number of inputs: '))
list=[int(input('Enter the inputs: '))for i in range(n)]

mul=1

for i in list:
    mul*=i
print('multiplication of all numbers in a list: ')

print(mul)