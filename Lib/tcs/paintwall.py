# painting wall

n=int(input('Enter the numner of interior wall: '))
m=int(input('Enter the numner of interior wall: '))

a=sum([float(input('enter surface area of interior wall: ')) for i in range(n)])
b=sum([float(input('enter surface area of exterior wall: ')) for i in range(m)])

x=a*18
y=b*12

z=x+y

print('the total cost to paint the wall: ')
print(z)
