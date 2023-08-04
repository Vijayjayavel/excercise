 # NOT COMPLETED YET#

# find paerking space

n=int(input('Enter number of rows: '))
m=int(input('Enter number of columns: '))

b=[]
for i in range(0,n):
    for j in range(0,m):
        while True:
            a=(int(input('Enter the input: ')))
            if a==1 or a==0:
                b.append(a)
                break
            else:
                print('Enter a valid input')
                continue

count=0
max=0
id=0
for x in range(n):
    for y in range(0,m):
        z=b[y]
        count+=z
        if count>max:
            max=count
            id=id+1
        else:
            continue

print(f'The maximum number of 1 is in row{id}')


