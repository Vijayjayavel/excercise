# count string in given sentence

x=input('Enter a sentence:  ')

'''b=input('Ener the string you want to count: ')''' # input to print count

list=[*x]

def count(b):
    count=0
    for i in list:
        if i==b:
            count+=1
        else:
            continue
    print(f"the number of time '{b}' appeared: ")
    return count

print(count('a'))

res={key:x.count(key) for key in list}

print(res)

