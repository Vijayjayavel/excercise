# remove multiple elements from a list

n=int(input('Enter the number of inputs: '))
list=[int(input("enter the inputs: ")) for i in range(n)]
flag=1
while flag:
    m=int(input('Enter the number of inputs you have to remove: '))
    if m>n or m<0:
        print('enter a valid input.')
    else:
        flag=0
list1=[int(input("enter the inputs to remove: ")) for i in range(m)]

for i in list:
    if i in list1:
        list.remove(i)
print(list)
