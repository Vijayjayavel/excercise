# finding greater number than its previuos number

while True:
    n = int(input('Enter the number of list: '))
    if n>=1 and n<=100:
        break
    else:
        print('Enter a valid input...!')
x=[]
for i in range(0,n):
    while True:
        a=int(input('Enter the inputs: '))
        if 10000 >=a >=1:
            x.append(a)
            break
        else:
            print('Enter a valid input...!')

count=1
b=[]
max=x[0]
i=0
for i in range(0,len(x)):
    if x[i]>=max:
        max=x[i]
        b.append(x[i])
        count+=1
    else:
        max=x[i]
        continue

print(f'There are {count-2} greater than its previous number')
print(f'The greater value than its prior elements: {b[0]}')