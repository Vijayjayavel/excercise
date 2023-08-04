# To find simple intrest of the given principle #
def Simpleinrest(P,N,R):
    print('The principle amount is ' + str(P))
    print('The number of years is ' + str(N))
    print('The simple intrest rate is ' + str(R))

    I=float((P*N*R)/100)

    print(f'Simple intrest rate for {P,N,R} is: {I}')

A=Simpleinrest(1000,2,13)
B=Simpleinrest(1000,4,25)