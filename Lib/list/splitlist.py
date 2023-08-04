# splitting list
n=int(input('Enter the number of inputs: '))
list=[int(input("enter the inputs: ")) for i in range(1,n+1)]

start = 0
end = len(list)
step = int(input('Enter the step: '))
for x in range(start, end, step):

    print(list[x:x+step])