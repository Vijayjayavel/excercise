"""Write a Python program to reverse words in a string"""
def rever_word(string):
    x=string.split()
    print(' '.join(x[::-1])) # print every word reveserd
    y=[]
    for i in x:
        a=''.join(reversed(i))
        y.append(a)
    return ' '.join(y)
print(rever_word('Eye for an eye make the whole world blind')) # each word reversed

