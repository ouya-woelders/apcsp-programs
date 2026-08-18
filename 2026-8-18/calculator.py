while True:
    o=input("""operator:
    1(+)
    2(-)
    3(*)
    4(/)
    5(exit)
    """)


    o=int(o)
    if o==1:
        n=int(input("first number: "))
        m=int(input("second number: "))
        print(n+m)
    elif o==2:
        n=int(input("first number: "))
        m=int(input("second number: "))
        print(n-m)
    elif o==3:
        n=int(input("first number: "))
        m=int(input("second number: "))
        print(n*m)
    elif o==4:
        n=int(input("first number: "))
        m=int(input("second number: "))
        if not(m==0):

            print(n/m)
        else:
            print("cannot divide by 0")
    elif o==5:
        break
    else:
        print("invalid operator")
    print()

