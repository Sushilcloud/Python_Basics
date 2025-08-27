print("welcome to the rollercoaster !")

height=int(input("What is your height in cm?"))

if height >=120:
    print("you can ride the rollercoaster")
    age=int(input("what is your age?"))
    if age<=12:
        blll=5
        print("child ticket are $5")
    elif age <=18:
        bill=7
        print("youth ticket are $7")
    else:
        bill=12
        print("Adult ticket are $12")

    want_photo=input("Do you want to take photo type y for yes and n for no")
    if want_photo=="y":
        bill+=3
    print(f"your final bill amount is {bill}")

else:
    print("Sorry you have to gorw taller before you can ride")