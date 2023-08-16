"""Write a Python program to compute the sum of the digits in a given string."""

def sumofdig(string):
    x=[*string]
    sod=0
    for i in x:
        if i.isdigit()==True:
            sod+=int(i)
    return sod
print(sumofdig('4457jfa542'))