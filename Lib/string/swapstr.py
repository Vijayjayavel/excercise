# swap first 2 char of two string and return joined strings sepearated by ' '

def strgs(s1,s2):
    x=s2[:2]+s1[2:]
    y=s1[:2]+s2[2:]
    return x+' '+y

print(strgs('vijay','ajith'))