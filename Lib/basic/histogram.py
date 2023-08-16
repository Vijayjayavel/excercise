# histogram print with respect to the list values
x=input('enter the input with comma seperated value')
y=list(map(int,x.split(',')))
print(y)
sym=input('enter the symbol you want to print')

for i in y:
    out=''
    while i>0:
        out=out+sym
        i=i-1
    print(out)