# to find given number is arm strong or not

def Armstrongnumber(a):

    b = list(map(int, str(a)))

    c=0
    for i in range(0,len(b)):
        c=c+(b[i])**len(b)

    if c==a:
        print(f'the given number {a} is an armstrong number')
    else:
        print(f'given number {a} is not an armstrong number')
pArmstrongnumber(153)
Armstrongnumber(148)
Armstrongnumber(1634)