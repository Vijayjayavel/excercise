# print tuple sort inside list by 2nd ele of tuple
def last(n):
    return n[-1]

def ord_list(list):
    return sorted(list,key=last)

print(ord_list([(1,4),(4,2),(19,67),(-2,-9)]))
