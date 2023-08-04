# To find compound intrest rate
def Compoundintrest(P,N,R):

    print('The principle amount is '+str(P))
    print('The number of years is '+str(N))
    print('The compound intrest rate is '+str(R))

    I=float(((P*(((100+R)/100)**N)))-P)

    print(f'compund intrest rate for {P,N,R} is: {I}')

A=Compoundintrest(1000,2,1)
