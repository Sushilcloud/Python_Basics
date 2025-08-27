# Factorial of any number is Factorialn=n*(n-1)*(n-2).......*1
# Fac4=4*3*2*1=24

num1 =input("Plese enter number to get his Factorial:--")

# create a funtion to get factorial
def factorial(num1):
    return 1 if(num1==1 or num1==0) else num1*factorial(num1-1);

print(factorial(int(num1)))
