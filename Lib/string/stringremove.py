# To remove ith string

test_str =input('Enter a string: \n')
n=int(input('Enter which position of character should be removed: \n'))

new_str = ""

for i in range(len(test_str)):
	if i != n:
		new_str = new_str + test_str[i]

print ("The string after removal of 'n'th character : " + new_str)
