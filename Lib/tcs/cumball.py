# finding cum ball left
n = int(input())

if n <= 10 and n <= 5:

    print('THE NUMBER OF CANDIES SOLD :' + str(n))
    print('THE NUMBER OF CANDIES AVAILABLE :' + str(10 - n))
else:
    print('INVALID INPUT')
    print('NUMBER OF CANDIES AVAILABLE:10')