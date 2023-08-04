# converting multiple element into a single element

def sing(list):
    x=''.join(map(str,list))
    return int(x)
print(sing([1,2,3,4,5,6,7,8,9,2,3,4,4,5,5,6]))
