
import random
right = 0

for i in range(0,5):

    b=random.randint(1,10)
    a=int(input("enter a number from 1 to 10: "))

    if a==b:
        print("you guessed right")
        right = right +1
    else:
        print("wrong")



print("you guessed right "+ str(right) + " times")
