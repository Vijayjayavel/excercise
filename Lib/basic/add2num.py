# Find addition of Two number #
while True:
    print("enter 'q to quit")
    A=input('enter a number: ')
    try:

        if A.lower()=='q':
            break

        elif int(A)%2==0:
            print(f'the number {A} is an even number')

        else:
            print(f'the number {A} is a odd number')

    except ValueError:
        print('enter a valid input...')