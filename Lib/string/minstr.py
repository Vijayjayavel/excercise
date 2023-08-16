"""Write a Python program to find the minimum window in a given string that will contain all
the characters of another given string."""

def minstr(string,chrs):

    a=[]
    for i in chrs:
        a.append(string.rindex(i))
    return string[min(a):max(a)+1]
print(minstr(' PRWSOERIUSFK','OSU'))

print(minstr('afssfaasg','asfg'))



