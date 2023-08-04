# print even numbers in a list

n=int(input('Enter number of inputs: '))
list=[int(input('Enter the inputs')) for i in range(1,n+1)]
"""even=[i for i in list if i%2==0]
print(even)""" #easy and simple way to print list
for i in list:
    if i%2==0:
        even.append(i)
    else:
        continue
for e in even:
    print(e)

