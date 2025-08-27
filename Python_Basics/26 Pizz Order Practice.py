print("welcome to python pizza order deliveries")
size=input("what size of piza do you want? S, M, and L")
bill=0
if size=="S":
    bill+=15
    print("Cost of Pizz is 15$")
elif size=="M":
    bill += 20
    print("Cost of Pizz is 20$")
elif size=="L":
    bill += 25
    print("Cost of Pizz is 25$")
else:
    print("you type the wrong input")
paperoni=input(print("Do you want add pepperoni in Medium and Large Pizz Y and N Cost Extra 3"))
if paperoni=="Y":
    if size=="M":
        bill+=3
    else:
        bill+=2
print(bill)
extracheez=input(print("Do you want add extra cheez in Medium and Large Pizz Y and N Cost Extra 1"))
if extracheez=="Y":

        bill+=1

print(f"your final bill amount is {bill}")


