
maxnum=1000

a=0
b=1
c=2
while True:
    c=a+b

    a=b
    b=c
    if a >= maxnum:
        break

    print(a)

