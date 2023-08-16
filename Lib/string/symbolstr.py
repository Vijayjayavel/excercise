"""Write a Python program to print the following integers with '*' to the right of the specified width."""

def star_num(num):
    return str(num)+'*'*num
print(star_num(5))

x=[10,3,6,7,8,9,9,4,5,6,7,3,34,5,6,7]
print(list(map(star_num,x)))