
inventory=20
while True:
    buy=input('We have ' + str(inventory) + ' items in inventory. How many would you like to buy? ')
    buyint=int(buy)
    if buyint > inventory:
        print("There is not enough in inventory for that purchase.")
    else:
        inventory=inventory-buyint
        if inventory <= 0:
            print("All out!")
            break
