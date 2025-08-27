# Compound Interest  Formula is Amount=P(1+R/100)^t
# P for Principle
# R for Rate
# T for Time

# ask user to input the values
principle=input("Enter Principle Amount ==")
rate=input("Enter Rate of Interest==")
time=input("Enter Time ")

# Defined funtion here
def compound_interest(principle,rate,time):
    Amount=principle*(pow((1+rate/100),time))
    ci =Amount-principle

#print(compound_interest(float(principle),float(rate),float(time)))

    print(int(ci))