def findprime(x):
    print('The given number is :'+str(x))

    for a in range(2,int(x/2)+1):
        if x%a==0:
           A=print(f'The given number {x} is not a prime nuhmber.')
        break
    else:
        A=print(f'The given number {x} is a prime nuhmber.')

A=int(input('Enter a number to find : '))

print(findprime(A))