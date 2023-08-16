"""Remove duplicate characters of a given string"""

def remdup(string):
    x=[]
    for i in string:
        if i not in x or i==' ':
            x.append(i)
    return ''.join(x)
print(remdup('nallai allai nallai allai nan nilave nee nallai allai'))
print(remdup("python exercises practice solution"))