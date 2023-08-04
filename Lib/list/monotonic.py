# To find given input is monotonic or not
n=int(input('enter the number of inputs : '))
arr=[int(input('enter the inputs: ')) for i in range(1,n+1)]
list1=sorted(arr)
list2=sorted(list1,reverse=True)

if arr==list1:
    print('Given input array is monotonically increasing.')
elif arr==list2:
    print('Given input is monotonially decreasing.')
else:
    print('Given input is not monotonic')
