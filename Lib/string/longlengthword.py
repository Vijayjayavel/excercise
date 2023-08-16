"""Write a Python function that takes a list of words
 and return the longest word and the length of the longest one."""

def sen(string):
    z=string.split(' ')
    x={key:len(key) for key in z}
    return max(zip(x.values(),x.keys(),))

print(sen('abcde abcdf aaaa aaa aa a'))