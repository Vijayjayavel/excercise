# find the nth fibinoci number

def n_fibonacci(x):
     if x<=0:
         print('Enter a valid input')
     elif x==1:
         return 0
     elif x==2:
         return 1
     else:
         return n_fibonacci(x-2)+n_fibonacci(x-1)

y=int(input('Enter a number :'))
print(n_fibonacci(y))

# print n fibonacci series
def fibonacci(y):
    a=0
    b=1
    if y<1:
        print("Enter a valid input")
    elif y==0:
        return a
    elif y==1:
        return b
    else:
        for i in range(2,y):
            c=a+b
            a=b
            b=c
            print(b)
m=int(input('\nEnter an input: '))
print(fibonacci(m))

