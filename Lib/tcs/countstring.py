# counting for valid string '#' and '*'

x=input('Enter an input: ')

y=[*x]

z=x.count('*')-x.count('#')
if z==0:
    print('number of # and * are equal')
elif z<0:
    print('number of # and stars are not equal there are more #')
else:
    print('number of # and stars are not equal there are more *')
