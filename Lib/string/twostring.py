"""Write a Python program to generate two strings from a given string.
 For the first string, use the characters that occur only once,
 and for the second, use the characters that occur multiple times in the said string"""

def cre_str(string):
    dic={key:string.count(key) for key in string}
    odd=list(dict(filter(lambda x:x[1]<2,dic.items())).keys())
    even=list(dict(filter(lambda x:x[1]>=2,dic.items())).keys())
    print('(odd),(even):')
    return (''.join(odd),''.join(even))

print(cre_str('jhevtgjalhva'))
print(cre_str("aabbcceffgh"))