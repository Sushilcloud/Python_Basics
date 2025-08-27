# Armstrong number abc=a^3+b^3+c^3=abc
# abcd... = pow(a,n) + pow(b,n) + pow(c,n) + pow(d,n) + ....

A=input("Enter the number:--")

def power(x,y):
     if y==0:
         return 1
     # reurns true if the number y is divisible by 2, and returns false if it is not divisible by 2
     if y % 2==0:
         return
