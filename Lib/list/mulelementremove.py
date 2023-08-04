# To remove multiple element from a list

n=int(input('Enter the number of inputs: '))
list=[input("enter the inputs: ") for i in range(1,n+1)]

unique=[]

for a in list:
    if a not in unique:
        unique.append(a)
    else:
        continue

for i in unique:
    print(i)