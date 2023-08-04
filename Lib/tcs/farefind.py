# fare calculation between routes
def getFare(s,d):
    route=[ [ "TH", "GA", "IC", "HA", "TE", "LU", "NI", "CA"],
    [800,600,750,900,1400,1200,1100,1500]
        ]
    fare = 0.0
    if not (s in route[0] and d in route[0]):
        print("Invalid Input")
        exit()
    if route[0].index(s) < route[0].index(d):
        for i in range(route[0].index(s),route[0].index(d)+1):
            fare+=route[1][i]
    elif route[0].index(d) < route[0].index(s):
        for i in range(route[0].index(s)+1,len(route[0])):
            fare+=route[1][i]
        for i in range(0,route[0].index(d)+1):
            fare+=route[1][i]
    return round(float((fare*5)/1000))
s = input()
d = input()
fare = getFare(s,d)
if fare == 0:
    print("Invalid Input")
else:
    print(fare)