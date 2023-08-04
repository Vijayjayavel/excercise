# remove particular element from the list

def rem_ele(list,indices): #list=[1,2,3],indices=[0,1]
    result=[]
    for n,i in enumerate(list):
        if n not in indices:
            result.append(i)
    return result
print(rem_ele([i for i in range(100)],[i for i in range(0,100,2)]))
