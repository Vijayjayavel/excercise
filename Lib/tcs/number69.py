# to find a number's square and cube lements have number 0-9

x=[0,1,2,3,4,5,6,7,8,9]
i=0
Flag=1
cnt1=0
while Flag:
    cnt=0
    a=[*str((i**2)),*str((i**3))]
    for j in x:
        if str(j) not in a:
            i+=1
            break
        else:
            cnt+=1

    if(cnt==10 ):
        print(i)
        i += 1
        cnt1+=1
        if(cnt1==10):
            Flag=0



""""
for i in d:
    if int(i) in x:
        print(True)
    else:
        print('false')

"""