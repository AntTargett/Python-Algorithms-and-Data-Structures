def GCD(N1,N2):
    a=N1
    b=N2

    while True:
        if a%b!=0:
            r=a%b
        else:
            print(b)
            break
        a=b
        b=r
