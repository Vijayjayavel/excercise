# To find cumulative sum of

n=int(input('Enter the number of inputs: '))
list=[int(input("enter the inputs: ")) for i in range(1,n+1)]

cum_list=[]
cum=0
for i in list:
    cum=cum+i
    cum_list.append(cum)
print('cumulative sum of list: ')
print(cum_list)