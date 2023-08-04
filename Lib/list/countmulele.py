# to count multiple element

n=int(input('Enter the number of inputs: '))
list=[input('enter the inputs: ') for i in range(1,n+1)]
print('entered list is'+str(list))
x=input('enter the input to count: ')
count=0
for i in list:
    if i==x:
        count+=1
    else:
        continue

print(f"{count} times '{x}' appeared in the list.")