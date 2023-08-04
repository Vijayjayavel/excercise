# creating multiple list

out=[[[i] for i in range(10)]for j in range(10)]
print(out)


l1=['0', '1', '2', '3', '4']
l2=['red', 'green', 'black', 'blue', 'white']
l3=['100', '200', '300', '400', '500']
list=['{}{}{}'.format(x,y,z) for x,y,z in zip(l1,l2,l3)]
print(list)

list=[i for i in range(30)]
n=2.2
li=[]
for i in list:
    i=i+2.2
    li.append(i)

print(li)