import matplotlib.pyplot as plt
import random

def rep(a, yaxis, xaxis):
    yaxis = [a]
    d = a
    
    while d != 1:
        if d%2 == 0:
            d = d/2
            yaxis.append(d)
        else:
            d = 3*d + 1
            yaxis.append(d)
            
    yaxis.append(1)
    yaxis.append(4) 
    yaxis.append(2)
    yaxis.append(1)
    yaxis.append(4) 
    yaxis.append(2)
    yaxis.append(1) 
    yaxis.append(4) 
    yaxis.append(2)
    yaxis.append(1)         
    for i in range(1, (len(yaxis)+1)):
        xaxis.append(i)
        
    return([xaxis, yaxis])

colourset = [ "red", "blue", "green", "yellow", "purple", "orange", "black" ]

g = [15, 12, 3, 5, 8, 9, 10, 7, 13, 11]
usecolor = []

for j in range(0, len(g)):
     n = random.randint(0,6)
     usecolor.append(colourset[n])

for i in range(0, len(g)):
    y = []
    x = []
    print("Series", i+1, "," ,"initial value = ", g[i], "----->",usecolor[i])

    set = rep(g[i], y, x)
    ini = str(g[i])
    label = "initial = " + ini
    
    print(set[1])
    print("\n"*2)
    
    plt.scatter(set[0],set[1],color = usecolor[i])
    plt.plot(set[0], set[1], color = usecolor[i], label = label)
    plt.legend()
        
plt.show()

