"""Write a Python program to print the following numbers up to 2 decimal places."""

def two_deci(string):
    return '{:+.2f}'.format(float(string)) 

print(two_deci('21454.1456'))

x=['3414.52','-45252.526','144523.14541']
print(list(map(two_deci,x))) # use the function for list of strings


