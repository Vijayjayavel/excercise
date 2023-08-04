# counting matached character in pair of string
x = input('Enter a string: ').strip()

y = input('Enter the 2nd string: ').strip()

x = [*x] #  split  str each character
y = [*y]

z = []
count = 0
for i in x:
    if i in y:
        z.append(i)
        y.remove(i)
        count += 1

print('The total number of matched chracters :'+str(count))
print('the matched characters are: '+str(z))