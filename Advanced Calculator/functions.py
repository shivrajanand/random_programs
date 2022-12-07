import math


def basic_calc():
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    opr = input("Enter operation: {+, -, /, *, %}: ")

    if opr == '+':
        print(f"{num1} + {num2} = {num1+num2}")
    elif opr == '-':
        print(f"{num1} - {num2} = {num1-num2}")
    elif opr == '*':
        print(f"{num1} x {num2} = {num1*num2}")
    elif opr == '/':
        print(f"{num1} {chr(247)} {num2} = {num1/num2}")
    elif opr == '%':
        print(f"{num1} % {num2} = {num1%num2}")


def advance_hcf():  # hcf and gcd are same thing
    list1 = []  # Empty list to store all hcf elements
    while True:
        element = input(
            "Enter integer element or press Enter to display result: ")
        if element == "":  # checks if user has entered "ENTER"
            break  # exit the while loop
        else:
            element = int(element)  # converting string element into integer
            list1.append(element)  # adding element to list

    temp_gcd = list1[0]  # assumed first element of list as gcd
    for i in list1:
        # comparing gcd with every element if list
        temp_gcd = math.gcd(temp_gcd, i)

    print("HCF of {", end="")  # printing the hcf
    for x in list1:
        print(f"{x}, ", end="")
    print("} = ", temp_gcd)


def advance_lcm():
    list1 = []  # Empty list to store all lcm elements
    while True:
        element = input(
            "Enter integer element or press Enter to display result: ")
        if element == "":  # checks if user has entered "ENTER"
            break  # exit the while loop
        else:
            element = int(element)  # converting string element into integer
            list1.append(element)  # adding element to list

    temp_lcm = list1[0]  # assumed first element of list as lcm
    for i in list1:
        # comparing lcm with every element if list
        temp_lcm = math.lcm(temp_lcm, i)

    print("LCM of {", end="")  # printing the lcm
    for x in list1:
        print(f"{x}, ", end="")
    print("} = ", temp_lcm)


def hcf_lcm_calc():
    choice = int(input("1.HCF\n2.LCM\n...> "))
    if choice == 1:  # HCF or GCD code
        advance_hcf()
    elif choice == 2:
        advance_lcm()


def exponential_calc():
    base = float(input("Enter base value: "))
    power = float(input("Enter power value: "))
    print(f"{base} raised to {power} is {pow(base, power)}")


def multiplication_tables():
    num = int(input("Enter number of which multiplication table is required: "))
    multiple = int(input("Enter number of multiples required: "))
    for i in range(1, multiple+1):
        print(f"{num} x {i} = {num*i}")


def exponential_table():
    try:  # used this to handle overflow error which is very common in exponents
        base = float(input("Entervalue for initial base: "))
        power = float(input("Enter power value: "))

        for i in range(10):
            print(f"S.No{i+1}   {base} raised to {power} is {pow(base, power)}")
            temp = pow(base, power)  # new base
            base = temp  # storing new base in base variable

    except OverflowError:  # results too large
        print("\nUnable to print further results.\nResult too large!!!")


def prime_number_check(num):
    flag = 0  # 0 means not prime
    # If a number is prime and is not 2 then it can be expressed in form 6n+1 or 6n-1

    if num == 2 or num == 3:
        flag = 1

    elif (num-1) % 6 == 0:  # num = 6n+1 ==> n = (num-1)/6
        flag = 1

    elif (num + 1) % 6 == 0:  # num = 6n-1 ==> n = (num+1)/6
        flag = 1

    else:
        print()

    return flag


def factorisation():
    num = int(input("Enter number: "))
    factor = []
    if prime_number_check(num) == 1:
        print("Number is prime")
        print(f"Factors: 1, {num}")

    else:
        for i in range(1, num+1):
            if (num % i) == 0:
                factor.append(i)

    print("Factors are: ", factor)
