# counting number of people present in hall

n=int(input('Enter the number of input: '))

E=[int(input(f'Enter the number of people entering at {i} hour: ')) for i in range(1,n+1)]
L=[int(input(f'Enter the number of people leaving at {i} hour: ')) for i in range(1,n+1)]

present=0
maxi=[]
i=0
while i<n:
    present=present+E[i]-L[i]
    maxi.append(present)
    print(f'People present in the {i+1} hour is {present}')
    i+=1
print(f'Maximum number of people present at the ship at an instance is {max(maxi)}')