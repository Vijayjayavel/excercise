"""Write a Python program to find the first appearance of the substrings 'not' and 'poor' in a given string.
 If 'not' follows 'poor', replace the whole 'not'...'poor' substring with 'good'.
 Return the resulting string"""

def re(string):
    x=string.find('poor')
    y=string.find('not')
    if (x!=-1 and y!=-1) and x>y:
        string=string.replace(string[y:x+4],'good')
    elif x!=-1:
        string=string.replace('poor','good')
    return string
print(re('The lyrics is not that poor!'))
print(re('The lyrics is good!'))