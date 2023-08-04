# to find the sum of digits of elements in a list

n=int(input('Enter the number of inputs: '))
list=[int(input("enter the inputs: ")) for i in range(1,n+1)]

list1=[]
for i in list:
    sum=0
    for j in str(i):
        sum+=int(j)
    list1.append(sum)
print('list of sum of digits of list '+str(list1))
