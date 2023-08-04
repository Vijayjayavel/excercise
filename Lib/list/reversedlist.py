#reversed splited list

n=int(input('Enter the number of inputs: '))
list=[int(input("enter the inputs: ")) for i in range(1,n+1)]
step=int(input('Enter the split'))
list1=list[0:step]
list2=list[step:n+1]

list1.reverse()
print(list1)
list2.reverse()
print(list2)
list1.extend(list2)
print('output :'+str(list1))

