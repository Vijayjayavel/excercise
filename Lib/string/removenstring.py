# to remove nth character from a string

a=input('Enter a string: ')
b=int(input('Enter the character you want to remove: '))
newstr=''
for i in range(len(a)):
    if i!=b-1:
        newstr=newstr+a[i]
print(newstr)
# print(a[:b-1]+a[b:]) simple solution