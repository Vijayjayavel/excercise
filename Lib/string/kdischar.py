"""Write a Python program to count the number of substrings from a given string of
  with exactly k distinct (given) characters"""

def kdischr(string,k):
    x=[]

    for i in range(len(string)):
        for j in range(i+k,len((string))+1):
            x.append(string[i:j])
    out=list(filter(lambda x:len(set(x))>=4,x))

    return (len(out),out)

print(kdischr('agdtsytnudsftsdrynbudrt',3))
print(kdischr('wolf',4))




