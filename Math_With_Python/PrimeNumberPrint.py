# Print all prime number between the range

# must define integer for % other wise error present
start=int(input("Enter the start number:--"))
end=int(input("Enter the End number:--"))

# use loop here
for i in range(start,end+1):
    if i>1:
        for j in range(2,i):
            if(i % j==0):
                break
        else:
            print(i)