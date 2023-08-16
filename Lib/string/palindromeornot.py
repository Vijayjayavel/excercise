# to find a string palindrome or not

a=input('Enter an input: ').lower()
# b=[*a]
c=a[::-1] #reversing  the input
# print(c)
# d=''
# for i in c:
#    d+=i

if a==c:
    print('given str is a palindrome')
else:
    print('given str is not a palindrome')