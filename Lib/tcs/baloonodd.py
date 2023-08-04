# counting baloon odd

while True:

    n=int(input('Enter the number of baloons: '))
    if n>=3 and n<=50:
        break
    else:
        print('Enter a valid baloon number(3-50)')

a=[]
for i in range(n):
    while True:
        x=input('Enter the baloon color: ')
        if x.isalpha():
            a.append(x.lower())
            break
        else:
            print('Enter a valid baloon color..!')

b={}
for items in b:
    b[key]=value


def count(b):
    count = 0
    for i in a:
        if i == b:
            count += 1
        else:
            continue
    print(f"the number of time '{b}' appeared: ")
    return count

res = {key: x.count(key) for key in list}
print(res)

print(map(count(),a))

'''
c=[]
d=[]
#d=[0 for i in range(n)]
for i in range(0,len(a)-1):
    if a[i] not in c:
        c.append(a[i])
        d.append(i)
    else:
        for j in range(0,len(c)-1):
            if(c[j]==a[i]):
                d[j]=d[j]+1
'''






