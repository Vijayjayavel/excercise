def faltten(list):
    out=[]
    for i in list:
        for j in i:
            out.append(j)
    return out
print(faltten([[1,2,3],[2,3,4],[6],[4,22,3]]))

import itertools
lis=[[1,2,3],[2,3,4],[6],[4,22,3]]
print(list(itertools.chain(*lis)))
