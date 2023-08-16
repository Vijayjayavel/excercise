def faltten(list1):
    out=[]
    for i in list1:
        if type(i) is list:
            for j in i:
                out.append(j)
        else:
            out.append(i)
    return out
print(faltten([[1,2,3],[2,3,4],[6],[4,22,3],3,4,5]))

import itertools
lis=[[1,2,3],[2,3,4],[6],[4,22,3]]
print(list(itertools.chain(*lis)))
