import matplotlib.pyplot as plt

def collatz(a):
    yaxis = [a]
    d = a

    while d != 1:
        if d % 2 == 0:
            d = d/2
            yaxis.append(d)
        else:
            d = 3*d + 1
            yaxis.append(d)

    return yaxis

if __name__ == '__main__':
    x = []  # stores lists as elemenst for x-axis
    y = []  # stores lists as elemenst for y-axis
    legend = []  # legend list

    low = int(input("Enter low value: "))
    high = int(input("Enter high value: "))


    for i in range(low, high+1):
        xtemp = []  # for temporary storage of elements
        ytemp = []  # for temporary storage of elements
        ytemp = collatz(i)  # list of collatz values for i
        y.append(ytemp)  # storing the list in main y-list
        for j in range(len(ytemp)):  # creating the x-set corresponding to y-set
            xtemp.append(j+1)

        x.append(xtemp)  # appending the x-set to main x-list

        temp = "Initial = "+str(i)
        legend.append(temp)

    # Plotting the graphs
    n = high-low+1
    for k in range(0, n):
        plt.plot(x[k], y[k])
        # for i, j in zip(x[k], y[k]):
        #     plt.text(i, j+0.5, '({}, {})'.format(i, j))


    # plt.legend(legend)
    plt.show()
