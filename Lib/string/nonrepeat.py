'''Write a Python program to find the first non-repeating character in a given string'''

def non_repeat(string):
    for i in string:
        if i not in string[string.index(i)+1:]:
            return i
        else:
            continue
    return None

print(non_repeat('abcdefabcde'))
print(non_repeat('rajaram'))