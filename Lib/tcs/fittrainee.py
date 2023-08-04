# to find fit trainee
trainee = [[], [], [], []]
for i in range(3):
    for j in range(3):

        while True:
            x = int(input(f'Enter {i+1} batch input of {j+1} trainee: '))
            if x not in range(1, 101):
                print("invalid input")
            else:
                trainee[i].append(x)
                break

for i in range(3):
    trainee[3].append(round((trainee[2][i] + trainee[1][i] + trainee[0][i])/3))
maximum = max(trainee[3])
for i in range(3):
    if trainee[3][i] < 70:
        print("Trainee {0} is unfit".format(i + 1))
    elif trainee[3][i] == maximum:
        print("Trainee Number: ", i + 1)