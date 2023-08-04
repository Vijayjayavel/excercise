# to print minimum accuring character

x=input('Enter a string: ')
dic={key:x.count(key) for key in x}

print(dic)

res = min(dic, key = dic.get)

print(res)