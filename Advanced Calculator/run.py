import os
from functions import *
# from graphs import *71

if __name__ == '__main__':
    while True:
        os.system("cls")
        print("1.Basic Calculator\n2.HCF/LCM\n3.Exponential Calculator\n4.Multiplication Tables")
        print("5.Exponential Table\n6.Prime Number Check\n7.Factorisation")
        choice1 = int(input("...> "))
        os.system("cls")

        if choice1 == 1:
            basic_calc()

        elif choice1 == 2:
            hcf_lcm_calc()

        elif choice1 == 3:
            exponential_calc()

        elif choice1 == 4:
            multiplication_tables()

        elif choice1 == 5:
            exponential_table()

        elif choice1 == 6:
            num1 = int(input("Enter number: "))
            if prime_number_check(num1) == 1:
                print(f"{num1} is Prime")
            else:
                print(f"{num1} is not prime")

        elif choice1 == 7:
            factorisation()

        else:
            print("Wrong Choice\n")

        quit = input(
            "\n\n\nIf you want to continue press enter or press Q\n...> ")
        if quit.lower() == 'q':
            exit()
