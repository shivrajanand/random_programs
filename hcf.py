def hcf(a, b):
    if (a == 0):
        return b
    elif (b == 0):
        return a
    else:
        return hcf(b%a, a)
    
    
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print(f"HCF of {num1} and {num2} is {hcf(num1, num2)}")