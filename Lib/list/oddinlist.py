# print odd number in a list

n=int(input('Enter number of inputs: '))
list=[int(input('Enter the inputs')) for i in range(1,n+1)]
odd=[]
for i in list:
    if i%2!=0:
        odd.append(i)
    else:
        continue
for o in odd:
    print(o)
