def maxi(list):
    max=list[0]
    for i in list:
        if i>max:
            max=i
        else:
            continue
    return max

print(maxi([1,2,3,45,8,656,545,5,0]))