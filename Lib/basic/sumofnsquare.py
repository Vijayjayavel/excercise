 # sum of first n square numbers

A=int(input('Enter a number: '))
sum=0
for i in range(0,A+1):
    sum=sum+i*i
print(f'sum of n square terms: {sum}')
# first A squares
squares=[i*i for i in range(1,A+1)]

print(f'the first {A} square numbers are:' )
for square in squares:
    print(square)
