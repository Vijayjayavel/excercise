import string
def represtr(strings):
    return ' '.join(str(ord(i.lower())-96) for i in strings if i.isalpha())
print(represtr('fasv'))
print(represtr('Vijay'))