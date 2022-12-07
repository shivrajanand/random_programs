n = int(input("Enter number of star in top of Z: "))

for i in range(n):
    if i == 0 or i == (n-1):
        print("*"*n)
    else:
        for j in range(n-1-i):
            print(" ", end="")
        print("*", end="")
        for k in range(n-i ,n):
            print(" ", end="")
        print("\n", end="")
