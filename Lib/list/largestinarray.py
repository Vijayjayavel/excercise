# To find largest in an array

n=int(input('Enter the number of input: '))
list=[int(input('enter inputs: ')) for i in range(1,n+1)]
print(list)

'''simple way to find largest in array: print(max(list))'''

max=list[0]
for i in range(1,n):
    if list[i]>max:
        max=list[i]
print(max)