# replace charcter into symbol if str[0] comes after that

def rep_str(string):
    x=string[0]
    y=string.replace(x,'$')
    return x+y[1:]
print(rep_str('return'))