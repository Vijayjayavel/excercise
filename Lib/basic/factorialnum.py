# To find factorial of a given number #

while True:
    print("\nEnter 'q to break.")
    num = input("Enter a number: ")
    try:
        factorial = 1
        if num.lower()=='q':
            break
        elif int(num) < 0:
           print("Sorry, factorial does not exist for negative numbers")
        elif int(num) == 0:
           print("The factorial of 0 is 1")
        else:
           for i in range(1,int(num) + 1):
               factorial = factorial*i
           print("The factorial of",num,"is",factorial)
    except ValueError:
        print('Enter a valid input..')


