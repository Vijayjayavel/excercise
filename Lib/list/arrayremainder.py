# remainder of array elements multiplication

n=int(input('enter the number of inputs : '))
arr=[int(input('enter the inputs: ')) for i in range(1,n+1)]

mul=1

for i in arr:
    mul=mul*i

print('the multiplication of the elements : '+str(mul))
# number you want use divisor
m=int(input('enter a number for divisor: '))

z=mul%m

print('remainder of the given list multiplication by input number : '+str(z))