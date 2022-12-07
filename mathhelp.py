def tables():
    print(f"{choice2} x 1 = {choice2 * 1}")
    print(f"{choice2} x 2 = {choice2 * 2}")
    print(f"{choice2} x 3 = {choice2 * 3}")
    print(f"{choice2} x 4 = {choice2 * 4}")
    print(f"{choice2} x 5 = {choice2 * 5}")
    print(f"{choice2} x 6 = {choice2 * 6}")
    print(f"{choice2} x 7 = {choice2 * 7}")
    print(f"{choice2} x 8 = {choice2 * 8}")
    print(f"{choice2} x 9 = {choice2 * 9}")
    print(f"{choice2} x 10 = {choice2 * 10}")

def calcy():
    if choice3 == 1:
        print(num1, "+", num2, "=", num1 + num2)
    elif choice3 == 2:
        print(num1, "-", num2, "=", num1 - num2)
    elif choice3 == 3:
        print(num1, "x", num2, "=", num1 * num2)
    elif choice3 == 4:
        print(num1, "÷", num2, "=", num1 / num2)
    elif choice3 == 5:
        if num1 > num2:
            g = num1
            s = num2
        else:
            g = num2
            s = num1
        print("The remainder of", num1, "and", num2, "is", g % s)
    elif choice3 == 6:
        print(num1, "raised to the power of", num2, "=", num1 ** num2)
    elif choice3 == 7:
        print("The square of", num1, "=", num1 ** 2)
        print("The square of", num1, "=", num1 ** 2)
    elif choice3 == 8:
        print("The cube of", num1, "=", num1 ** 3)
        print("The cube of", num2, "=", num2 ** 3)

def expo():
    print(f"{base} raised to the power of {power} = {base ** power}")
    
while(True):
    choice1 = int(input("Choose what you want to do:\n 1. Multiplacation Tables\n 2. Calculator\n 3. Exponents\n"))

    if choice1 == 1:
        choice2 = float(input("Enter your rational number here:\n"))
        tables()
        c = input("If you want to coninue than press Enter otherwise press Q:\n")
        c.upper()
        if c == "\n":
            continue
        elif c == "Q":
            exit
            

    elif choice1 == 2:
        choice3 = int(input("Enter your operation here\n 1. Addition\n 2. Subtraction\n 3. Multiplication\n 4. Division\n 5. Remainder\n 6. Exponential Powers\n 7. Square\n 8. Cube\n"))
        num1 = float(input("Enter first number:\n"))
        num2 = float(input("Enter second number:\n"))
        calcy()
        c.upper()
        if c == "\n":
            continue
        elif c == "Q":
            exit

    elif choice1 == 3:
        base = float(input("Enter the base value:\n"))
        power = float(input("Enter the power:\n"))
        expo()
        c.upper()
        if c == "\n":
            continue
        elif c == "Q":
            exit()
        