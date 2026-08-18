import random

a=random.randint(1,3)

b=input("""(1)rock
(2)paper
(3)scissors
""")

b=int(b)

lookup=["","rock","paper","scissors"]
if a == b:
    print("tie")
if (a == 1 and b == 3) or (a == 2 and b == 1) or (a == 3 and b == 2):
    print("Computer won")
else:
    print("you won")


print("computer did " + lookup[a])


