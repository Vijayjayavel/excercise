# To find maxi number between two number #
print("Enter 'q' to quit.")

Flag=True

while Flag:
    A=input('Enter the first number..')
    B=input('Enter the second number..')
    try:
        if A=='q' or B=='q':
            Flag=False
        elif int(A) > int(B):
            print(f'{A} is the maximum of two number')
        else:
            print(f'{B} is the maximum of two number')
    except ValueError:
        print('Enter a valid input')