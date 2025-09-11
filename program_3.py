    #figure out how many items we are buying and save that number. I know this isnt required, but I wanted 
    #the challenge. If you dont like it, you can just enter 5
print("How many items are you purchasing?")
numberofitems = int(input())

currentitem = 1
totalitemcost = 0
TAX = 0.07
    
while currentitem <= numberofitems:                                    #check to make sure we are still on an item number that we want. If we only have 6 items but we are on item 7, then we shouldnt ask for the price of item 7 and should instead continue on to print our total.
    print("How much does item number " + str(currentitem) +" cost?")    
    totalitemcost += float(input())                                    #here, instead of saving the input to a seperate variable and adding it, we simply add the number to the total.
    currentitem += 1                                                   #here we increase our item number by 1
else:  
    print("Item subtotal: " + str(totalitemcost))                      #print out totals, doing the math within the print line to reduce the amount of variables we need.
    print("Sales tax: " + str(totalitemcost * TAX))
    print("     Total: " + str(totalitemcost * (TAX + 1)))
