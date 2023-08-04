#array sum
n=int(input('Enter the number of input: '))
list=[int(input('enter inputs: ')) for i in range(1,n+1)]
print(list)
'''simple way to find sum : print(sum(list))'''

sum=0
for a in list:
    sum=sum+a
print('sum of array')
print(sum)