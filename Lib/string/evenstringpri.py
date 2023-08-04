# to print even length of words in given length of words

x=input('Enter a sentence:  ')
x=x.split()
for i in x:
    if len(i)%2==0:
        print(i)
    else:
        continue
        