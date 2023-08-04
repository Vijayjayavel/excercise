#prime number in an enterval

def Prime(a,b):
    print('starting number of the interal: '+str(a))
    print('ending number of the interval: '+str(b))
    p=[]
    for i in range(a,b):
        if i==0 or i==1:
            continue
        else:
            for j in range(2,int(i/2)+1):
                if i%j==0:
                    break
            else:
                (p.append(i))
    print(f'The list of prime number in between {a,b} is ')
    print(p)
    print(f'\nThe total number of prime numbers in between {a,b} is ')
    return len(p)


st=int(input("give the input : "))
end=int(input("give the end value : "))
print(Prime(st,end))