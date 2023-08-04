# return True if all ele prime otherwise false

def prime_find(list):
    m=max(list)
    for i in list:
        for j in range(2,round(m/2)+1):
            if 1 in list:
                x=False
                break
            elif i%j==0:
                x=False
                break
        else:
            x=True
    return x

print(prime_find([1,4,5,6,9,0,5,9,9,0]))
print(prime_find([1,3,5,7,13,19,23,29]))
print(prime_find([3,5,7,13,19,23,29]))