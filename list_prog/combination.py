# to print combination of all the elements of a list

def combination(list):
    result=[]

    for n,i in enumerate(list):
        ele=str(i)
        for j in list[n+1:]:
            ele+=str(j)
            result.append(ele)
    return result
print(combination(['1','2','3','4','gowtham']))
