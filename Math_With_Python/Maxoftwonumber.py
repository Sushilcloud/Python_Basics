# Find Max of tow number

num1=input("please enter number1:-")
num2=input("pleaes enter number2:-")

def max(num1,num2): # create funtion here
    if num1 > num2:
        return num1
    else:
        return num2

print("Maximum number is",max(num1,num2))