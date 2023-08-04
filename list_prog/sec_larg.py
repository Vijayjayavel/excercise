# find second largest number

def sec(list):
    if list[0]<list[1]:
        maxi=list[1]
        maxi2=list[0]
    else:
        maxi = list[0]
        maxi2 = list[1]

    for i in list[2:]:
        if i >maxi :
            maxi2 = maxi
            maxi=i
        elif i>maxi2 and i<maxi:
            maxi2=i
        else:
            continue
    return maxi,maxi2

print(sec([12,3,4,5,7,88,9,87]))

