#sum of 'n' cube terms
n=int(input('Enter a number: '))
sum=0
for i in range(0,n+1):
    sum=sum+i*i*i
print(f'sum of n cube terms: {sum}')
# first 'n' cubes
cubes=[i*i*i for i in range(1,n+1)]

print(f'the first {n} cube numbers are:' )
for cube in cubes:
    print(cube)
