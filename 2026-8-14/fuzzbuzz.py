
n=input()
a=int(n)
if a%3 == 0 and a%5 ==0 :
    print("fuzz buzz")
else:
    if a%3 == 0 :
        print("fuzz")
    if a%5 == 0 :
        print("buzz")


