import matplotlib.pyplot as plt

def armstrong(num):
    temp1 = num
    p = len(str(num))
    sum = 0

    temp2 = num

    for i in range(len(str(num))):
        digit = str(num)[i]
        digit = int(digit)
        sum = sum + (digit**p)

    if (sum == num):
        return 1
    else:
        return 0


if __name__ == '__main__':
    low = int(input("Enter lower limit of range: "))
    high = int(input("Enter higher limit of range: "))

    last = 0
    x = 0
    rlist = []
    xlist = []
    for i in range(low, high+1):
        result = armstrong(i)
        if result == 1:
            print(f"{i} --> {i - last}")
            rlist.append(i-last)
            x += 1
            xlist.append(x)
            last = i
            
    print(rlist)
    # print(xlist)
    
    plt.plot(xlist, rlist)
    plt.show()
    
    