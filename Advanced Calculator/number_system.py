import os

def operation_list():
    opr_list = ['1.binary_to_decimal', '2.octal to decimal', '3.hexadecimal to decimal',
            '4.decimal to binary', '5.decimal to octal', '6.decimal to hexadecimal']
    return opr_list

def binary_to_decimal():
    num = int(input("Enter Binary Number: "))

    for i in str(num):
        if i not in "10":
            os.system("cls")
            print(f"Invalid Binary Number: {num}. Please enter again")
            del num
            binary_to_decimal()
        else:
            p = len(str(num))-1  # powers of 2
            sum = 0
            for i in str(num):
                i = int(i)
                sum = sum + i*(2**p)
                p = p-1

    

    print(f"Binary: {num}\nDecimal: {sum}")
    
def octal_to_decimal():
    num = int(input("Enter Octal Number: "))

    for i in str(num):
        if i not in "01234567":
            os.system("cls")
            print(f"Invalid Octal Number: {num}. Please enter again")
            octal_to_decimal()
        else:
            print()

    p = len(str(num))-1  # powers of 8
    sum = 0
    for i in str(num):
        i = int(i)
        sum = sum + i*(8**p)
        # print(f"{i}x8^{p} = {i*(8**p)}")
        # print(f"sum = {sum}")
        p = p-1

    print(f"Octal: {num}\nDecimal: {sum}")

def hexadecimal_to_decimal():
    print()

def run():
    for x in operation_list():
        print(x)
    choice = int(input("Enter task number: "))
    os.system("cls")
    if choice == 1:
        binary_to_decimal()
    
    elif choice == 2:
        octal_to_decimal()
        
    elif choice == 3:
        hexadecimal_to_decimal()
        
    else:
        print("Wrong Choice")
    
run()
