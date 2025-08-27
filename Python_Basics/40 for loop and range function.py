# range function
total=0
for i in range(1,10):
    total+=i
    #print(i)
print(total)


for p in range(1,20):
    if p%3==0 and p%5==0:
        print("Number Divisable by both 3 and 5")
    elif p%3==0:
        print("Divisable by 3")
    elif p%5==0:
        print("Divisable by 5")
else:
   print(i)