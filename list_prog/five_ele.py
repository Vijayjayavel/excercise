# return 1st 5 ele and last 5 ele from a list
import random
from random import choice
def ran_list(list):
        for i in range(5):
            x = choice([i**2 for i in range(1, 31)])
            list.insert(0, x)
        for i in range(5):
            x = choice([i ** 2 for i in range(1, 31)])
            list.append(x)
        return list
print(ran_list([1,2,33245,245]))