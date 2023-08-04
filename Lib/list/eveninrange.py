# print even numbers in a range
a=int(input('Enter starting range: '))
b=int(input('Enter endding range'))

even=[]
for i in range(a,b):
    if i%2==0:
        even.append(i)
    else:
        continue
for e in even:
    print(e)