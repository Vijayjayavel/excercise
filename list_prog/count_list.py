# count number of string in list

def cntstr(list):
    str=0
    for i in range(0,len(list)):
        if list[i] in list[i+1:]:
            continue
        else:
            if type(list[i]) is int:
                # print(type(list[i]))
                continue
            else:
                str+=1

    return str
print(cntstr(['2','sfs','4',';',5]))
print(cntstr(['3','5',6,8,'33','3','3']))
print(cntstr([1,2,3,4]))
print(cntstr(['5' for i in range(10)]))
