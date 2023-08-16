"""remove consecutive char in a string"""

def restr(string):
    i=0
    j=0
    s=''
    while j<len(string):

        if string[i]==string[j]:
            j+=1
        elif string[i]!=string[j] or j==len(string)-1:
            s+=string[i]
            i=j
            j+=1
    s=s+string[j-1]
    return s
print(restr('aaaaaaaabbbbbbbbjgnbbbbbbbbbbbbbbbbcccccccccc'))

def rem_con(string):
    if len(string)<2:
        return string
    elif string[0]!=string[1]:
        return string[0]+rem_con(string[1:])
    return rem_con(string[1:])
print(rem_con('aaaaaaaaaaaabbbbbbbbbbbbbcccccccddddddgfdsgvrgrrrsrdgggggggggggghhhhhhsedd'))

def rem_cons(string):
    x=[string[0]]

    for i in string[1:]:
        if i!=x[-1]:
            x.append(i)
    return ''.join(x)
print(rem_cons('aaaaaaaaaaaabbbbbbbbbbbbbcccccccddddddgfdsgvrgrrrsrdgggggggggggghhhhhhsedd'))