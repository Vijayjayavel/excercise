# check wheather list empt or not

def emp_lst(list):
    if list:
        x='list is not empty'
    else:
        x='list is empty'
    return x

print(emp_lst([]))
print((emp_lst([1])))