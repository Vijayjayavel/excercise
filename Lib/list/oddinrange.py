# print odd in range
a=int(input('Enter starting range: '))
b=int(input('Enter endding range'))

odd=[]
for i in range(a,b):
    if i%2!=0:
        odd.append(i)
    else:
        continue
for o in odd:
    print(o)
