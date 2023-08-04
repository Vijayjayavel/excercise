def re_dup(list):
    result=[]
    [result.append(i) for i in list if i not in result]
    return result

print((re_dup([5 for i in range(10)])))

# print(list(set([1,2,3,4,5,5,4,3,2,1])))  #simple way