def frq(list):
    dic={}
    for i in list:
        if i not in dic.keys():
            dic[i] = 0
            dic[i] = dic[i] + 1

        else:
            dic[i] += 1

    return dic
print((frq([1,2,3,4,4,4,2,2,3])))