# to print repeated element

def Repeat(x):
    size = len(x)
    repeated = []
    for i in range(size):
        k = i + 1
        for j in range(k, size):
            if x[i] == x[j] and x[i] not in repeated:
                repeated.append(x[i])
    return repeated

n=int(input())
list1 = [int(input('Enter an input: ')) for i in range(n)]
print(Repeat(list1))