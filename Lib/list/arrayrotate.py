# for rotation of array elements
n=int(input('enter the number of inputs : '))
arr=[int(input('enter the inputs: ')) for i in range(1,n+1)]

start = 0
end = len(arr)
step =int(input('Enter the step: '))
a=[]
for i in range(start, end, step):
    x = i
    b=arr[x:x+step] # slicing based on input
    b.reverse()
    print(b)
    a.append(b) # adding all the reversed list parts
print(a)

# adding all the sliced list after reversing
list=[]
for j in a:
    list.extend(j)
print(list)