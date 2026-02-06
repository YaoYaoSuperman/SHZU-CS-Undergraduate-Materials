t = list(map(eval, input().split()))
Y,M,D = t[0],t[1],t[2]
flag = 0
if (Y % 4 == 0) & (Y % 100 != 0):
    flag = 1
elif Y % 400 == 0:
    flag = 1
if (M == 4)|(M == 6)|(M == 9)|(M == 11):
    if D<30:
        D = D + 1
        print("{} {} {}".format(Y,M,D))
    elif D == 30:
        M = M+1
        D = 1
        print("{} {} {}".format(Y,M,D))
    else:
        print("Erorr,No data");
elif M == 2:
    if flag == 1:
        if D<29:
            D = D+1
            print("{} {} {}".format(Y,M,D))
        elif D == 29:
            M = M + 1
            D = 1
            print("{} {} {}".format(Y,M,D))
        else:
            print("Erorr,No data");
    else:
        if D < 28:
            D = D + 1
            print("{} {} {}".format(Y,M,D))
        elif D == 28:
            M = M + 1
            D = 1
            print("{} {} {}".format(Y,M,D))
        else:
            print("Erorr,No data");
elif M == 12:
    if D<31:
        D = D + 1
        print("{} {} {}".format(Y,M,D))
    elif D == 31:
        Y = Y + 1
        M = 1
        D = 1
        print("{} {} {}".format(Y,M,D))
    else:
        print("Erorr,No data");
elif (M == 1)|(M == 3)|(M == 5)|(M == 7)|(M == 8)|(M == 10):
    if D < 31:
        D = D + 1
        print("{} {} {}".format(Y,M,D))
    elif D == 31:
        M = M+1
        D = 1
        print("{} {} {}".format(Y,M,D))
    else:
        print("Erorr,No data");
else:
    print("Erorr,No data");
