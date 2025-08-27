english=int(input("Enter english marks"))
maths=int(input("Enter maths marks"))
if english>=80:
    if maths>=80:
        print("your are good in both subject")
    else:
        print("you are good only in maths")
if english>=80:
    print("you are good in english")


height=int(input("enter your height for roller coaster"))
if height >=180:
    print("you are eligible for roller coaser")
    age=int(input("Enter your age"))
    if age <=12:
        print("Please pay rs100")
    elif age <=6:
        print("Please pay rs 50")
    else:
        print("please pay 200")
else:
    print("sorry you dont take ride")