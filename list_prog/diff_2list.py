def diff_2list(list1,list2):
    result=[]
    for i in range(len(list1)):
        result.append(list1[i]-list2[i])
    return result
print(diff_2list([6,5,4,3,2],[2,3,4,5,6]))