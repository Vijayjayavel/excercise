""" Write a Python program to count the number of substrings with
the same first and last characters in a given string."""

def count_same_firstlastchr(string):
    string=[*string]
    x=0
    for i in range(len(string)):
        for j in range(i,len(string)):
            if string[i]==string[j]:
                x+=1
    return x

print(count_same_firstlastchr('abab'))