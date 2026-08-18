a=100





three=0
five=0
threefive=0
for i in range(1,a):
    if i%3 == 0 and i%5 ==0 :
        threefive=threefive+1
    else:
        if i%3 == 0 :
            three=three+1
        if i%5 == 0 :
            five=five+1


print("factors of 3:  " +str(three))
print("factors of 5:  " +str(five))
print("factors of 3 and 5:  " +str(threefive))
