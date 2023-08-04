'''while True:
    n=int(input('Enter number of horses: '))
    k=int(input('Enter the reward money: '))
    if 2>n or n>105 or k<2 or k>109:
        print('Enter a valid input: ')
    else:
        break
'''
def fun(n, k, arr):
    ans = 0
    if min(arr) < k:
        ans = 1
    for i in range(n - 1):
        for j in range(i + 1, n):
            if sum(arr[i:j]) < k:
                ans = max(ans, j - i)
            else:
                break
    return ans


n, k = map(int, input().split())
arr = list(map(int, input().split()))
print(fun(10, 20, [1,2,3,4,5,6,7,8,8,9]))