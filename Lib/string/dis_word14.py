"""Write a Python program that accepts a comma-separated sequence of words as input and
 prints the distinct words in sorted form (alphanumerically)."""

def dis():
    n=input('enter input,seperated: ')
    x=n.split(',')
    y=sorted((set(x)))
    return ','.join(y)
print(dis())