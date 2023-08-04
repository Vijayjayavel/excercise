# to find a string palindrome or not

a=input('Enter an input: ').lower()
b=[*a]
c=reversed(b)
d=''
for i in c:
   d+=i

if a==d:
    print('given str is a palindrome')
else:
    print('given str is not a palindrome')