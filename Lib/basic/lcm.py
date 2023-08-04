# lcm of given number #

N=int(input('Enter the number of input: '))

values=[]
print('non negative and non zero values..')
for value in range(N):
    values.append(int(input('Enter the Values')))
res=[]
#ihj7tgnugt
values.sort()

for i in range(2,values[len(values)-1]):
    count=0
    for j in range(0,len(values)-1):
        if values[j]%i==0:
            count+=1
    if(count>=1):
        res.append(i)
res.sort()
for k in res:
    print(k)


'''i=1
while True:
    for value in values:
        if i%value[0]==0 and i%value[1]==0
            print(i)
    i+=1'''

